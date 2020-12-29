import discord
from discord.ext import commands

# -------------- API --------------
from cogs.api.reddit import *
from cogs.api.covid import *
# ------------- ADMIN -------------
from cogs.admin.settings import *
from cogs.admin.welcome_message import *
# ---------- MODERATION -----------
from cogs.mod.moderation import *
from cogs.mod.warn import *
# ------------- USER --------------
from cogs.user.dm import *
from cogs.user.info import *
# ------------ OTHER --------------
from cogs.other.cprofile import *
# ------------- DEV ---------------
from cogs.dev.dev import *
from cogs.dev.error_handler import *

class CogManager(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.cogs = [
			RedditAPI,
			CovidAPI,
			Settings,
			WelcomeMessage,
			Moderation,
			Warn,
			DMWorker,
			Info,
			CProfile,
			Dev,
			ErrorHandler
		]
		self.load_systems()

	def load_systems(self):
		for cog in self.cogs:
			try:
				self.bot.add_cog(cog(self.bot, self.config))
			except Exception:
				print(f"Something went wrong trying to activate {cog.name}")