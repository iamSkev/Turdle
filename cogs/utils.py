from xmlrpc.client import Boolean
import disnake
from typing import Optional
from disnake.ext import commands

ALLOWED_ROLES = 884136022592610334
BANNED_USER = 619672500019789844

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def bot_check_once(self, ctx) -> Boolean:
        if ctx.author.id == BANNED_USER:
            return False
        return True
    
    @commands.command()
    @commands.has_any_role(ALLOWED_ROLES)
    async def say(
        self, 
        ctx, 
        channel: Optional[disnake.TextChannel], 
        *, 
        phrase
        ) -> None:
        channel = channel or ctx.channel
        await channel.send(phrase)
    
    @say.error
    async def say_error(self, ctx, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Sorry bub no can do. I actually need something to send.") 
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("Sorry bub you don't have the required roles.")

def setup(bot):
    bot.add_cog(Utilities(bot))