import discord
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
		if self.data[member.guild.id]["use_wm"]:
			channel = discord.utils.get_channel(int(self.data[member.guild.id]["welcome_channel"]))

			embedbuilder = EmbedBuilder()
			embedbuilder.create_embed(member.guild, "Title", "description")
			
			choice = random.choice(self.data[member.guild.id]["welcome_messages"])
			
			embed = discord.Embed(title="Welcome!", description=choice, timestamp=datetime.datetime.utcnow(), color=eval(self.data[member.guild.id]["color"]))

			await channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		if self.data[member.guild.id]["use_lm"]:
			channel = discord.utils.get_channel(int(self.data[member.guild.id]["leave_messages"]))
			
			choice = random.choice(self.data[member.guild.id]["leave_messages"])
			
			embed = discord.Embed(title="Bye!", description=choice, timestamp=datetime.datetime.utcnow(), color=eval(self.data[member.guild.id]["color"]))

			await channel.send(embed=embed)

	@commands.command(brief="Change the welcome-messages.\nNOTE: If you want to activate them use the settings command", help="")
	async def welcomemessage(self, ctx):
		if has_admin(ctx.message.author, ctx):
			embedbuilder.create_embed(ctx.guild, "", "description")

			emojis = [get_emoji_by_name(ctx.guild, "crossmark"), "✅"]
			msg = await ctx.send(embed=embed)

			for emoji in emojis:
				await msg.add_reaction(emoji)

				def check(reaction, user):
						return user == ctx.message.author and str(reaction.emoji) in emojis
				try:
						reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)
				except asyncio.TimeoutError:
						await ctx.send("Taking too long there buddy.")
				else:
					if reaction.emoji == emojis[0]:
						embed = discord.Embed(
							description="Please write the new welcome message you want to add.\n The format will be either <message> <member> or <member> <message> write \"message\" after your welcome message if you want the message to before the name of the member, and vice versa.",
							color=eval(self.color)
							)
					elif reaction.emoji == emojis[1]:
						embedbuilder.create_embed()
						def check(reaction, user):
							return user == ctx.message.author and message.endswith("message") or message.endswith("member")

						try:
								reaction, user = await self.bot.wait_for('message', timeout=20.0, check=check)
						except:
							pass
						else:
							pass

			messages = self.data[member.guild.id]["welcome_messages"]
			messages = dict(enumerate(results, start=1))

			msg = await ctx.send(embed=embed)

			emojis = [
					"1️⃣", "2️⃣", "3️⃣",
					"4️⃣", "5️⃣", "6️⃣",
					"7️⃣", "8️⃣", "9️⃣"
					]

			for emoji in emojis:
					await msg.add_reaction(emoji)

			demojis = {
					"1️⃣":1, "2️⃣":2, "3️⃣":3,
					"4️⃣":4, "5️⃣":5, "6️⃣":6,
					"7️⃣":7, "8️⃣":8, "9️⃣":9
					}

			def check(reaction, user):
					return user == ctx.message.author and str(reaction.emoji) in emojis

			try:
					reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)
			except asyncio.TimeoutError:
					await ctx.send("Taking too long there buddy.")
			else:
				pass