class Config():
    ENV = "Production"
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyProductionKey'
    
class DevConfig():
    ENV = "Development"
    DEBUG = True
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyDevelopmentKey'
    
class TestConfig():
    ENV = "Testing"
    DEBUG = True
    TESTING = True
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'MyTestingKey'
