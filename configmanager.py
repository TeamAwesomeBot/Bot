from configparser import SafeConfigParser
import inspect
import atexit

config = SafeConfigParser()
config.read('config.ini')

def getconfig():
	global config
	frame = inspect.stack()[1]
	module = inspect.getmodule(frame[0])
	
	print(f"{module.__name__} Requested config.")
	
	return config

def saveconfig():
    global config
    with open('config.ini', 'w') as configfile:    # save
        print('Saving changes before exiting the program...')
        try:
            config.write(configfile)
            print('Success!')
        except Exception as e:
            print('An unexpected error occurred when trying to save the config. {}'.format(e))

atexit.register(saveconfig)