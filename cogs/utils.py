import disnake
from disnake.ext import commands

ALLOWED_ROLES = 884136022592610334

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role(ALLOWED_ROLES)
    async def say(self, ctx, channe=None,* , phrase):
        channel = channel or ctx.channel
        await channel.send(phrase)
    

def setup(bot):
    bot.add_cog(Utilities(bot))