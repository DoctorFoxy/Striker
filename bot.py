import discord 
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()
client = command.Bot(command_prefix = "=")

@client.event
async def on_ready():
	print("Bot is ready!")
	
@client.event
async def on_message(message):
	if message.content == "ping":
		await client.send_message(message.channel, "Pong!")


client.run("NDU1MTExODQzNjE5NDA1ODM1.Df6Epw._emD_LSqM7Bi8JB_iF2rWsnDNf0")