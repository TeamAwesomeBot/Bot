import discord
import asyncio
import json
import configparser
from discord.ext import commands

from jsonloader import *
from hasperm import *


class Moderation(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.config = config["MODERATION"]
		self.json = getfilecontent()
		self.color = self.rawconfig.get("BOT", "color")

	@commands.command(aliases=["warnmember"], brief="", help="<member> <reason>")
	async def warn(self, ctx, target: discord.Member, *, reason=""):
		if await has_admin(ctx.message.author, ctx):
			jsondata = {'date' : int(config['ECONOMY']['startbalance']), 'warns' : 0}
			self.json[str(ctx.guild.id)]["warns"][str(target.id)]["date"]
			print(lst)

	@commands.command(brief="", help="<member>")
	async def warns(self, ctx, member: discord.Member):
		embed = discord.Embed(
			description=f"{member.name}'s warnings:",
			color=eval(self.color), 
			timestamp=ctx.message.created_at
			)
		embed.set_footer(
			text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
			)
	
	@commands.command(brief="", help="<member> <reason>")
	async def kick(self, ctx, member: discord.Member, *, reason):
		if await has_admin(ctx.message.author, ctx):
			embed = discord.Embed(
				description=f"{member.name} has been kicked for {reason}",
				color=eval(self.color), 
				timestamp=ctx.message.created_at
				)
			embed.set_footer(
				text=f"Issued by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)

			dm_embed = discord.Embed(description=f"You have been kicked from `{ctx.guild.name}`")
			dm_embed.add_field(name="Reason:", value=reason)
			dm = await member.create_dm()
			await dm.send(embed=embed)

			print(f"{member.name} has been kicked for \"{reason}\".")			
			await member.kick(reason=reason)
			await ctx.send(embed=embed)
			
	
	@commands.command(brief="", help="<member> <reason>")
	async def ban(self, ctx, member: discord.Member, *, reason):
		if await has_admin(ctx.message.author, ctx):
			embed = discord.Embed(
				description=f"{member.name} has been banned for {reason}",
				color=eval(self.color),
				timestamp=ctx.message.created_at
				)
			embed.set_footer(
				text=f"Issued by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)

			dm_embed = discord.Embed(description=f"You have been banned from `{ctx.guild.name}`")
			dm_embed.add_field(name="Reason:", value=reason)
			dm = await member.create_dm()
			await dm.send(embed=embed)

			print(f"{member.name} has been banned for \"{reason}\".")			
			await member.ban(reason=reason)
			await ctx.send(embed=embed)
	
	@commands.command(aliases=["clear"], brief="Deletes the provided amount of messages", help="<amount>")
	async def wipe(self, ctx, amount: int):
		if amount < 1001:
			embed = discord.Embed(
				description=f"Cleared {amount} messages!",
				color=eval(self.color),
				timestamp=ctx.message.created_at
				)
			embed.set_footer(
				text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url
				)
			await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await ctx.channel.purge(limit=amount+2)
			
		else:
			await ctx.send("I can't clear that much!")

	@commands.command(brief="Change the bot settings.", help='<prefix/username/activity> <argument>')
	async def settings(self, ctx, mode='', arg=''):
		if await has_admin(ctx.message.author, ctx):
			if not mode == '' and not arg == '':
				if mode in self.settings_list:
					var_name = mode.lower()
					if mode == 'prefix':
						self.bot.command_prefix = arg
					elif mode == 'username':
						await ctx.guild.me.edit(nick=arg)
					elif mode == 'activity':
						await self.bot.change_presence(activity=discord.Game(name=arg))
						self.config['BOT']['activity'] = arg
				
				print(f'Changed variable \'{var_name}\' to \'{arg}\'.')

				embed = discord.Embed(title=f':gear: Settings', description=f'Changed variable \'{var_name}\' to \'{arg}\'.',
										timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
				await ctx.send(embed=embed)