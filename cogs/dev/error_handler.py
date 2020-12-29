import discord
from discord.ext import commands
from helper.embedbuilder import *
from helper.handystuff import *

class ErrorHandler(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config

	@commands.Cog.listener
	async def on_command_error(ctx, error: Any):
		eb = EmbedBuilder()
		
		eb.error_embed(error="An error occurred. The devs have already been notified about this issue. _Try again later._")
		await ctx.send(embed=eb.get_embed())
		for dev_id in dev_ids:

			eb.error_embed(error="An error occurred.")
			eb.add_field(name="Taceback" value=str(error))

			member = self.bot.get_user(dev_id)
			dmc = await member.create_dm()
			await dmc.send(embed=eb.get_embed())
