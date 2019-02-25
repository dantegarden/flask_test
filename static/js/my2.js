/**
 * Created by HELP on 2018/4/17.
 */
$(function(){
        $.getJSON("static/data.json",function(data){

            var colsSeed = [
                 {colName:"洗衣机统计表",subCol:[
                    {colName:"功能分组", colKey:"name", footerFormatter:function(value){
                            return "合计"
                        }},
                    {colName:"美的", subCol:[
                            {colName:"国内", subCol:[
                                {colName:"数量", colKey:"meidiNum", visible:false},
                                {colName:"占比", colKey:"meidiPercent"}
                            ]},
                            {colName:"国外", subCol:[
                                {colName:"数量", colKey:"meidiNum2"},
                                {colName:"占比", colKey:"meidiPercent2", formatter:function(value,row,index){
                                     return value + "%"
                                    }}
                            ]}
                    ]},
                    {colName:"三星", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"sanxingNum"},
                            {colName:"占比", colKey:"sanxingPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"sanxingNum2"},
                            {colName:"占比", colKey:"sanxingPercent2"}
                        ]}
                    ]},
                    {colName:"松下", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"songxiaNum"},
                            {colName:"占比", colKey:"songxiaPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"songxiaNum2"},
                            {colName:"占比", colKey:"songxiaPercent2"}
                        ]}
                    ]},
                    {colName:"海尔", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"haierNum"},
                            {colName:"占比", colKey:"haierPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"haierNum2"},
                            {colName:"占比", colKey:"haierPercent2"}
                        ]}
                    ]},
                    {colName:"博世", subCol:[
                        {colName:"数量", colKey:"boshiNum"},
                        {colName:"占比", colKey:"boshiPercent"}
                    ]},
                    {colName:"西门子", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"ximenziNum"},
                            {colName:"占比", colKey:"ximenziPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"ximenziNum2"},
                            {colName:"占比", colKey:"ximenziPercent2"}
                        ]}
                    ]},
                    {colName:"长虹", subCol:[
                        {colName:"数量", colKey:"changhongNum"},
                        {colName:"占比", colKey:"changhongPercent"}
                    ]},
                    {colName:"樱花", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"yinghuaNum"},
                            {colName:"占比", colKey:"yinghuaPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"yinghuaNum2"},
                            {colName:"占比", colKey:"yinghuaPercent2"}
                        ]}
                    ]},
                    {colName:"志高", subCol:[
                        {colName:"国内", subCol:[
                            {colName:"数量", colKey:"zhigaoNum"},
                            {colName:"占比", colKey:"zhigaoPercent"}
                        ]},
                        {colName:"国外", subCol:[
                            {colName:"数量", colKey:"zhigaoNum2"},
                            {colName:"占比", colKey:"zhigaoPercent2"}
                        ]}

                    ]},
                    {colName:"小天鹅", subCol:[
                        {colName:"数量", colKey:"xiaotianeNum"},
                        {colName:"占比", colKey:"xiaotianePercent"}
                    ]}
                 ]}
                ]


            // $("#output2").generalTable("server", {
            //     url:"/test2",
            //     //data: data,
            //     pagination:true,
            //     showExport: true,
            //     enableExportSelection:true,
            //     fnQueryParams: function(fnData){ //查询参数
            //         fnData['searchOpts'] = "my query params";
            //     },
            //     height:600,
            //     columnsSeed: colsSeed, //生成标准树形表头
            //     fixedColHeader: true, //启用冻结列
            //     fixedColNumber: 1  //冻结几列
            //     // onPostBody: function(data){ //渲染完成后回调函数
            //     // }
            // });

            $("#output").generalTable("client", {
                data: data,
                pagination:true,
                showColumns: true,
                showExport: true,
                enableExportSelection:true,
                height:600,
                idField: 'id', //每行的唯一标识
                saveSelected: true, //翻页保留选择框状态，需要与idField配合使用
                columns:[
                {
                    title:'全选',
                    field:'multi-select',
                    checkbox:true,
                    width:25,
                    align:'center',
                    valign:'middle'

                },
                {
                    title:'ID',
                    field:'id',
                    visible:false
                },
                {
                    title:'商品名',
                    field:'name',
                    sortable:true
                },
                {
                    title:'单价',
                    field:'price',
                    sortable:true
                },
                {
                    title:'数量',
                    field:'amount',
                    sortable:true
                },
                {
                    title:'备注',
                    field:'remark',
                    visible: false
                }
            ]

            });
        });

        // $("#output").generalTable("server", {
        //     url:"/test",
        //     pagination:true,
        //     showColumns: true,
        //     showExport: true,
        //     enableExportSelection:true,
        //     queryParams: function(params){
        //       return {
        //             rows: params.limit,//页面大小
        //             page: params.offset / params.limit + 1, //页码
        //             sort: params.sort,      //排序列名
        //             sortOrder: params.order, //排位命令（desc，asc）
        //             searchOpts:'商品 9'
        //       };
        //     },
        //     columns:[
        //         {
        //             checkbox: true, //是否显示复选框
        //             field : "multi-select",
        //             visible: true,
        //             width: 25
        //         },
        //         {
        //             title:'ID',
        //             field:'id',
        //             visible: false
        //         },
        //         {
        //             title:'商品名',
        //             field:'name',
        //             sortable:true
        //         },
        //         {
        //             title:'单价',
        //             field:'price',
        //             sortable:true
        //         },
        //         {
        //             title:'数量',
        //             field:'amount',
        //             sortable:true
        //         },
        //         {
        //             title:'备注',
        //             field:'remark',
        //             visible: false
        //         }
        //     ]
        // });
});
