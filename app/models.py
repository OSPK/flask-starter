from app import db


class Universities(db.Model):
    __tablename__ = 'universities'
    id = db.Column(db.Integer, primary_key=True)
    uni_name = db.Column(db.String(512), nullable=False)
    city = db.Column(db.String(512), nullable=False)
    province = db.Column(db.String(512), nullable=False)
    pub_pri = db.Column(db.String(32), nullable=False)
    website = db.Column(db.String(512))
    govt = db.Column(db.String(512), nullable=False)
    campuses = db.Column(db.Integer)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    # def __repr__(self):
    #     return '<User %r>' % self.username
