import json
from datetime import datetime, timedelta
from celery import Celery
from flask import render_template, request, url_for
from sqlalchemy.exc import OperationalError
from werkzeug.utils import redirect

from bunkmeet import app, db
from bunkmeet.one import bunk
from bunkmeet.two import covid
from bunkmeet.models import User, Teams, Lecture


def make_celery(job):
    celery_job = Celery(
        job.import_name,
        backend=job.config['CELERY_BACKEND'],
        broker=job.config['CELERY_BROKER_URL']
    )
    celery_job.conf.update(job.config)

    class ContextTask(celery_job.Task):
        def __call__(self, *args, **kwargs):
            with job.app_context():
                return self.run(*args, **kwargs)

    celery_job.Task = ContextTask
    return celery_job


celery = make_celery(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def attend():
    try:
        global team
        team = Teams.query.order_by(Teams.id.desc()).first()
    except OperationalError:
        db.create_all()
        team = Teams.query.order_by(Teams.id.desc()).first()
    try:
        load = json.loads(team.teams)
        data = load['array']
        return render_template('success.html', data=data)
    except AttributeError:
        global message
        message = "Please log in first"
        return redirect(url_for('error'))


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/success', methods=['GET', 'POST'])
def fetch_input():
    email = request.form.get("email")
    password = request.form.get("pass")
    user = User(
        email=email,
        password=password)
    db.session.add(user)
    db.session.commit()
    fetch_teams = bunk(email, password)
    if fetch_teams == 'Invalid credentials':
        global message
        message = fetch_teams
        return redirect(url_for('error'))
    else:
        array = {"array": fetch_teams}
        dump = json.dumps(array)
        teams = Teams(teams=dump)
        db.session.add(teams)
        db.session.commit()
        return render_template('success.html', data=fetch_teams)


@app.route('/error')
def error():
    return render_template('error.html', message=message)


# DO NOT USE THE TEST ROUTE IN PRODUCTION
@app.route('/test')
def test():
    return render_template('wait.html')


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    TEAM = request.form.get("team")
    DATE = request.form.get("date")
    TIME = request.form.get("time")
    DURATION = request.form.get("duration")
    lecture = Lecture(
        team=TEAM,
        date=DATE,
        time=TIME,
        duration=DURATION
    )
    db.session.add(lecture)
    db.session.commit()
    final.delay()
    return render_template('finish.html')


@celery.task()
def final():
    user = User.query.order_by(User.id.desc()).first()
    email = user.email
    password = user.password
    eureka = Lecture.query.order_by(Lecture.id.desc()).first()
    team = eureka.team
    date = eureka.date
    time = eureka.time
    duration = eureka.duration
    combine = date + time
    strp = datetime.strptime(combine, '%Y-%m-%d%H:%M')
    until = strp + timedelta(minutes=int(duration))
    covid(email, password, team, strp, until)
