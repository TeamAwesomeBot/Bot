import discord
from discord.ext import commands

from cogs.moderation import *
from cogs.administration import *
from cogs.api import *

class CogManager(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        self.cogs = [Moderation, Administration, Api]
        self.load_systems()

    def load_systems(self):
        for cog in self.cogs:
            self.bot.add_cog(cog(self.bot, self.config))