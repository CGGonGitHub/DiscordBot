import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# On start
@bot.listen()
async def on_ready():
    await bot.change_presence(status= discord.Status.online, activity=discord.Game("https://discord.gg/qE95VSpvwW"))
    print(f'Running, logged in as {bot.user}')
    
# Commands
@bot.command()
async def repeat(ctx, *, args):
    await ctx.send(f'{args}')
        
@bot.listen()
async def on_message(message):
    if message.content == 'fuck you':
        await message.reply('no, fuck you')

@bot.listen()
async def on_message_delete(message):
    message.channel.send(f'{message.content}')

@bot.command()
async def dm(ctx, user, *, text):
    testuser = ctx.message.guild.get_member_named(user)
    if testuser:
        user = ctx.message.guild.get_member_named(user)
        await user.send(f'{text}')
    elif str.isnumeric(user):
        user = int(user)
        user = bot.get_user(user)
        await user.send(f'{text}')

@bot.command(name='bot')
async def _bot(ctx):
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

@bot.command()
async def server(ctx):
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


bot.run('MTA4Mzc1OTUwNDk3MTI3MjI2Mg.G81wNf.Nzk6o7y_pjO72dpXfKfESBBtxkFruwyyksfkqQ')
