import json
import atexit
import discord
from configmanager import config

filenames = ['data.json', 'config.json']
data = [{}, {}]

def readfile():
	global filenames, data
	
	for i, filename in enumerate(filenames):
		with open(str(filename), "r") as read_file:
			data[i] = json.load(read_file)

def getfilecontent():
    global data
    return data

def checkuser(member:discord.Member=None, ctx=None):
    global data

    if not member == None or not ctx == None:
        if not str(member.id) in data:
            jsondata = {'balance' : int(config['ECONOMY']['startbalance']), 'warns' : 0}
            data[ctx.guild.id][str(member.id)] = jsondata
            print(f'User {member.name} was registered successfully.')
    else:
        raise TargetError()

def savefile():
	global filenames, data

	for i, filename in enumerate(filenames):
		with open(str(filename), "w") as write_file:
			json.dump(data[i], write_file)

atexit.register(savefile)
readfile()

class TargetError(Exception):
    def __init__(self, msg='The given member can\'t be null!'):
        super().__init__(msg)

class MatchingMember(Exception):
    def __init__(self, msg='The given member already exist!'):
        super().__init__(msg)