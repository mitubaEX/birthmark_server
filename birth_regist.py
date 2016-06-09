from bottle import route, run, template, request
import os
import commands

@route('/')
def index():
    return template("regist")

@route('/upload', method='POST')
def do_upload():
    barthmark_kind = ["cvfv", "fmc", "fuc", "kgram", "smc", "uc", "wsp"]
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload.save("./jar",overwrite=True)
    os.chdir("./jar")
    os.system("sh find_jar_ext_birth_xml.sh")
    return template("search")

run(host='0.0.0.0', port=8080)
