import discord
from discord.ext import commands
from cogs.embedbuilder import *

class DMWorker(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config

	@commands.command()
	async def dm(self, ctx, target, *, msg):
		channel = target.create_dm()

		embedbuilder = EmbedBuilder

		await channel.send(msg)