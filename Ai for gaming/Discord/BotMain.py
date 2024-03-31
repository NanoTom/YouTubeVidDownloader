import discord
from discord.ext import commands
import youtube_dl


# Define all intents
intents = discord.Intents.default()
intents.guilds = True  # Guilds
intents.members = True  # Members
intents.bans = True  # Bans
intents.emojis = True  # Emojis
intents.integrations = True  # Integrations
intents.webhooks = True  # Webhooks
intents.invites = True  # Invites
intents.voice_states = True  # Voice States
intents.presences = True  # Presences
intents.messages = True  # Messages
intents.reactions = True  # Message Reactions
intents.typing = True  # Message Typing
intents.dm_messages = True  # Direct Messages
intents.dm_reactions = True  # Direct Message Reactions
intents.dm_typing = True  # Direct Message Typing

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Type !hello for a greeting"))


@bot.command()
async def play(ctx,url:str):
    if ctx.voice_client is None:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You need to be in a vc")
            return
    # Set up youtube_dl options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # Download the audio from the YouTube URL
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']

    # Play the audio in the voice channel
    ctx.voice_client.play(discord.FFmpegPCMAudio(URL), after=lambda e: print('done', e))



@bot.command()
async def pin(ctx):
    await ctx.send("pong")


#somehow music playerbot







# Command: hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your Discord bot.')

bot.run('ODkzMjIwODcxMDU2MDE5NTg5.GdnFE9.Fb_LuJnPfnSsqoPvfiMev3I0-hp-Vf6mvoR7F0')