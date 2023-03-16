import discord
from discord.ext import commands
from discord import app_commands

class SlashCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    user = app_commands.Group(name='users', description='Getting Information about Users')

    @user.command(name='avatar', description='Gets the avatar of a user')
    async def _avatar(self, interaction: discord.Interaction, member: discord.Member):
        print(f'WORKRRR')
        await interaction.response.send_message(f'{member.display_avatar.with_size(4096).url}')

    @user.command(name='info', description='get a bunch of useless info about a user')
    async def _info(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title=f'{member.display_name}',
            description=f'{member.display_name} is one of the {interaction.guild.member_count} great members of {interaction.guild.name}.',
            type='rich',
            colour=member.color
        )
        embed.set_author(name=f'{member.name}', icon_url=member.avatar.url)
        embed.set_image(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    info = app_commands.Group(name='info', description='Information about me and thereal#5282')

    @info.command(name='owner', description='Information about my owner')
    async def _owner(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='CoolGermanGuy',
            description='Alias: CGG',
            type='rich',
            colour=000000
        )
        embed.set_author(name='thereal#5282', icon_url='https://cdn.discordapp.com/avatars/1058129514632335360/ec758cc6e50339a9b1303b8bb12c6bdb.webp?size=1024')
        embed.add_field(name='IRL Info', value='Name:\nAge: 14\nLocation: Germany', inline=True)
        embed.add_field(name='Twitch', value='Watch me play or code on Twitch!\nhttps://www.twitch.tv/CGGonTwitch', inline=True)
        embed.add_field(name='Roblox', value='I play a lot of roblox. Ive been developing on roblox for some time now and its not bad. People just create trash games.\nFollow me and play my games!!\nhttps://www.roblox.com/users/1136054560/profile', inline=False)
        await interaction.response.send_message(embed=embed)

    @info.command(name='bot', description='Information about me')
    async def _bot(self, interaction: discord.Interaction):
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
        await interaction.response.send_message(embed=embed)
    
    @info.command(name='server', description='Information about the Server')
    async def _server(self, interaction: discord.Interaction):
        embed = discord.Embed(
        title=f'{interaction.guild.name}',
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
        await interaction.response.send_message(embed=embed)

    admin = app_commands.Group(name='admin', description='Administrator stuff')

    @admin.command(name='nickname', description='Sets the nickname of a member')
    async def _nickname(self, interaction: discord.Interaction, member: discord.Member, newname: str):
        await member.edit(nick=newname)


    fun = app_commands.Group(name='fun', description='fun tools and stuff')

    @fun.command(name='embed', description='make an embed!!!')
    async def _embed(self, interaction: discord.Interaction, title: str, text: str):
        embed = discord.Embed(
            title= title,
            description= text,
        )
        embed.set_author(
            name= interaction.user.name,
            icon_url= interaction.user.avatar.url
        )
        await interaction.response.send_message(embed=embed)

    @fun.command(name='repeat', description='The bot will repeat your input text')
    async def _repeat(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(f'{text}')



async def setup(bot: commands.Bot):
    await bot.add_cog(SlashCommands(bot))
