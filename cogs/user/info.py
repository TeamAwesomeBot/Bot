import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from helper.embedbuilder import *

class Info(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot

	@commands.command(name="whois",aliases=["info"],description="Get info about a user",usage="<member>")
	async def whois(self, ctx, member: discord.Member=None):
		eb = EmbedBuilder()
		
		if not member:
			member = ctx.message.author

		roles = [role for role in member.roles[1:]]
		
		eb.default_embed(guild=ctx.guild, title=f"Who is {member.name}?", description="Here are the answers!")
		eb.set_thumbnail(url=member.avatar_url)
		
		if member.name != member.display_name: eb.add_field(name="Nickname", value=member.display_name)
		eb.add_field(name="Account created", value=member.created_at.strftime("%Y-%m-%d, %H:%M:%S"))
		eb.add_field(name="Joined this server", value=member.joined_at.strftime("%m/%d/%Y - %H:%M:%S"))
		eb.add_field(name="Roles:", value=", ".join([role.mention for role in roles]))
		eb.add_field(name="ID:", value=member.id)
		await ctx.send(embed=eb.get_embed())