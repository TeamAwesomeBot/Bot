import discord
from discord.ext import commands
from helper.jsonloader import *

class Settings(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.config = config
		self.data = getfilecontent()

	@commands.group(brief="Changes bot settings for this server.", help="<prefix/activate/deactivate> [welcome_msgs]", invoke_without_command = True)
	async def settings(self, ctx):
		await ctx.send("Hello")

	@settings.command()
	async def prefix(self, ctx):
		await ctx.send("Hello world")

	@settings.group()
	async def activate(self, ctx):
		print("hello")

	@settings.group()
	async def deactivate(self, ctx):
		pass

	@activate.command()
	async def welcome_msgs(self, ctx):
		self.data[1][str(ctx.guild.id)]["use_wm"] = True
		await ctx.send()

''' 	@commands.command(brief="Change the bot settings.", help='<prefix/username/activity> <argument>')
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
				await ctx.send(embed=embed) '''