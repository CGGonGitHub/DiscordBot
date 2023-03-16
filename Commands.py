import discord
from discord.ext import commands
from discord import app_commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sync')
    async def _sync(self, ctx):
        self.bot.tree.sync()
        print(f'synced!')

    @commands.command(name='repeat')
    async def _repeat(self, ctx, *, text):
        await ctx.send(text)
    
    @commands.command(name='bot' or 'botinfo')
    async def _bot(self, ctx):
        embed = discord.Embed(
        title='Eric Cartman',
        type='rich',
        description='Eric Cartman is a bot in development. thereal#5282 is using this bot to play around with the api and stuff.',
        url='https://discord.com/api/oauth2/authorize?client_id=1083759504971272262&permissions=1101860514880&scope=bot',
        colour=discord.Color.blue(),
        )
        embed.set_author(
            name='thereal#5282',
            icon_url='https://cdn.discordapp.com/avatars/1058129514632335360/ec758cc6e50339a9b1303b8bb12c6bdb.webp?size=320'
        )
        embed.set_image(url='https://cdn.discordapp.com/avatars/1083759504971272262/525c6fdc0fecd5edc5ea5d8301d68b8b.webp?size=640')
        embed.set_footer(text='Invite me to your Server now!! Click on the link in the title')
        await ctx.send(embed=embed)

    @commands.command(name='server' or 'serverinfo')
    async def _server(self, ctx):

        embed = discord.Embed(
        title=f'{ctx.guild}',
        type='rich',
        description='CGG Projects is the discord server of thereal#5282. He will post updates about his developing in many different ways there. It is also a great place to hangout!',
        colour=discord.Color.blurple(),
        )
        embed.set_author(
            name='thereal#5282',
            icon_url='https://cdn.discordapp.com/avatars/1058129514632335360/ec758cc6e50339a9b1303b8bb12c6bdb.webp?size=320'
        )
        embed.add_field(
            name='',
            value='https://discord.gg/qE95VSpvwW'
        )
        embed.set_footer(text='Join now!!11!!!1!')
        await ctx.send(embed=embed)


    @commands.command(name='sync')
    async def _sync(self, ctx):
        await self.bot.tree.sync()
        await ctx.send('Synchronized! Slash Commands are now avaible.')

    
async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
