import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_POOL_SIZE = 20  # 数据库连接池的大小。默认是引擎默认值（通常 是 5 ），此处最重要。
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_POOL_TIMEOUT = 100
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = False

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'S^soWaGiGl)*r#'

    # File upload Path
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'static', 'upload')

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    REDIS_URL = os.environ.get('REDIS_CACHE_URL')
    DEBUG = False


class DevelopmentConfig(Config):
    """Statement for enabling the development environment"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/flask_web?charset=utf8mb4'
    REDIS_URL = f"redis://:@127.0.0.1:6379/0"
    SQLALCHEMY_ECHO = True
    DEBUG = True


class APIConfig(Config):
    """Statement for enabling the api environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/flask_web'
    REDIS_URL = f"redis://:@127.0.0.1:6379/0"
    WTF_CSRF_ENABLED = False


class UATConfig(ProductionConfig):
    """Statement for enabling the UAT environment"""
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/flask_web'
    REDIS_URL = f"redis://:@127.0.0.1:6379/0"
    SQLALCHEMY_ECHO = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/flask_web?charset=utf8mb4'
    REDIS_URL = f"redis://:@127.0.0.1:6379/0"

    SQLALCHEMY_ECHO = True
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'api': APIConfig,
    'uat': UATConfig,
}

