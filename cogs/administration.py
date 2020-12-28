import discord
from discord.ext import commands
from datetime import datetime

from hasperm import *


class Administration(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
	
	