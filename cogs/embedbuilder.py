import discord
import configparser
import datetime
from jsonloader import *

class EmbedBuilder():
	def __init__(self):
		self.data = getfilecontent()
		self.embed = None
		
	def default_embed(self, guild, author, title, description, color=None, set_footer=True, set_author=False):
		self.create_embed(guild, title, description, color)

		if set_footer: self.set_footer(author=author)
		if set_author: self.set_author(author=author, url="", icon_url=author.avatar.url)

	def create_embed(self, guild, title, description, color=None):
		if not description or title:
			if not color: color = self.data[1][str(guild.id)]["color"]
			self.embed = discord.Embed(title=title, description=description,timestamp=datetime.datetime.utcnow(), color=eval(str(color)))
		else:
			raise NoneType()
		
	def add_field(self, name, value):
		self.embed.add_field(name=name, value=value, inline=True)
   
	def set_footer(self, text, icon, author=None):
		if author == None: self.embed.set_footer(text=text, icon_url=icon)
		else: self.embed.set_footer(text=f"Executed by {author.name}", icon_url=author.avatar_url)
	
	def set_author(self, author, url, icon_url):
		self.embed.set_author(name=author, url=url, icon_url=icon_url)
  
	def set_thumbnail(self, url):
		self.embed.set_thumbnail(url=url)
	
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