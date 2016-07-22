# search server
from bottle import route, run, template, request, redirect
import os
import commands
import sys

@route('/')
def index():
    return template("search")

@route('/upload', method='POST')
def do_upload():
    barthmark_kind = sys.argv
    del barthmark_kind[0]
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload.save("./data/jar",overwrite=True)
    os.chdir("./data/search_birthmark")
    os.system("rm *.csv")
    for tmp in barthmark_kind:
        os.system("java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+tmp+" extract ../jar/"+upload.filename+" > ../search_birthmark/"+upload.filename+"-"+tmp+".csv")

    os.system("bash ../../script/birth_search/birth_main.sh")
    os.system("bash ../../script/fuzzy_search/fuzzy_main.sh")
    redirect("/")
    return template("search")

run(host='0.0.0.0', port=8080)
