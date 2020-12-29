import discord
import asyncio
import json
import configparser
from discord.ext import commands

from helper.jsonloader import *
from helper.hasperm import *
from helper.embedbuilder import *


class Moderation(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.config = config["MODERATION"]
		self.json = getfilecontent()
		self.color = self.rawconfig.get("BOT", "color")

	@commands.command(brief="Kicks a member.", help="<member> [reason]")
	async def kick(self, ctx, member: discord.Member, *, reason=""):
		if await has_admin(ctx.message.author, ctx):
			if reason == None: reason = "No reason specified."
			if not member.bot:
				eb = EmbedBuilder()
				
				eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=f"You have been kicked from {ctx.guild.name}")
				eb.add_field(name="Reason:", value=reason)

				dm = await member.create_dm()
				await dm.send(embed=eb.get_embed)
				eb = None

			eb = EmbedBuilder()
			
			eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=f"{ctx.message.author.name} kicked {member.name}.", description=f"Reason: {reason}")
						
			await member.kick(reason=reason)
			await ctx.send(embed=eb.get_embed())
	
	@commands.command(brief="Bans a member.", help="<member> <reason>")
	async def ban(self, ctx, member: discord.Member, *, reason=""):
		if await has_admin(ctx.message.author, ctx):
			if reason == None: reason = "No reason specified."
			if not member.bot:
				eb = EmbedBuilder()
				
				eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=f"You have been banned from {ctx.guild.name}")
				eb.add_field(name="Reason:", value=reason)

				dm = await member.create_dm()
				await dm.send(embed=eb.get_embed)
				eb = None

			eb = EmbedBuilder()
			
			eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=f"{ctx.message.author.name} banned {member.name}.", description=f"Reason: {reason}")
			try:
				await ctx.guild.ban(member, reason)
				await ctx.send(embed=eb.get_embed())
			except Forbidden or HTTPException:
				print("An unexpected error ocurred trying to ban a member.")

	
	@commands.command(aliases=["clear"], brief="Deletes the provided amount of messages.", help="<amount>")
	async def wipe(self, ctx, amount: int):
		if amount < 1001:
			eb = EmbedBuilder()

			eb.default_embed(guild=ctx.guild, author=ctx.message.author, description=f"Cleared {amount} messages!")
			
			await ctx.send(embed=eb.get_embed())
			await asyncio.sleep(2)
			await ctx.channel.purge(limit=amount+2)
			
		else:
			await ctx.send("I can't clear that much!")
