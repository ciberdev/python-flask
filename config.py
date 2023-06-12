class Config():
    username= 'tester'
    password= 'tester2023#'
    server='localhost'
    database='tutorial'

    ENV = "Production"
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyProductionKey'
    SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{username}:{password}@{server}/{database}"
    
class DevConfig():
    username= 'tester'
    password= 'tester2023#'
    server='localhost'
    database='tutorial'

    ENV = "Development"
    DEBUG = True
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyDevelopmentKey'
    SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{username}:{password}@{server}/{database}"
    
class TestConfig():
    ENV = "Testing"
    DEBUG = True
    TESTING = True
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyTestingKey'
