import discord
from discord import app_commands
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        await bot.load_extension('botcommands')

bot = MyBot(command_prefix='!', intents=intents, activity=discord.Game("https://discord.gg/qE95VSpvwW"), status= discord.Status.online)

bot.run('MTA4Mzc1OTUwNDk3MTI3MjI2Mg.G81wNf.Nzk6o7y_pjO72dpXfKfESBBtxkFruwyyksfkqQ')
