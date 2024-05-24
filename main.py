from flask import Flask, url_for, flash
from flask import request, redirect, send_file
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
import hashlib
import datetime
import sqlalchemy
from data import db_session
from data.users import User
from data.news import News
from sqlalchemy.orm import Session, sessionmaker
UPLOAD_FOLDER = 'C:\\Users\\dog.slava-ПК\\Desktop\\flask1'




app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)

@app.route('/sample_page')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""

@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''


@app.route('/registration', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        request.method == 'POST'
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Регистрация</title>
                          </head>
                          <body>
                            <h1>Новый ящик</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="sname" placeholder="Введите фамилию" name="sname">
                                    <input type="text" class="form-control" id="fname" placeholder="Введите имя" name="fname">
                                    <input type="text" class="form-control" id="email" placeholder="Введите логин" name="email">
                                    <input type="text" class="form-control" id="password" placeholder="Введите пароль" name="password">
            
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <h6>Ваши интересы</h6>
                                     <div class="form-group form-check">
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Компьютерные игры</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Спорт</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Искусство</label></div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Фильмы и видео</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Еда и кулинария</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Пирожки</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="w" name="w">
                                            <label class="form-check-label" for="w">Наука</label>
                                        </div>



                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about">Напишите, зачем вы хотите зарегистрироваться</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы регалярно поддерживать общение?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        
        # return request.form
        db_sess = db_session.create_session()
        #if db_sess.query(User).filter(User.email == request.form["email"]).first()["id"]:   db_sess.query(User).get(0)
        if db_sess.query(User).filter(User.email == request.form["email"]).first():
            return "Пользователь с таким логином уже существует"
        else:
            nchel(request.form["password"], 365, request.form["fname"], request.form["sname"], request.form["email"], "/n".join([request.form["about"], request.form["accept"], request.form["class"], request.form["file"], request.form["sex"], request.form["w"]]))
            return redirect('/send')
    


@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'GET':
        return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Отправка пакета информации</title>
                      </head>
                      <body>
                      <div>
                      <form class="send_form" method="post" enctype="multipart/form-data">
                        <h1>Отправка пакета информации</h1>
                        <div class="alert alert-primary" role="alert">
                          После ввода данных, проверьте заполненные формы на правильность, пожалуйста!
                        </div>
                        <input type="text" class="form-control" id="email" placeholder="Введите логин" name="email">
                        <input type="text" class="form-control" id="password" placeholder="Введите пароль" name="password">
                        <input type="text" class="form-control" id="chel" placeholder="Введите логин получателя" name="chel">
                        <h1></h1>
                        <input type="file" id="file" name="file">
                        <input type="submit" value="Upload">
                      </form>
                      </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            db_sess = db_session.create_session()
            if cchel(request.form["password"], db_sess.query(User).filter(User.email == request.form["email"]).first().hashed_password, db_sess.query(User).filter(User.email == request.form["email"]).first().salt):
                with open(filename, "rb") as ff:
                    nN(request.form["email"], ff.read(), request.form["chel"])
                os.remove(filename)
                return redirect('/send')
            else:
                return "Ошибоцка"
        #return request.form
        #if db_sess.query(User).filter(User.email == request.form["email"]).first()["id"]:   db_sess.query(User).get(0)
        # return redirect('/login')


@app.route('/pochta', methods=['POST', 'GET'])
def pochta():
    if request.method == 'GET':
        return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Получение архива информации</title>
                      </head>
                      <body>
                      <div>
                      <form class="send_form" method="post" enctype="multipart/form-data">
                        <h1>Получение архива информации</h1>
                        <div class="alert alert-primary" role="alert">
                          После ввода данных, проверьте заполненные формы на правильность, пожалуйста!
                        </div>
                        <input type="text" class="form-control" id="email" placeholder="Введите логин" name="email">
                        <input type="text" class="form-control" id="password" placeholder="Введите пароль" name="password">
                        <h1></h1>
                        <input type="submit" value="Upload">
                      </form>
                      </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        db_sess = db_session.create_session()
        if cchel(request.form["password"], db_sess.query(User).filter(User.email == request.form["email"]).first().hashed_password, db_sess.query(User).filter(User.email == request.form["email"]).first().salt):
            k = 0
            for i in db_sess.query(News).filter(News.title == request.form["email"]).all():
                with open(hex(k), "wb") as ff:
                    ff.write(i.content)
            return send_file(hex(k))
        else:
            return "Ошибоцка"


def nN(title, content, user_id):
    nn = News()
    nn.title = title
    nn.content = content
    nn.user_id = user_id
    nn.is_private = True
    db_sess = db_session.create_session()
    db_sess.add(nn)
    db_sess.commit()


def nchel(password, salt, fname, sname, email, about):
    user = User()
    user.fname = fname
    user.sname = sname
    user.about = about
    user.email = email
    salt = os.urandom(32)
    user.salt = salt
    key = hashlib.pbkdf2_hmac(
    'sha256', # Используемый алгоритм хеширования
    password.encode('utf-8'), # Конвертирование пароля в байты
    salt, # Предоставление соли
    100000, # Рекомендуется использоваться по крайней мере 100000 итераций SHA-256 
    dklen=128 # Получает ключ в 128 байтов
    )
    user.hashed_password = key
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

def cchel(password, key, salt):
    return hashlib.pbkdf2_hmac(
    'sha256', # Используемый алгоритм хеширования
    password.encode('utf-8'), # Конвертирование пароля в байты
    salt, # Предоставление соли
    100000, # Рекомендуется использоваться по крайней мере 100000 итераций SHA-256 
    dklen=128 # Получает ключ в 128 байтов
    ) == key
    


if __name__ == '__main__':
    db_session.global_init("db/base.db")
    app.run(port=8080, host='127.0.0.1')
