import discord
from discord.ext import commands

from jsonloader import *


class CProfile(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.data = getfilecontent()

	@commands.command()
	async def manualoverride(self, ctx):
		if ctx.message.author.id == 414585685895282701:
			print(f"Mannually creating a json profile for {ctx.guild.name}")
			await ctx.send(f"Mannually creating a json profile for {ctx.guild.name}")

			jsondata = {"prefix" : "!", "color" : "0x17c4b9", "use_wm" : False, "use_lm" : False, "welcome_messages" : [],"leave_messages" : [], "welcome_channel" : "", "warns" : []}

			self.data[1][str(ctx.guild.id)] = jsondata

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		print(f"Hello {guild.name}")
		jsondata = {"prefix" : "!", "color" : "0x17c4b9", "use_wm" : False, "use_lm" : False, "welcome_messages" : [],"leave_messages" : [], "warns" : []}

		self.data[1][str(guild.id)] = jsondata

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		print(f"Bye {guild.name}")
		dict_ = self.data[1]
		del dict_[str(guild.id)]
