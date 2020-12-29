import discord
from discord.ext import commands

from cogs.moderation import *
from cogs.administration import *
from cogs.api import *
from cogs.cprofile import *
from cogs.welcome_message import *
from cogs.settings import *
from cogs.warn import *
from cogs.dm_worker import *
from cogs.info import *
from cogs.reddit import *


class CogManager(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.cogs = [
			Moderation, 
			Administration, 
			Api, 
			CProfile, 
			WelcomeMessage, 
			Settings, 
			Warn , 
			DMWorker,
			Info,
			Reddit
			]
		self.load_systems()

	def load_systems(self):
		for cog in self.cogs:
			try:
				self.bot.add_cog(cog(self.bot, self.config))
			except Exception:
				print(f"Something went wrong trying to activate {cog.name}")