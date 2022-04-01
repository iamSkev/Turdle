import asyncio
import disnake
from dotenv import load_dotenv
import os
from disnake.ext import commands

class Turdle(commands.Bot):
  def __init__(self):
    intents = disnake.Intents.all()
    super().__init__(command_prefix="t!", intents=intents)

  async def on_ready(self) -> None:
    print(f'Logged in as {self.user} (ID: {self.user.id})')

bot = Turdle()

load_dotenv()
token = os.getenv("BOT_TOKEN")

@bot.command()
@commands.is_owner()
async def load(ctx, extension) -> None:
  bot.load_extension(f'cogs.{extension}')
  await ctx.send("Succesfully did it poggers")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension) -> None:
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send("Succesfully did it poggers")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension) -> None:
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  await ctx.send("Did it")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)