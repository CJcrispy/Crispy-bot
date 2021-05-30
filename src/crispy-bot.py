import os
import subprocess
import webbrowser
from selenium import webdriver
from to_do_list import *
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix='!')

# Help
@bot.command()
async def commandsList(ctx):
    await ctx.send("""
    test
    A List of commands
    """)

# Quality of Life commands
@bot.command()
async def study(ctx, topic: str):
    addToStudyList(topic)
    await ctx.send("New study topic '%s' added!" % topic)

@bot.command()
async def idea(ctx, idea: str, description: str = None):
    addToProjectList(idea, description)
    await ctx.send("New project idea '%s' added!" % idea)

# Concourse CI commands
@bot.command()
async def concourseUp(ctx):
    url = "http://localhost:8082/"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    
    subprocess.call("docker-compose up -d", shell=True)
    sleep(15)
    webbrowser.get(chrome_path).open(url)

@bot.command()
async def concourseDown(ctx):
    subprocess.call("docker-compose down", shell=True)

bot.run(os.getenv('DISCORD_TOKEN'))