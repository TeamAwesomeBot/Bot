import discord
from discord.ext import commands
import json
from jsonloader import *
from hasperm import *
import configparser

class Moderation(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.config = config["MODERATION"]
		self.json = getfilecontent()
		self.color = self.rawconfig.get("BOT", "color")

	@commands.command(aliases=["warnmember"], brief="", help="<target> <reason>")
	async def warn(self, ctx, target: discord.Member, *, reason=""):
		if await has_admin(ctx.message.author, ctx):
			print(self.json)

	@commands.command(aliases=[], brief="", help="<member> <reason>")
	async def kick(self, ctx, member: discord.Member, *, reason):
		if await has_admin(ctx.message.author, ctx):
			embed = discord.Embed(
				description=f"{member.name} has been kicked for {reason}",
				color = eval(self.color))
			embed.set_footer(
				text=f"Issued by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)

			dm_embed = discord.Embed(description=f"You have been kicked from `{ctx.guild.name}`")
			
			if not reason:
				dm_embed.add_field(name="Reason", value=reason)

			dm = await member.create_dm()
			await dm.send(embed=embed)

			print(f"{member.name} has been kicked for \"{reason}\".")			
			await member.kick(reason=reason)
			await ctx.send(embed=embed)
			
	
	@commands.command(aliases=[], brief="", help="<member> <reason>")
	async def ban(self, ctx, member: discord.Member, *, reason):
		if await has_admin(ctx.message.author, ctx):
			embed = discord.Embed(
				description=f"{member.name} has been banned for {reason}",
				color = eval(self.color))
			embed.set_footer(
				text=f"Issued by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)

			dm_embed = discord.Embed(description=f"You have been banned from `{ctx.guild.name}`")
			
			if not reason:
				dm_embed.add_field(name="Reason", value=reason)

			dm = await member.create_dm()
			await dm.send(embed=embed)

			print(f"{member.name} has been banned for \"{reason}\".")			
			await member.ban(reason=reason)
			await ctx.send(embed=embed)

	@commands.command(aliases=[], brief="", help="<member> <reason>")
	async def ban(self, ctx, member: discord.Member):
		if await has_admin(ctx.message.author, ctx):
			embed = discord.Embed(
				description=f"{member.name} has been unbanned.",
				color = eval(self.color))
			embed.set_footer(
				text=f"Issued by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)

			dm_embed = discord.Embed(description=f"You have been unbanned from `{ctx.guild.name}`")
			dm = await member.create_dm()
			await dm.send(embed=embed)

			print(f"{member.name} has been unbanned.")			
			await member.unban()
			await ctx.send(embed=embed)