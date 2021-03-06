import discord
from discord.ext import commands


class Dev(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot

	@commands.command(brief="Unloads a cog", help=" <cog>")
	async def unload(self, ctx, cog):
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			await ctx.message.add_reaction("🚫")
			print(e)
		else:
			await ctx.message.add_reaction("✅")
			print(f"Unloaded {cog}")

	@commands.command(brief="Loads a cog", help=" <cog>")
	async def load(self, ctx, cog):
		try:
			self.bot.load_extension({extension})
		except Exception as e:
			await ctx.message.add_reaction("🚫")
			print(e)
		else:
			await ctx.message.add_reaction("✅")
			print(f"Loaded {extension}")

	@commands.command(brief="Reoads a cog", help=" <cog>")
	async def reload(self, ctx, cog):
		try:
			self.bot.reload_extension(f"extensions.{extension}")
		except Exception as e:
			await ctx.message.add_reaction("🚫")
			print(e)
		else:
			await ctx.message.add_reaction("✅")
			print(f"Reloaded {extension}")

	@commands.command(brief="Leaves the guild")
	async def leave(self, ctx):
		await ctx.guild.leave()

	@commands.command(aliases=["exe", "exec"], brief="Evaluates the given code and executes it.")
	async def execute(self, ctx, *, args):
		try:
			exec(self.convert_codeblock(args))
			await ctx.send("Code ran successfully!")
		except Exception as exc:
			await ctx.send(f"Something in your code is not working properly: {exc}")

	def convert_codeblock(self, cb):
		ncb = cb.replace("```", "").replace("py", "", 1)
		print(ncb)
		return ncb

	@commands.command(aliases=["off", "kill", "sts", "sleep"], brief="Closes the bot")
	async def shutdown(self, ctx):
		print(f"Bot shutdown by {ctx.message.author}.")
		await ctx.send("Going to sleep... :zzz:")
		await self.bot.close()