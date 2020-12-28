import discord

def get_emoji_by_name(guild:discord.Guild=None, emoji_name:str=None):
	if emoji_name == None:
		raise TypeError("string")
		return
	elif guild == None:
		raise TypeError("discord.Guild")
	
	for emoji in guild.emojis:
		if emoji.name == emoji_name:
			print("Found")
			return emoji

class TypeError(Exception):
	def __init__(self, arg, ms):
		super().__init__(msg=f'The given object has to be a {arg}!')