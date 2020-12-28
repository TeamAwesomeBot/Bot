import discord
import asyncio
import random
from discord.ext import commands

from hasperm import has_admin
from cogs.handystuff import *
from cogs.embedbuilder import *
from jsonloader import *

class WelcomeMessage(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.data = getfilecontent() 
		self.color = self.rawconfig.get("BOT", "color")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		if self.data[1][str(member.guild.id)]["use_wm"]:
			channel = member.guild.get_channel(int(self.data[1][str(member.guild.id)]["welcome_channel"]))

			choice = random.choice(self.data[1][str(member.guild.id)]["welcome_messages"])
			choice.replace("{user}", member.mention)
			_str = choice.split("|", 1)

			embedbuilder = EmbedBuilder()
			embedbuilder.create_embed(guild=member.guild,title=_str[0], description=_str[1])
			
			await channel.send(embed=embedbuilder.get_embed())

	''' @commands.Cog.listener()
	async def on_member_remove(self, member):
		if self.data[member.guild.id]["use_lm"]:
			channel = discord.utils.get_channel(int(self.data[member.guild.id]["leave_messages"]))
			
			choice = random.choice(self.data[member.guild.id]["leave_messages"])
			
			embed = discord.Embed(title="Bye!", description=choice, timestamp=datetime.datetime.utcnow(), color=eval(self.data[member.guild.id]["color"]))

			await channel.send(embed=embed) '''

	@commands.command(aliases=["wm"], brief="Change the welcome-messages.\nNOTE: If you want to activate them use the settings command", help="")
	async def welcomemessage(self, ctx):
		if await has_admin(ctx.message.author, ctx):
			
			emojis = ["✅", get_emoji_by_name(ctx.guild, "crossmark")]

			embedbuilder = EmbedBuilder()
			embedbuilder.create_embed(ctx.guild, title="Change welcome-messages", description=f"Please react with {emojis[1]} in order to add a welcome message or with {emojis[0]} in order to remove a welcome message.")

			msg = await ctx.send(embed=embedbuilder.get_embed())

			for i, emoji in enumerate(emojis):
				await msg.add_reaction(emojis[i])

			def check(reaction, user):
					return user == ctx.message.author and str(reaction.emoji) in emojis

			try:
					reaction, user = await self.bot.wait_for("reaction_add", timeout=20.0, check=check)
			except asyncio.TimeoutError:
					await ctx.send("Taking too long there buddy.")
			else:
				if reaction.emoji == emojis[0]:
					embedbuilder.create_embed(ctx.guild, title="Add a welcome message", description="Example: `Welcome|Hello {user}!` in this case the bot will say `Welcome` as the embed title and `Hello (name of user that joined)` as the embed description.")

					msg = await ctx.send(embed=embedbuilder.get_embed())

					def check(m):
						return m.channel == ctx.message.channel and m.author == ctx.message.author and "|" in m.content

					try:
						msg = await self.bot.wait_for('message', check=check)
					except asyncio.TimeoutError:
						await ctx.send("Taking too long there buddy.")
					else:
						self.data[1][str(ctx.guild.id)]["welcome_messages"].append(msg.content)
						await ctx.send("Added a new welcome message!")
						
				if reaction.emoji == emojis[1]:
					embed = embedbuilder.create_embed(ctx.guild, title="Delete a welcome message", description="Please react with one of the numbers to delete a welcome message.")
					
					msg = await ctx.send(embed=embedbuilder.get_embed())

					emojis = [
						"1️⃣", "2️⃣", "3️⃣",
						"4️⃣", "5️⃣", "6️⃣",
						"7️⃣", "8️⃣", "9️⃣"
						]

					for i, emoji in enumerate(emojis):
						await msg.add_reaction(emojis[i])

					def check(reaction, user):
						return user == ctx.message.author and str(reaction.emoji) in emojis

					try:
							reaction, user = await self.bot.wait_for("reaction_add", timeout=20.0, check=check)
					except asyncio.TimeoutError:
							await ctx.send("Taking too long there buddy.")
					else:
						messages = self.data[member.guild.id]["welcome_messages"]
						messages = dict(enumerate(results, start=1))

						demojis = {
							"1️⃣":1, "2️⃣":2, "3️⃣":3,
							"4️⃣":4, "5️⃣":5, "6️⃣":6,
							"7️⃣":7, "8️⃣":8, "9️⃣":9
							}
							

				