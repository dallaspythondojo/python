class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = 'someSecretKey'

class DevelopmentConfig(Config):
	DEBUG = True

class StagingConfig(Config):
	TESTING = True

class ProductionConfig(Config):
	pass
