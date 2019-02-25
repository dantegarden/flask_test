(function(){
    $.fn.generalTable = function(queryType, inputOpts, locale) {
        if (locale == null) {
            locale = "zh";
        }
        if (queryType == null) {
            queryType = "client";
        }

        var $table_div, $toolbar, table;
        $table_div = this;

        var defaults, default_client, default_server, opts, fnPostBody, maintainSelects, fnMaintainSaveSelected, fnMaintainRemoveSelected, fnMaintainResponseHandler;

        defaults = {
            cache: false,
            //height: 400, //表高度
            striped: true, //是否显示行间隔色
            pagination: false,
            pageNumber: 1, //初始化加载第一页，默认第一页
            pageSize: 10,
            pageList: [10, 20, 50, 100],
            showColumns: false, //列筛选器 在组合列头下有bug
            showRefresh: false, //刷新按钮
            showPaginationSwitch: false,//显示or隐藏分页按钮
            showExport: false, //导出按钮
            enableExportSelection: false, //显示导出类型选择框
            exportDataType: "all", //导出类型 basic默认 all全部 selected选中
            exportTypes: ['csv','excel'], //导出选项
            exportOptions: {
                //ignoreColumn:[0,1], //忽略某一列
                //ignoreRow:[],  //忽略某一行
                fileName:"下载表格",//文件名
                mso:{worksheetName:"表格"},
                excelstyles: ['background-color', 'color', 'font-size', 'font-weight']
            },
            //toolbar:"#toolbar", //指定工具栏
            toolbarAlign: 'left', //工具栏对齐方式
            buttonsAlign: 'right', //按钮对齐方式
            clickToSelect: true,
            saveSelected: false, //翻页保留选中的选择框
            search: false,//是否显示右上角的搜索框
            singleSelect: false,//复选框只能选择一条记录
            locale: locale, //国际化
            // fixedColumns: false, //启用固定列头
            // fixedNumber: 1, //固定列头数量(从左起)
            fixedColHeader: false,
            fixedColNumber: 1,
            showFooter: false,//不展示合计列
            onPreBody: function(data){
                data = fnMaintainResponseHandler().call(this, data);
                if(opts.fnPreBody === "function"){
                    data = opts.fnPreBody.call(this, data);
                }
                return data;
            },
            onCheck: function(row){
                fnMaintainSaveSelected().call(this, new Array(row));
                if(opts.fnCheck === "function"){
                    opts.fnCheck.call(this, row);
                }
            },
            onUncheck: function(row){
                fnMaintainRemoveSelected().call(this, new Array(row));
                if(opts.fnUnCheck === "function"){
                    opts.fnUnCheck.call(this, row);
                }
            },
            onCheckAll: function(rows){
                fnMaintainSaveSelected().call(this, rows);
                if(opts.fnCheckAll === "function"){
                    opts.fnCheckAll.call(this, rows);
                }
            },
            onUncheckAll: function(rows){
                fnMaintainRemoveSelected().call(this, rows);
                if(opts.fnUncheckAll === "function"){
                    opts.fnUncheckAll.call(this, rows);
                }
            },
            onScrollBody: function(){ //滚动body时触发
                //解决纵向滚动条错位
                var $theader,$tbody
                $theader = $table_div.find("div.fixed-table-header");
                $tbody = $table_div.find("div.fixed-table-body");
                $tfooter = $table_div.find("div.fixed-table-footer");
                $theader.css("margin-right", $tbody[0].offsetWidth - $tbody[0].clientWidth);
                $tfooter.css("margin-right", $tbody[0].offsetWidth - $tbody[0].clientWidth);

                if(opts.fnScrollBody === "function"){
                    opts.fnScrollBody.call(this);
                }
            },
            columns:[]
        }

        default_client = {
            data:[],
            method: 'get',
            sidePagination: 'client', //指定客户端分页
        }

        default_server = {
            method: 'post',
            url: "",
            dataType: "json",
            contentType: "application/x-www-form-urlencoded",
            sidePagination: 'server', //指定服务端分页
            silent: false, //设置为 false 将在点击分页按钮时，自动记住排序项。仅在 sidePagination设置为 server时生效。
            queryParams: function(params){//请求服务数据时所传参数
                var fnData = {
                    rows: params.limit,//页面大小
                    page: (params.offset / params.limit) + 1, //页码
                    sort: params.sort,      //排序列名
                    sortOrder: params.order //排位命令（desc，asc）
                };
                //自定义查询参数
                if(typeof opts.fnQueryParams === "function"){
                    opts.fnQueryParams.call(this, fnData)
                }
                return fnData;
            },
            queryParamsType: 'limit',//查询参数组织方式
            responseHandler: function(res){return res;},//在ajax获取到数据，渲染表格之前，修改数据源
            onPostBody: function(){
                fnPostBody().call(this);
                if(typeof opts.onSucess === "function"){
                    opts.onSucess.call(this);
                }
            }
        }

        if(queryType === "client") {//客户端模式
            opts = $.extend(true, $.extend(true, default_client, defaults), inputOpts);
        }else if(queryType === "server") {//服务端模式
            opts = $.extend(true, $.extend(true, default_server, defaults), inputOpts);
        }else{
            console.error("do not support query type : " + queryType);
        }

        //工具类
        $.generalTableUtilities = {
            isNumber: function isNumber(val){
                var regPos = /^\d+(\.\d+)?$/; //非负浮点数
                var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/; //负浮点数
                if(regPos.test(val) || regNeg.test(val)){
                    return true;
                }else{
                    return false;
                }
            }
        }

        //自动生成表头
        if(opts.columns.length < 1 && opts.columnsSeed && opts.columnsSeed instanceof Array){
            var seeds = opts.columnsSeed;
            var columns = [];
            var columDepth = [];

            var default_col = {
                halign: "center",
                valign: "middle",
                align: "center",
                sortable: false
            }

            var iteratorDepth = function(obj,depth){
                if(!depth){
                    depth = 0;
                }
                if(!columns[depth]){
                    columns[depth] = [];
                }
                columDepth.push({'col':obj, 'depth': depth});
                if(obj.subCol){
                    for (var i = 0; i < obj.subCol.length; i++) {
                         iteratorDepth(obj.subCol[i], depth+1)
                    }
                }
            }

            var getDepth = function(obj,depth){
                if(!depth){
                    depth = 0;
                }

                if(obj.subCol){
                    depth += 1;
                    for (var i = 0; i < obj.subCol.length; i++) {
                         depth = Math.max(depth,getDepth(obj.subCol[i], depth))
                    }
                }
                return depth;
            }

            var iteratorWidth = function(obj,width){
                if(!width){
                    width = 0;
                }
                if(obj.subCol){
                    for (var i = 0; i < obj.subCol.length; i++) {
                        width = iteratorWidth(obj.subCol[i],width);
                    }
                    return width
                }else{
                    width += 1
                    return width;
                }
            }

            var getHeight = function(col,depth){
                var arr = $.grep(columDepth, function(n,i){
                    return n.depth == depth
                });

                if(arr.length > 1 && !col.subCol){
                    var a_depth = [];
                    arr.forEach(function(item){
                        var d = getDepth(item.col);
                        if(d === 1){d+=1}
                        a_depth.push(d)
                    })
                    return Math.max.apply(Math, a_depth);
                }else{
                    return 1;
                }
            }


            for(var i in seeds){iteratorDepth(seeds[i])};
            for(var i in columDepth){
                var col_dep = columDepth[i], ref1,ref2,ref3,ref4,ref5,ref6,ref7,ref8,ref9;
                var col = col_dep.col, depth = col_dep.depth;

                var mycol = {};
                mycol.title = (ref1 = col.colName) != null ? ref1 : '',
                (ref2 = col.colKey)? (mycol.field = ref2) : null;
                (ref3 = iteratorWidth(col))? (mycol.colspan = ref3) : null;
                (ref4 = getHeight(col,depth))?(mycol.rowspan = ref4) :null;
                (ref5 = col.formatter)?(mycol.formatter = ref5): null;
                ((ref7 = col.sortable) || typeof col.sortable === "boolean")?(mycol.sortable = ref7):null;
                ((ref8 = col.switchable) || typeof col.switchable === "boolean")?(mycol.switchable = ref8):null;
                (ref9 = col.width)?(mycol.width = ref9):null;

                mycol = $.extend(true, {}, default_col, mycol);

                if(ref2 && opts.showFooter){
                    var footerFormatter = function (value) {
                        var count = 0, v = 0;
                        for (var i in value) {
                            v = value[i][this.field];
                            if($.generalTableUtilities.isNumber(v)){
                                count += parseFloat(value[i][this.field]);
                            }
                        }
                        if(!$.generalTableUtilities.isNumber(count))
                            count = "-";
                        return count;
                    }
                    mycol['footerFormatter'] = (ref6 = col.footerFormatter)?ref6:footerFormatter;
                }

                columns[depth].push(mycol)

            }
            opts.columns = columns;
        }

        //取得表元素
        if($(this).find("table").length > 0){
            table = $(this).find("table")[0];
        }else{
            table = document.createElement("table");
            $(this).append(table);
        }

        //自适应高度
        if(!opts.height){
            function tableHeight(){
                //可以根据自己页面情况进行调整
                opts.height = $(window).height() - $(table).offset().top
                return opts.height;
            }
            tableHeight.apply();
            $(window).resize(function() {
                $(table).bootstrapTable('resetView', {
                    height: tableHeight()
                })
            })
        }

        /**eleFixed**/
        $.eleFixed = {
          targets: [],
          push: null,
          distory: null,
          handler: null,
          delete: null
        }
        $.eleFixed.push =  function (option) {
          if(typeof option !== 'object') return console.error('eleFixed: push param must be a Object')
          if(!option.target && !isDOM(option.target)) return console.error('eleFixed: target must be a HTMLElement')
          if(((option.offsetTop && typeof option.offsetTop == 'number') || option.offsetTop === 0 )
              || ((option.offsetLeft && typeof option.offsetLeft == 'number') || option.offsetLeft === 0 ) ){
          }else{
            return console.error('eleFixed: param\'s offsetLeft or offsetTop must be a Number')
          }
          $.eleFixed.targets.push(option)
        }
        $.eleFixed.handler = function(){
          for(var i in $.eleFixed.targets){
              var offsetLeft = window.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft || ($.eleFixed.targets[i].fixed_ref_x?$.eleFixed.targets[i].fixed_ref_x.scrollLeft:0) || this.scrollLeft;
              var offsetTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || ($.eleFixed.targets[i].fixed_ref_y?$.eleFixed.targets[i].fixed_ref_y.scrollTop:0) || this.scrollTop;

              if(typeof $.eleFixed.targets[i].offsetLeft == "number"){
                  if(offsetLeft > $.eleFixed.targets[i].offsetLeft){
                    var _target = $.eleFixed.targets[i].target;// = $.eleFixed.targets[i].target.style.backgroundColor;
                    $(_target).css({
                        "background-color": "rgb(255,255,255)",
                        "font-weight":"bold"
                    })
                    $.eleFixed.targets[i].target.style.transform = 'translateX('+ (offsetLeft - $.eleFixed.targets[i].offsetLeft) +'px)'
                  }else{
                    $.eleFixed.targets[i].target.style.transform = 'translateX(0px)'
                  }
            }
            if($.eleFixed.targets[i].offsetTop){
              if(offsetTop > $.eleFixed.targets[i].offsetTop){
                $.eleFixed.targets[i].target.style.transform = 'translateY('+ (offsetTop - $.eleFixed.targets[i].offsetTop) +'px)'
              }else{
                $.eleFixed.targets[i].target.style.transform = 'translateY(0px)'
              }
            }
          }
        }
        $.eleFixed.delete = function (target) {
          if(target && isDOM(target)){
            var targets = $.eleFixed.targets
            for(var i in targets){
              if(target.isEqualNode(targets[i].target)){
                target.style.transform = 'translateY(0px)'
                targets.splice(i, 1)
                break
              }
            }
          }
        }
        $.eleFixed.distory = function () {
          window.removeEventListener('scroll', $.eleFixed.handler)
          for(var i in $.eleFixed.targets){
            $.eleFixed.targets[i].target.style.transform = 'translateY(0px)'
          }
          $.eleFixed = null
        }

        maintainSelects = [];

        fnMaintainSaveSelected = function(){
            return function(rows){
                if(opts.saveSelected && opts.idField){
                    $.each(rows, function(i, row){
                        if($.inArray(row[opts.idField],maintainSelects)==-1){
                            maintainSelects[maintainSelects.length] = row[opts.idField];
                        }
                    });
                    console.log(maintainSelects);
                }
            }
        }

        fnMaintainRemoveSelected = function(){
            return function(rows){
                if(opts.saveSelected && opts.idField){
                    $.each(rows, function(i, row){
                        var index = $.inArray(row[opts.idField],maintainSelects);
                        if(index!=-1){maintainSelects.splice(index,1); }
                    });
                    console.log(maintainSelects);
                }
            }
        }

        fnMaintainResponseHandler = function(){
            return function(data){
                if(opts.saveSelected && opts.idField){
                    $.each(data, function(i, row){
                        var index = $.inArray(row[opts.idField],maintainSelects);
                        if(index!=-1){
                            row['multi-select'] = true;
                        }
                    });
                }
                return data;
            }
        }

        fnPostBody = function(){
            return function(){
                //冻结列
                if(opts.fixedColHeader){
                    var index,i;
                    (index = opts.fixedColNumber)?'':(index = 1)
                    for(i = 1; i<=index; i++){
                        $(table).find("tbody td:nth-child("+ i +")").each(function(e){
                            $(this).css({
                                "background-color": "rgb(255,255,255)",
                                "font-weight":"bold"
                            });

                            var left = $(this).offsetLeft;
                            left = !isNaN(left)? left : 0;
                            $.eleFixed.push({target:$(this)[0], offsetLeft: left, fixed_ref_x: table.closest(".fixed-table-body") });
                        })
                    }
                    table.closest(".fixed-table-body").addEventListener('scroll', $.eleFixed.handler);
                }

            }
        }

        //渲染表
        $(table).bootstrapTable(opts);

        return this;
    }
}).call(this);