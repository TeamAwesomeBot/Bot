#!/usr/bin/python -u
import discord
import datetime
from cogs.embedbuilder import *

from cogmanager import *
from configmanager import *
from webserver.app import *
from jsonloader import *

config = getconfig()
bot_config = config['BOT']

intents = discord.Intents(messages=True, guilds=True, members=True, reactions=True, dm_messages=True)

bot = commands.Bot(
	command_prefix=bot_config['prefix'], description=bot_config['description'], help_command=None,
	intents=intents
	)

@bot.event 
async def on_ready():
	print('Initializing Cogs...')
	bot.add_cog(CogManager(bot, config))

	status =f'{bot.command_prefix}help'
	await bot.change_presence(activity=discord.Game(name=bot_config['activity']))
	print("Started successfully!\n")
	

@bot.command(name="help", brief="Shows a list of all commands.", help='<command>')
async def help(ctx, arg=None):
	data = getfilecontent()
	prefix = data[1][str(ctx.guild.id)]["prefix"]
	embedBuilder = EmbedBuilder()
	if not arg:
		embedBuilder.create_embed(ctx.guild, title=":gear: Help",description=bot.description)

		for command in bot.commands:
			if not command.brief: command.brief = "This command has no description"
			if not command.help: command.help = ""

			embedBuilder.add_field(name=f"{prefix}{command} {command.help}", value=command.brief)
		
		await ctx.send(embed=embedBuilder.get_embed())
	else:
		for command in bot.commands:
			if arg in str(command) or arg in str(command.aliases):
				if not command.brief: command.brief = "This command has no description"
				if not command.help: command.help = ""

				aliases = ""
				dalsynt = ", "
				if len(command.aliases) > 0: dalsynt = ""
				if len(command.aliases) != 0:
					for alias in command.aliases:
						aliases += f"{prefix}{alias}{dalsynt}"
				else:
					aliases = "There are no aliases for this command."

				embedBuilder.create_embed(ctx.guild, title=f":gear: Help \"{command}\"", description=command.brief)
				embedBuilder.add_field(name="Usage", value=f"{prefix}{command} {command.help}")
				embedBuilder.add_field(name="Aliases", value=f"{aliases}")

				await ctx.send(embed=embedBuilder.get_embed())
		
try:
  print('Starting systems...')
  bot.run(bot_config['token'])
  print('Done!')
except Exception as e:
  print(f'end: {e}')