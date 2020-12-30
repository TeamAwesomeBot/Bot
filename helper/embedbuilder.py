import discord
import configparser
import datetime
from helper.jsonloader import *

class EmbedBuilder():
	def __init__(self):
		self.data = getfilecontent()
		self.embed = None
		
	def default_embed(self, guild=None, author=None, title="", description="", color=None, set_footer=True, set_author=False):
		self.create_embed(guild, title, description, color)

		if set_footer: self.set_footer(author=author)
		if set_author: self.set_author(author=author, url=f"https://discord.com/users/{author.id}", icon_url=author.avatar.url)
	
	def error_embed(self, error=None, color=None):
		if color == None: color = 0xe74c3c
		
		self.create_embed(title="Error", description=str(error), color=color)
		self.set_thumbnail(url="https://bit.ly/38Ms03p")

	def create_embed(self, guild=None, title="", description="", color=None):
		if not color: color = self.data[1][str(guild.id)]["color"]
		self.embed = discord.Embed(title=title, description=description,timestamp=datetime.datetime.utcnow(), color=eval(str(color)))
		
	def add_field(self, name, value):
		self.embed.add_field(name=name, value=value, inline=True)
   
	def set_footer(self, text="", icon=None, author=None):
		if author == None: self.embed.set_footer(text=text, icon_url=icon)
		else: self.embed.set_footer(text=f"Requested by {author.name}", icon_url=author.avatar_url)

	def set_image(self, url=""):
		if url != None: self.embed.set_image(url=url)
		else: self.embed.set_image(url="https://discordapp.com/assets/dd4dbc0016779df1378e7812eabaa04d.png")

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