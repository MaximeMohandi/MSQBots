"""
the base code for this custom help command has been developped here. I don't take any credit for it.
https://gist.github.com/StudioMFTechnologies/ad41bfd32b2379ccffe90b0e34128b8b
"""

import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands
from discord import embeds,colour
bot = discordReporter.bot
embededcoulour = colour.Colour.dark_green()
thumbmaillink = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
embedHelpfooter = "https://beecome.io"

class HelpCommands(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self,ctx,*cog):
        """Gets all cogs and commands of mine."""
        try:
            if not cog:
                halp=embeds.Embed(title='Cog Listing and Uncatergorized Commands',
                                  description='Use `$help *cog*` to find out more about them!\n(BTW, the Cog Name Must Be in Title Case, Just Like this Sentence.)',
                                  color=embededcoulour)
                cogs_desc = ''
                for x in self.bot.cogs:
                    cogs_desc += ('{0} - {1}'.format(x,self.bot.cogs[x].__doc__)+'\n')
                halp.add_field(name='Cogs',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
                cmds_desc = ''
                for y in self.bot.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmds_desc += ('{0} - {1}'.format(y.name,y.help)+'\n')
                halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
                await ctx.send(embed=halp)
            else:
                if len(cog) > 1:
                    halp = embeds.Embed(title='Error!',description='That is way too many cogs!', color= colour.Color.red())
                    await ctx.send(embed=halp)
                else:
                    found = False
                    for x in self.bot.cogs:
                        for y in cog:
                            if x == y:
                                halp=embeds.Embed(title=cog[0]+' Command Listing',description=self.bot.cogs[cog[0]].__doc__)
                                for c in self.bot.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name,value=c.help,inline=False)
                                found = True
                    if not found:
                        halp = embeds.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=colour.Color.red())
                    await ctx.send(embed=halp)
        except Exception as ex:
            print(ex)


def setup(bot):
    bot.add_cog(HelpCommands(bot))