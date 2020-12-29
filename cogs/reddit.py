import discord
import praw
from discord.ext import commands

from jsonloader import *
from configmanager import *

config = getconfig()
bot_config = config["BOT"]
reddit_config = config["REDDIT_BOT"]

reddit = praw.Reddit(
    client_id=reddit_config["client_id"],
    client_secret=reddit_config["client_secret"],
    user_agent=reddit_config["user_agent"]
    )

class Reddit(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.color = eval(self.rawconfig.get("BOT", "color"))

	@commands.group(brief="Sends a random subreddit picture.", help="<subreddit>")
	async def reddit(self, ctx):
		await ctx.send("Reddit API go brrr")
		
	@reddit.command()
	async def pic(self, ctx, subreddit):
		index = 0
		while True:
				index += 1
				if index > 9:
						embed = discord.Embed(
								description="Couldn't find an image on this subreddit",
								color=self.color
								)
						await ctx.send(embed=embed)
						break

				post = reddit.subreddit(subreddit).random()
				if "i.redd.it" in post.url:
						embed = discord.Embed(
								description=post.title,
								color=self.color,
								timestamp=ctx.message.created_at
								)
						embed.set_image(url=post.url)
						embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.message.author.avatar_url)
						await ctx.send(embed=embed)
						break