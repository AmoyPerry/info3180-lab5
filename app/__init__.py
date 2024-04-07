from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect 

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.from_object(Config)


# app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views