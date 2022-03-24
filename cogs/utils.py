import disnake
from typing import Optional
import datetime
from datetime import datetime
from disnake.ext import commands

ALLOWED_ROLES = [884136022592610334, 949097027483086888, 956021556033761311]

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role(*ALLOWED_ROLES)
    async def say(self, ctx, channel: Optional[disnake.TextChannel], *, phrase) -> None:
        channel = channel or ctx.channel
        await channel.send(phrase)
    
    @commands.command()
    async def userinfo(self, ctx, id: int) -> None:
        user = await self.bot.fetch_user(id)
        if user is None:
            await ctx.send("Could not get info about that userid. Perhaps its wrong or it does not exist")
            return
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = disnake.Embed(color=0xdfa3ff, description=user)
        embed.set_author(name=user.display_name, icon_url=user.display_avatar)
        embed.set_thumbnail(url=user.display_avatar)
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(956359584233181295)
        embed = disnake.Embed(title="Welcome to Pomelo SMP!", description="You should go and check out <#955306783130386442> & the <#955306855305990174>!", colour=0xFFE684, timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/956026532105707560/956033570558861342/axolotl-minecraft.gif")
        embed.set_image(url="https://media.discordapp.net/attachments/956026532105707560/956034300518752276/minecraft-axolotl.gif")
        await channel.send(f"{member.mention} has just arrived! Say hi and slap them on the ass!")

    @commands.command()
    async def test(self, ctx):
        embed = disnake.Embed(title="Welcome to Pomelo SMP!", description="You should go and check out <#955306783130386442> & the <#955306855305990174>!", colour=0xFFE684, timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/956026532105707560/956033570558861342/axolotl-minecraft.gif")
        embed.set_image(url="https://media.discordapp.net/attachments/956026532105707560/956034300518752276/minecraft-axolotl.gif")
        await ctx.send(embed=embed)


    @say.error
    async def say_error(self, ctx, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Sorry bub no can do. I actually need something to send.") 
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("Sorry bub you don't have the required roles.")

def setup(bot):
    bot.add_cog(Utilities(bot))