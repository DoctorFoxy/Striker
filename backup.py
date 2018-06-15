import discord 
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()
client = Bot(description="Striker bot by DoctorFoxy", command_prefix="=", pm_help = False)

@client.event
async def on_ready():
	print("======================")
	print("Bot is ready!")
	print("======================")
	print("Striker is now running.")
	print("======================")

if "=" in line:
    param, value = line.split("=",1)

@client.event
async def on_message(message):
	if message.content.startswith("=ping"):
		userID = message.author.id
		await client.send_message(message.channel, value)


client.run("NDU1MTExODQzNjE5NDA1ODM1.Df6Epw._emD_LSqM7Bi8JB_iF2rWsnDNf0")












