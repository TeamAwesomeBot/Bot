import discord
from discord.ext import commands
from helper.embedbuilder import *

class DMWorker(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config

	@commands.command()
	async def dm(self, ctx, target : discord.Member, *, msg):
		channel = await target.create_dm()

		embedbuilder = EmbedBuilder()

		await channel.send(msg)