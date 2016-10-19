import os

class DBConfig(object):
	DB_ON = True
	DB_DRIVER = 'mysql'
	DB_ORM = False


class DevelopmentDBConfig(DBConfig):
	DB_USERNAME = 'root'
	DB_PASSWORD = ''
	DB_DATABASE_NAME = 'loginreg'
	DB_HOST = 'localhost'
	DB_PORT = 3306

class StagingDBConfig(DBConfig):
	DB_USERNAME = 'root'
	DB_PASSWORD = ''
	DB_DATABASE_NAME = 'loginreg'
	DB_HOST = 'localhost'

class ProductionDBConfig(DBConfig):
	DB_USERNAME = 'root'
	DB_PASSWORD = ''
	DB_DATABASE_NAME = 'loginreg'
	DB_HOST = 'localhost'
