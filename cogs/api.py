import discord
import requests
import json
import configparser
from discord.ext import commands

class Api(commands.Cog):
	def __init__(self, bot, config):
		self.bot = bot
		self.color = config.get("BOT", "color")
	
	@commands.command(aliases=["covid-19", "corona"], brief="Gives you the covid-19 statistics.", help="<country>")
	async def covid(self, ctx, *, country = None):
			url = "https://api.covid19api.com/summary"

			response = requests.get(url)
			response = response.json()

			if country is None:
					embed = discord.Embed(
							title="Global covid-19 statistics",
							color=eval(self.color),
							timestamp=ctx.message.created_at
							)
					embed.add_field(name="Total confirmed cases:", value=response["Global"]["TotalConfirmed"])
					embed.add_field(name="Total deaths:", value=response["Global"]["TotalDeaths"])
					embed.add_field(name="Total recovered:", value=response["Global"]["TotalRecovered"])
					embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.message.author.avatar_url)
					await ctx.send(embed=embed)
			else:
					embed = discord.Embed(
							title=f"Covid-19 statistics for {country}",
							color=self.bot.color,
							timestamp=ctx.message.created_at
							)
					for dictionary in response["Countries"]:
							if dictionary["Country"] == country or dictionary["CountryCode"] == country or dictionary["Slug"] == country:
									embed.add_field(name="Total confirmed cases:", value=dictionary["NewConfirmed"])
									embed.add_field(name="Total deaths:", value=dictionary["TotalDeaths"])
									embed.add_field(name="Total recovered:", value=dictionary["TotalRecovered"])
									embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.message.author.avatar_url)
									await ctx.send(embed=embed)