from configparser import ConfigParser

config = ConfigParser()
config.read('healthtracker.cfg')
DBPATH = config.get('database', 'dbpath')