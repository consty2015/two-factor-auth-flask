import os

SECRET_KEY = 'top-secret'
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Welcome123@alahdb.c2fba95zjgl1.us-east-1.rds.amazonaws.com/"
#os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
