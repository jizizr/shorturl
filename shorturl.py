from flask import Flask,redirect, render_template, session, request
#from flask_bootstrap import Bootstrap
import gevent.pywsgi
from db_manager import db_manager as dm
import os
import random

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['PORT'] = 81
app.config['TIMEOUT'] = 10  # In seconds
app.config['VERSION'] = 1
#bootstrap = Bootstrap(app)
db=dm()
name="URL"

def generate_random_url(length):
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    random_url = ''.join(str(random.choice(base_str)) for _ in range(length))
    return random_url

print("working")

@app.route('/',methods = ['GET','POST'])
def index():
    if  request.method == "POST":
        url = request.form.get('source_url')
        s_url = request.form.get('short_url')
        if s_url.strip() == '':
            s_url = generate_random_url(4)
        if db.serch_data(name,s_url) == None:
            return render_template('success.html',a=db.add_data_to_db(name,url,s_url),surl=f'添加成功 https://s.z-r.cc/{s_url}')
        else:
            return render_template('index.html',a=True)
    return render_template('index.html',a=False)

@app.route('/login',methods=['GET',"POST"])
def login():
    if  request.method == "POST":
        user=request.form.get('user')
        pwd=request.form.get('pwd')
    else:
        return render_template('login.html')
    if user=='admin' and pwd=='123':
        session['user_info']=user
        return redirect('/admin')
    else:
        return redirect('/login')

@app.route('/admin',methods=['GET',"POST"])
def admin():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    else:
        if  request.method == "GET" and request.args:
            request_parameters = request.args
            url = request_parameters.get('url')
            db.del_data(name,url)
            return redirect('/admin')
        return render_template('admin.html',rows = db.serch_all(name))


@app.route('/<url>')
def jump(url):
    source = db.serch_data(name,url)
    if source == None:
        return "你访问的页面不存在!"
    else:
        if "http" not in source:
            source=f"http://{source}"
        return redirect(source, code=301)
@app.errorhandler(404)
def page_not_found(e):
    return "<p>The resource could not be found.</p>", 404

if __name__ == '__main__':
    app_server = gevent.pywsgi.WSGIServer(('0.0.0.0', app.config['PORT']), app,log=None)
    app_server.serve_forever()
