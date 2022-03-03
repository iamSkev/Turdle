import disnake
from typing import Optional
from disnake.ext import commands

ALLOWED_ROLES = 884136022592610334

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role(ALLOWED_ROLES)
    async def say(self, ctx, channel: Optional[disnake.TextChannel],* , phrase):
        channel = channel or ctx.channel
        await channel.send(phrase)
    
    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Sorry bub no can do. I actually need something to send.") 

def setup(bot):
    bot.add_cog(Utilities(bot))