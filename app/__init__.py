from flask import Flask, render_template, request, send_from_directory, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from simplekv.db.sql import SQLAlchemyStore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://andriano:andriano1!@backup.c9paluzwflwq.ap-southeast-1.rds.amazonaws.com/jubliaor_platform1?charset=utf8'
db = SQLAlchemy(app)

engine = db.create_engine('mysql://andriano:andriano1!@backup.c9paluzwflwq.ap-southeast-1.rds.amazonaws.com/jubliaor_platform1?charset=utf8')
db = SQLAlchemy(app)
metadata = db.MetaData(bind=engine)
store = SQLAlchemyStore(engine, metadata, 'kvstore')
Session = db.sessionmaker(bind=engine)
session = Session()

import org
app.register_blueprint(org.mod)