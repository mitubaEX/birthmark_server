from bottle import route, run, template, request, redirect
import os
import commands

@route('/')
def index():
    return template("search")

@route('/upload', method='POST')
def do_upload():
    barthmark_kind = ["cvfv", "fmc", "fuc", "2gram", "3gram", "smc", "uc", "wsp"]
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload.save("./jar",overwrite=True)
    os.chdir("./birthmark")
    os.system("rm *.csv")
    for tmp in barthmark_kind:
        os.system("java -jar ../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+tmp+" extract ../jar/"+upload.filename+" > ./"+upload.filename+"-"+tmp+".csv")
    os.system("python birth_search.py")
    os.system("python fuzzy_search.py")
    redirect("/")
    return template("search")

run(host='0.0.0.0', port=8080)
