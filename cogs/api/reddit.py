import discord
import praw
import requests
from discord.ext import commands, tasks

from helper.jsonloader import *
from helper.configmanager import *
from helper.embedbuilder import *

config = getconfig()
reddit_config = config["REDDIT_API"]

reddit = praw.Reddit(
    client_id=reddit_config["client_id"],
    client_secret=reddit_config["client_secret"],
    user_agent=reddit_config["user_agent"]
    )

class RedditAPI(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.rawconfig = config
		self.color = eval(self.rawconfig.get("BOT", "color"))

	@commands.group(brief="Sends a random subreddit picture.", help="<subreddit>")
	async def reddit(self, ctx):
		pass
		
	@reddit.command()
	async def pic(self, ctx, subreddit):
		eb = EmbedBuilder()

		index = 0
		while True:
				index += 1
				if index > 9:
					eb.default_embed(guild=ctx.guild, author=ctx.message.author, title="Error", description="Couldn't find an image on this subreddit.")
					await ctx.send(embed=eb.get_embed())
					break

				post = reddit.subreddit(subreddit).random()
				
				if "i.redd.it" in post.url:
					eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=post.title)
					eb.set_image(url=post.url)
					await ctx.send(embed=eb.get_embed())
					break

	@reddit.command(aliases=["subfeed"], brief="Add a subreddit feed to the channel you are in", help="<subreddit>")
	async def subredditfeed(self, ctx, subreddit):
		eb = EmbedBuilder()
		eb.default_embed(guild=ctx.guild, author=ctx.message.author, title=f"Added new subreddit feed to {ctx.channel.mention}", description=f"All posts from r/{subreddit} will be sent in this channel.")

		jsondata = {"subreddit" : str(subreddit), "channel" : str(ctx.channel.id)}
		self.data[str(ctx.guild.id)]["reddit"].append()

	@tasks.loop(minutes=10)
	async def update_feed(self):
		subreddit = reddit.subreddit(subreddit)
		for submission in subreddit.hot(limit=1): # if not image: 
			eb = EmbedBuilder()
			eb.default_embed(guild=guild, author="", title=f"Added new subreddit feed to {ctx.channel.mention}", description=f"All posts from r/{subreddit} will be sent in this channel.")

			print(submission.title)
			print(submission.score)
			print(submission.id)
			print(submission.url)