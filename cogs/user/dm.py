import discord
from discord.ext import commands
from helper.embedbuilder import *
from discord.ext.commands.cooldowns import BucketType

class DMWorker(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config

	@commands.cooldown(1, 120, BucketType.member) 
	@commands.command()
	async def dm(self, ctx, target : discord.Member, *, msg):
		channel = await target.create_dm()

		eb = EmbedBuilder()
		eb.default_embed(guild=ctx.guild, author=ctx.author, title=f"From {ctx.author.name}:", description=msg, set_footer=False)
		eb.set_footer(text=f"Sent by {ctx.author.name}", icon=ctx.author.avatar_url)
		await channel.send(embed=eb.get_embed())