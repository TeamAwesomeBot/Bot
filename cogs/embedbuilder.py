import discord
import configparser
import datetime
from jsonloader import *

class EmbedBuilder():
	def __init__(self):
		self.data = getfilecontent()
		self.embed = None
		
	def create_embed(self, guild, title, description, color=None):
		if not description or title:
			if not color: color = self.data[1][str(guild.id)]["color"]
			self.embed = discord.Embed(title=title, description=description,timestamp=datetime.datetime.utcnow(), color=eval(str(color)))
		else:
			raise NoneType()
		
	def add_field(self, name, value):
		self.embed.add_field(name=name, value=value)
   
	def footer(self, name, value, icon):
   	    self.embed.set_footer(name=name, value=value, icon_url=icon)
   
	def get_embed(self):
   	    if self.embed != None:
   	        return self.embed
   	        self.embed = None
   	    else:
   	    	raise EmptyEmbed()
   	    	
  
class NoneType(Exception):
	def __init__(self, msg="The given argument was None."):
		super().__init__(msg)


class EmptyEmbed(Exception):
	def __init__(self, msg='There is no embed to give!'):
		super().__init__(msg)