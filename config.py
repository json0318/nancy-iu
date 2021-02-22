import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # configuring our database uri
    # note an error here
    #app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@{server}/testdb".format(username, password, server)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
