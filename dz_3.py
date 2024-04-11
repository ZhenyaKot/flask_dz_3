from flask import Flask, render_template, request
from model_dz import db, Person
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_dz.db'
db.init_app(app)


@app.cli.command('init-db-dz')
def init_db_dz():
    db.create_all()
    print('ВСЕ ПРОШЛО ХОРОШО!')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        person = Person(id=random.randint(1, 1000), first_name=first_name, last_name=last_name, email=email,
                        password=password)
        db.session.add(person)
        db.session.commit()
    return render_template('index.html')
