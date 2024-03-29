import discord
import random
import os
import discord
from discord.ext import commands
from discord import app_commands

my_secret = os.environ['mydiscordtoken']

greeting_list = [
    "hello", "hi", "good morning", "good afternoon", "good evening",
    "@everyone"
]
bot = commands.Bot(command_prefix="!!~", intents=discord.Intents.all())


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Aina - とてもかわいい"))


async def send_message(message, user_message, is_private):
  try:
    response = get_response(user_message)
    await message.author.send(
        response) if is_private else await message.channel.send(response)

  except Exception as e:
    print(e)


TOKEN = my_secret
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(client.user, "is now running!")
  await client.change_presence(
      activity=discord.Game(name="Aina - とてもかわいい !", type=1))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = str(message.author)
  user_message = str(message.content)
  channel = str(message.channel)

  print(f'{username} said: "{user_message}" ({channel})')

  if user_message[0] == '?':
    user_message = user_message[1:]
    await send_message(message, user_message, is_private=True)
  else:
    await send_message(message, user_message, is_private=False)


client.run(TOKEN)
