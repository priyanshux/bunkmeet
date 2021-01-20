from bunkmeet import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User(" \
               f"'{self.email}', '{self.password}')"


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teams = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User(" \
               f"'{self.teams})"


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"User(" \
               f"'{self.team}', '{self.date}', '{self.time}', '{self.duration}', '{self.speed}')"
