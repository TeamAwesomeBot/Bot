import discord
from discord.ext import commands
from random import choice
from jsonloader import *

class WelcomeMessage(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.data = getfilecontent() 

	@commands.Cog.listener()
	async def on_member_join(self, member):
		await client.get_channel(idchannel).send(choice(data[member.guild.id]["welcome_messages"]))

	@commands.command()
	async def on_member_remove(self, member):
		await self.get_channel(idchannel).send(choice(data[member.guild.id]["leave_messages"]))