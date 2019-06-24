import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
client = commands.Bot(command_prefix = "?")

def community_report(guild):
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        if str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    return online, idle, offline
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game('Reading N177013 Out loud!'))
    print('bot is ready')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global sentdex_guild
bad_words = ["retard" ]
custom_emojis = ["https://cdn.discordapp.com/emojis/535572119896195082.gif?v=1"]
# async def react(message):                               #however we do need to call those emojis from the server... i mean guild
#     for emoji in message.guild.emojis:
#         if emoji.name in custom_emojis:
#             await message.add_reaction(emoji)

rand = ['Yes', 'No', 'Why are you even trying?', 'What do you think? NO', 'Maybe', 'Never', 'Yep','N :OMEGALUL:']
url = "https://www.youtube.com/watch?v=QKRi3SvCQqE"
# def __init__(self, bot):
#     self.bot = bot
#sentdex_guild = client.get_guild(375622104072192001)
# @client.event
# async def on_message(message):

#
#     if ";getinv" in message.content.lower():
#         await message.channel.send('https://discord.gg/TfFMdq4')
#     if ";selfdestruct" in message.content.lower():
#         await message.channel.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-atomic-a-bomb-gif-4464831")
#     if ";no u" in message.content.lower():
# #         await message.channel.send('https://cdn.discordapp.com/emojis/535572119896195082.gif?v=1')
# @client.event
# async def on_message(message):
#     if "hello bot" in message.content.lower():
#         if str(message.author) == "Anubis_mage#6121" and "hello bot" in message.content.lower():
#             await message.channel.send('Hi Oni!')
#         else:
#             await message.channel.send(f"Hi {message.author.name}!")
   # print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
#     if str(message.author) == "Anubis_mage#6121" and "!getout" in message.content.lower():
#         await message.channel.send('byee N :OMEGALUL:')
#         await client.close()
#     if ";join" in message.content.lower():
#         Author = message.author
#         VoiceChannel = Author.voice.channel
#         vc = await VoiceChannel.connect()
#         player = await YTDLSource.from_url(url, loop=self.bot.loop)
#         ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
#     if ";leave" in message.content.lower():
#         Author = message.author
#         VoiceChannel = Author.voice.channel
#         await VoiceChannel.disconnect()
#     if ";getcount" == message.content.lower():
#         await message.channel.send(f"```This sever has {sentdex_guild.member_count} degenerates```")
#     if ";info" == message.content.lower():
#         embed = discord.Embed(title="Noob bot", description="A Very **BASED** bot.", color=0xeee657)
#         embed.add_field(name="Author", value="AnubisMage")
#         embed.add_field(name="Server count", value=f"{len(client.guilds)}")
#         await message.channel.send(embed=embed)
#     if ";help" == message.content.lower():
#         embed = discord.Embed(title="NOOB bot", description="A Very ***BASED*** bot. List of commands are:", color=0xeee657)
#         embed.add_field(name=";getinv", value="Gives server inv link")
#         embed.add_field(name=";getcount", value="Shows server member count")
#         embed.add_field(name=";no u", value="**NO U**")
#
#         await message.channel.send(embed=embed)
#     for word in bad_words:
#         if message.content.count(word) > 0:
#             print("A bad word was said")
#             await message.channel.send('https://cdn.discordapp.com/emojis/418842424014536704.png?v=1')
#     if ";play" == message.content.lower():
#         player = self.get_player(message)
#         source = await YTDLSource.create_source(message, search, loop=self.bot.loop, download=False)
#         await player.queue.put(source)
#
#     if ";8ball" == message.content.lower():
#         await message.channel.send(f"{random.choice(rand)} {message.author.mention}")

sentdex_guild = client.get_guild(375622104072192001)
@client.command()
async def info(ctx):
    embed = discord.Embed(title="Noob bot", description="A Very Nice bot. IF THIS WORKS IM SHOOTING UP A SCHOL reeeeeeee", color=0x00FF00)
    embed.add_field(name="Author", value="AnubisMage")
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    await ctx.send(embed=embed)
client.remove_command('help')
@client.command()
async def severinfo(ctx):
    sentdex_guild = client.get_guild(375622104072192001)
    online, idle, offline = community_report(sentdex_guild)
    await ctx.channel.send(f"```This sever has {sentdex_guild.member_count} degenerates```")
    await ctx.channel.send(f"```Online Active: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

@client.command()
async def getinv(ctx):
    await ctx.channel.send('discord.gg/TfFMdq4')

@client.command()
async def join(ctx):
    Author = ctx.author
    VoiceChannel = Author.voice.channel
    await VoiceChannel.connect()
@client.command()
async def connect(ctx):
    channel=ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Anon bot", description="A anon bot. List of commands are:", color=0x00FF00)
    embed.add_field(name="?", value="The prefix")
    embed.add_field(name="?getinv", value="Gives server inv link")
    embed.add_field(name="?getcount", value="gives server member count")
    embed.add_field(name="?no u", value="NO U")

    await ctx.send(embed=embed)

@client.command()
async def hellobot(ctx):
    if str(ctx.author) == "Anubis_mage#6121" :
        await ctx.channel.send('Hi Oni!')
    else:
        await ctx.channel.send(f"Hi {message.author.name}!")

@client.command()
async def test(ctx):
    embed = discord.Embed(title="Pizza bot", description="A pizza bot. Pricese are:", color=0x00FF00)
    embed.add_field(name="20BCOKE", value="20oz Bottle Coke®        $1.89")
    embed.add_field(name="20BDCOKE", value="20oz Bottle Diet Coke®        $1.89")
    embed.add_field(name="D20BZRO", value="20oz Bottle Coke Zero™   $1.89")

    await ctx.send(embed=embed)

@client.command()
async def getout(ctx):
    await ctx.channel.send('byee :wave: ')
    await client.close()

# @client.command()
# async def getout(ctx):
#@client.commands()
# async def dmeveryonearesure(ctx):
#     while True:
#         c = ctx.guild.members
#         for user in c:
#             c.send('hi')

@client.event
async def on_member_join(member):
    print(f'{member} has joinned the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the sever.')


client.run('MzQ2NTQ4Mjk5MjkxMDMzNjAw.XOzUtw.s1WEW7uJQzD7pT6s2ibzMAcMT2Y')