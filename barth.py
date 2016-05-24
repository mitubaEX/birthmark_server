from bottle import route, run, template, request
import os
import commands

@route('/')
def index():
    return template("search")

@route('/upload', method='POST')
def do_upload():
    barthmark_kind = ["cvfv", "fmc", "fuc", "kgram", "smc", "uc", "wsp"]
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    #print "hello"
    #file check
    #if ext in ('*.jar'):
        #print "this is jar"
    upload.save("/Users/nakamurajun/barthmark_server/tmp",overwrite=True)
    os.chdir("./barthmark")
    os.system("rm *.csv")
    for tmp in barthmark_kind:
        os.system("java -jar /Users/nakamurajun/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+tmp+" extract /Users/nakamurajun/barthmark_server/tmp/"+upload.filename+" > /Users/nakamurajun/barthmark_server/barthmark/"+upload.filename+"-"+tmp+".csv")
    os.system("python birth_curl.py")
    os.system("python fuzzy_curl.py")
    return template("search")

run(host='0.0.0.0', port=8080)
