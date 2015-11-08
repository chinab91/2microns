from app import db #login_serializer, store
#TODO: remove session_info from database
#Add kv_store

class Attendee_Login(db.Model):
    #db.Model is my database
    __tablename__ = 'attendee_login'
    id_attendee_login = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)