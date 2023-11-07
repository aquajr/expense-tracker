import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Define app configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'

<<<<<<< HEAD
    # Database migration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
    # Data configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.dib')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 6336f05e94c025f568b88c28e2d8c75b446acfcd
