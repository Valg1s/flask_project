from sweter import db, app


class Services(db.Model):
    __tablename__ = "services"
    services_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(512),nullable=False)
    cost = db.Column(db.Integer(), nullable=False)


class Statement(db.Model):
    __tablename__ = "statement"
    statement_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.Integer(), nullable=False)
    message = db.Column(db.String(1024),nullable=False)


with app.app_context():
    db.create_all()
