import discord
from discord.ext import commands

class sneakyMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author == self.bot.user:
            if 'fuck you' in str.lower(message.content):
                await message.reply('no, fuck you')
            elif 'feet'in str.lower(message.content):
                await message.reply('https://images-ext-2.discordapp.net/external/rhJyoXjYPzogiUTRSrpYTtMgzPk6R0hkjUtXxmnf2Y8/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/680093266183847939/e3dae465bf834118951dfc5c1a88334f.png')
            elif 'touch grass'in str.lower(message.content):
                await message.reply('https://media.discordapp.net/attachments/961670649678544936/1048352008278638722/b7hbxhm3azp81.gif')
async def setup(bot: commands.Bot):
    await bot.add_cog(sneakyMessages(bot))
