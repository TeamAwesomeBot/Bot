import discord
from discord.ext import commands
from helper.embedbuilder import *
from helper.handystuff import *

from helper.jsonloader import *

class ErrorHandler(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.data = getfilecontent()

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		eb = EmbedBuilder()

		if hasattr(ctx.command, "on_error"):
			ctx.command = command
			return
		
		if ctx.command.help:
			ctx.command.help = ""

		error = getattr(error, "original", error)

		if isinstance(error, commands.MissingRequiredArgument):
			eb.default_embed(guild=ctx.guild, author=ctx.message.author, title="Missing argument", description=f"Use {self.data[1][str(ctx.guild.id)]['prefix']}{ctx.command} {ctx.command.help}")
			await ctx.send(embed=eb.get_embed())
			
		else:
			eb.error_embed(error="An error occurred. The devs have already been notified about this issue. _Try again later._")
			await ctx.send(embed=eb.get_embed())

			for dev_id in dev_ids:
				eb.error_embed(error="An error occurred.")
				eb.add_field(name="Traceback", value=str(error))

				member = self.bot.get_user(dev_id)
				dmc = await member.create_dm()
				await dmc.send(embed=eb.get_embed())
