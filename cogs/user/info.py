import discord
from discord.ext import commands


class Info(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot

	@commands.command(name="whois",aliases=["info"],description="Get info about a user",usage=" <member>")
	async def whois(self, ctx, member: discord.Member=None):
		if not member:
			member = ctx.message.author

		roles = [role for role in member.roles[1:]]

		embed = discord.Embed(
				color=member.color,
				timestamp=ctx.message.created_at,
				)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_author(name=member, url=f"https://discord.com/users/{member.id}", icon_url=member.avatar_url)
		if member.name != member.display_name:
				embed.add_field(
						name="Nickname:",
						value=member.display_name,
						inline=False
						)
		embed.add_field(
				name="Account created:",
				value=member.created_at.strftime("%Y-%m-%d, %H:%M:%S"),
				inline=False
				)
		embed.add_field(
				name="Joined this server:",
				value=member.joined_at.strftime("%Y-%m-%d, %H:%M:%S"),
				inline=False
				)
		embed.add_field(
				name="Roles:",
				value=", ".join([role.mention for role in roles]),
				inline=False
				)
		embed.add_field(
				name="ID:",
				value=member.id,
				inline=False
				)
		embed.set_footer(
				text=f"Requested by {ctx.author}",
				icon_url=ctx.message.author.avatar_url
				)
		await ctx.send(embed=embed)