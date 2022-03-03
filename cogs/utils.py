import disnake
from disnake.ext import commands

ALLOWED_ROLES = 884136022592610334

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role(ALLOWED_ROLES)
    async def say(self, ctx, channel: disnake.TextChannel,* , phrase):
        await channel.send(phrase)
    
    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            param = error.param
            if param == "channel: disnake.channel.TextChannel":
                await ctx.send("Sorry bub no can do. I need a channel to send stuff to.")
            else:
                await ctx.send(param)
                await ctx.send("Hey! I actually need something to send.") 

def setup(bot):
    bot.add_cog(Utilities(bot))