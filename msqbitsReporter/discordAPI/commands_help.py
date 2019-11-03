"""This custom help command is a perfect replacement for the default one on any Discord Bot written in Discord.py Rewrite!
However, you must put "bot.remove_command('help')" in your bot, and the command must be in a cog for it to work.
Written by Jared Newsom (AKA Jared M.F.)!"""

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
    async def help(self, ctx, *cogs):
        """Gets all cogs and commands of mine."""
        try:
            if not cogs:
                self.help_message = embeds.Embed(title='Command List',
                                                 description='Use `$help *command*` to find out more about them!\n(BTW, The Command Name Must Be in Title Case, Just Like this Sentence.)')
                cogs_desc = ''
                for x in self.bot.cogs:
                    cogs_desc += ('{} - {}'.format(x, self.bot.cogs[x].__doc__)+'\n')
                self.help_message.add_field(name='Cogs',
                                            value=cogs_desc[0:len(cogs_desc)-1],
                                            inline=False)
                cmds_desc = ''
                for y in self.bot.walk_commands():
                    cmds_desc += ('{} - {}'.format(y.name, y.help)+'\n')
                self.help_message.add_field(name='Uncatergorized Commands',
                                            value=(cmds_desc[0:len(cmds_desc)-1] if cmds_desc[0:len(cmds_desc)-1] else 'None'),
                                            inline=False)
                await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send(embed=self.help_message)
            else:
                if len(cogs) > 1:
                    print('This is way too many cog')
                else:
                    found = False
                    for x in self.bot.cogs:
                        for y in cogs:
                            if x == y:
                                self.help_message = embeds.Embed(title=cogs[0]+' Command Listing',
                                                                 description=self.bot.cogs[cogs[0]].__doc__)
                                for c in self.bot.get_cog(y).get_commands():
                                    if not c.hidden:
                                        self.help_message.add_field(name=c.name,
                                                                    value=(c.help if c.help else 'None'),
                                                                    inline=False)
                                found = True
                    if not found:
                        print(f'How do you even use {cogs[0]}?')
                    else:
                        await ctx.message.add_reaction(emoji='✉')
                    print(self.help_message)
                    await ctx.message.author.send(embed=self.help_message)
        except Exception as error:
            print(f'help command error: {error}')


def setup(bot):
    bot.add_cog(HelpCommands(bot))