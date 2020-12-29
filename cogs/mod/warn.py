import discord
import hasperm
import datetime
from discord.ext import commands
from cogs.embedbuilder import *
from jsonloader import *

class Warn(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.data = getfilecontent()

	@commands.command()
	async def warn(self, ctx, target: discord.Member, *, reason=""):
		if await has_admin(ctx.message.author, ctx):
			jsondata = {'date' : int(config['ECONOMY']['startbalance']), 'warns' : 0}
			self.json[str(ctx.guild.id)]["warns"][str(target.id)]["date"]
			print(lst)

	@commands.group(aliases=["warnmember"], brief="Warns a member.", help="<add/remove> <member> [reason]", invoke_without_command = True)
	async def warn(self, ctx):
		print("Hello.")

	@warn.command()
	async def add(self, ctx, target : discord.Member, *, reason):
		if await has_admin(ctx.message.author, ctx):
			jsondata = {"date" : datetime.datetime.utcnow(), "reason" : reason, "moderator" : str(ctx.message.author.id)}

			self.data[0][str(ctx.guild.id)]["warns"][str(target.id)].append(jsondata)

	@warn.command()
	async def remove(self, ctx, index):
		if await has_admin(ctx.message.author, ctx):
				self.data[0][str(ctx.guild.id)]["warns"][str(target.id)].pop(index)

	@warn.command()
	async def list(self, ctx, target):
		if await has_admin(ctx.message.author, ctx):
			out = self.data[str(ctx.guild.id)]["warns"][str(target.id)]
			eb = EmbedBuilder()
			eb.default_embed(guild=ctx.guild, author=ctx.message.author,title=f"Warnings for user {target.name}", description=" ")

			#for warning in self.data[0][str(ctx.guild.id)]["warns"][str(target.id)]

			eb.add_field(name="", value="")