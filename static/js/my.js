/**
 * Created by HELP on 2018/4/13.
 */
$(function(){
    $.getJSON("static/data.json",function(data){
        $("#mytab").bootstrapTable({data: data,
            pagination:true,
            showColumns: true,
            columns:[
                {
                    title:'全选',
                    field:'id',
                    checkbox:true,
                    width:25,
                    align:'center',
                    valign:'middle'

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
            ]})
    });
});

