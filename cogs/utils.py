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
    
    @commands.command()
    async def userinfo(self, ctx, user: int = None) -> None:
        user = self.bot.get_user(user)
        if user is None:
            await ctx.send("Could not get info about that userid. Perhaps its wrong or it does not exist")
            return
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = disnake.Embed(color=0xdfa3ff, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.display_avatar)
        embed.set_thumbnail(url=user.display_avatar)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(user)+1))
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)

    @say.error
    async def say_error(self, ctx, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Sorry bub no can do. I actually need something to send.") 
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("Sorry bub you don't have the required roles.")

def setup(bot):
    bot.add_cog(Utilities(bot))