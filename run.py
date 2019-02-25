# -*- coding: utf-8 -*-
import logging
import xmlrpclib
import json
import datetime
import string

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def test_page():
    print('jump in page !')
    return render_template('my_test.html')

# 普通表头
@app.route('/test', methods=['POST'])
def test():
    kw = request.form
    rows = int(kw['rows'])
    page = int(kw['page'])
    sort,sortOrder = None,None
    if 'sort' in kw:
        sort = kw['sort'] # 排序字段
    if 'sortOrder' in kw:
        sortOrder = kw['sortOrder'] # 排序规则
    if 'searchOpts' in kw:
        searchOpts = kw['searchOpts'] # 其他参数
        print(searchOpts)

    alldata = [
                  {
                    "id": 0,
                    "name": "商品 0",
                    "price": "$0",
                    "amount": 3,
                    "remark": "测试"
                  },
                  {
                    "id": 1,
                    "name": "商品 1",
                    "price": "$1",
                    "amount": 4,
                    "remark": "测试"
                  },
                  {
                    "id": 2,
                    "name": "商品 2",
                    "price": "$2",
                    "amount": 8,
                    "remark": "测试"
                  },
                  {
                    "id": 3,
                    "name": "商品 3",
                    "price": "$3",
                    "amount": 2,
                    "remark": "测试"
                  },
                  {
                    "id": 4,
                    "name": "商品 4",
                    "price": "$4",
                    "amount": 90,
                    "remark": "测试"
                  },
                  {
                    "id": 5,
                    "name": "商品 5",
                    "price": "$5",
                    "amount": 2,
                    "remark": "测试"
                  },
                  {
                    "id": 6,
                    "name": "商品 6",
                    "price": "$6",
                    "amount": 3,
                    "remark": "测试"
                  },
                  {
                    "id": 7,
                    "name": "商品 7",
                    "price": "$7",
                    "amount": 7,
                    "remark": "测试"
                  },
                  {
                    "id": 8,
                    "name": "商品 8",
                    "price": "$8",
                    "amount": 39,
                    "remark": "测试"
                  },
                  {
                    "id": 9,
                    "name": "商品 9",
                    "price": "$9",
                    "amount": 78,
                    "remark": "测试"
                  },
                  {
                    "id": 10,
                    "name": "商品 10",
                    "price": "$10",
                    "amount": 30,
                    "remark": "测试"
                  },
                  {
                    "id": 11,
                    "name": "商品 11",
                    "price": "$11",
                    "amount": 32,
                    "remark": "测试"
                  },
                  {
                    "id": 12,
                    "name": "商品 12",
                    "price": "$12",
                    "amount": 12,
                    "remark": "测试"
                  },
                  {
                    "id": 13,
                    "name": "商品 13",
                    "price": "$13",
                    "amount": 76,
                    "remark": "测试"
                  },
                  {
                    "id": 14,
                    "name": "商品 14",
                    "price": "$14",
                    "amount": 10,
                    "remark": "测试"
                  },
                  {
                    "id": 15,
                    "name": "商品 15",
                    "price": "$15",
                    "amount": 9,
                    "remark": "测试"
                  },
                  {
                    "id": 16,
                    "name": "商品 16",
                    "price": "$16",
                    "amount": 8,
                    "remark": "测试"
                  },
                  {
                    "id": 17,
                    "name": "商品 17",
                    "price": "$17",
                    "amount": 1,
                    "remark": "测试"
                  },
                  {
                    "id": 18,
                    "name": "商品 18",
                    "price": "$18",
                    "amount": 99,
                    "remark": "测试"
                  },
                  {
                    "id": 19,
                    "name": "商品 19",
                    "price": "$19",
                    "amount": 100,
                    "remark": "测试"
                  },
                  {
                    "id": 20,
                    "name": "商品 20",
                    "price": "$20",
                    "amount": 109,
                    "remark": "测试"
                  }
                ]

    startIndex = rows * (page - 1)
    endIndex = rows * page

    if sort:
         alldata.sort(key=lambda x: x[sort])
         if sortOrder == "desc":
             alldata.reverse()

    '''
          替换成SQL的时候，参照如下
          select * from tb_goods where ... limit A offset B order by C D;
          A是rows, B是startIndex, C是sort, D是sortOrder
    '''

    mydata = alldata[startIndex:endIndex]
    total = len(alldata)

    return json.dumps({'rows':mydata,
                       'total':total});


# 组合表头
@app.route('/test2', methods=['POST'])
def test2():
    kw = request.form
    rows = int(kw['rows'])
    page = int(kw['page'])
    sort,sortOrder = None,None
    if 'sort' in kw:
        sort = kw['sort'] # 排序字段
    if 'sortOrder' in kw:
        sortOrder = kw['sortOrder'] # 排序规则
    if 'searchOpts' in kw:
        searchOpts = kw['searchOpts'] # 其他参数
        print(searchOpts)

    alldata = [
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"12","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"32","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"},
                  {"name":"滚筒","meidiNum":"10","meidiPercent":"29%","meidiNum2":"10","meidiPercent2":"29%","songxiaNum":"10","songxiaPercent":"29%","songxiaNum2":"10","songxiaPercent2":"29%", "sanxingNum":"10", "sanxingPercent":"29%","sanxingNum2":"10", "sanxingPercent2":"29%","haierNum":"10","haierPercent":"29%","haierNum2":"10","haierPercent2":"29%","boshiNum":"10","boshiPercent":"29%","ximenziNum":"10","ximenziPercent":"29%","ximenziNum2":"10","ximenziPercent2":"29%","zhigaoNum":"10","zhigaoPercent":"29%","zhigaoNum2":"10","zhigaoPercent2":"29%","yinghuaNum":"10","yinghuaPercent":"29%","yinghuaNum2":"10","yinghuaPercent2":"29%","changhongNum":"10","changhongPercent":"29%","xiaotianeNum":"10","xiaotianePercent":"29%"}
                ]

    startIndex = rows * (page - 1)
    endIndex = rows * page

    if sort:
         alldata.sort(key=lambda x: x[sort])
         if sortOrder == "desc":
             alldata.reverse()

    '''
          替换成SQL的时候，参照如下
          select * from tb_goods where ... limit A offset B order by C D;
          A是rows, B是startIndex, C是sort, D是sortOrder
    '''

    mydata = alldata[startIndex:endIndex]
    total = len(alldata)

    return json.dumps({'rows':mydata,
                       'total':total});

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)