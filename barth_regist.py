#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request
import wget
import glob
import os
# localhost:8080
@route('/')
def title():
    # views/title.tplを呼ぶ
    return template('regist')


# localhost:8080/show
@route('/show', method='GET')
def men():
    # GETパラメータの取得(username, men)
    username = request.query.username
    men = request.query.men
    print username
    # filename = wget.download(username)
    print men
    # Controller部 =======================================
    os.chdir("/Users/nakamurajun/Desktop/jar/")
    tmp = glob.glob("*.jar")
    print tmp
    # View部 =============================================
    # views/show.tplを呼ぶ
 #   return template('show', name=username, men=menname)


# ビルドインサーバの実行
run(host='localhost', port=8080, debug=True, reloader=True)
