from msqbitsReporter.behavior import time_table_message
import msqbitsReporter.discordAPI.connector as discordReporter
from discord.ext import commands
from discord import embeds,colour
bot = discordReporter.bot
embededcoulour = colour.Colour.dark_blue()
thumbmaillink = 'http://www.epsi.fr/wp-content/uploads/2017/04/Notre-futur-campus-en-video-!-101483_reference.png'
embedsepsifooter = "https://beecome.io"

class EpsiCommands(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='edt', aliases=['timetable', 'planning'],
                      brief='Display planed course',
                      help='Display course programmed for each day nearest the actual week')
    async def display_planning_course(self, ctx):
        for message in time_table_message.getFormatedPlanningWeek():
            embedmessage = embeds.Embed(
                title=message['title'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=embedsepsifooter)
            embedmessage.set_thumbnail(url=thumbmaillink)
            for fields in message['courses']:
                embedmessage.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=True)
                embedmessage.add_field(name=fields['courseroom'], value=fields['courseteacher'], inline=True)

            await ctx.send(embed=embedmessage)

    @commands.command(name='daycourse', aliases=['coursefor', 'cours'],
                      brief='Display planed course for given day',
                      usage='date in format : dd/mm/yyyy')
    async def display_planning_for_date(self, ctx, arg):
        for message in time_table_message.getPlanningFor(arg):
            embedmessage = embeds.Embed(
                title=message['title'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=embedsepsifooter)
            embedmessage.set_thumbnail(url=thumbmaillink)
            for fields in message['courses']:
                embedmessage.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=True)
                embedmessage.add_field(name=fields['courseroom'], value=fields['courseteacher'], inline=True)

            await ctx.send(embed=embedmessage)

    @commands.command(name="todayedt", aliases=['edttoday','coursjours'],
                      brief='display course scheduled today')
    async def display_today_planning(self,ctx):
        for message in time_table_message.getThePlanningForToday():
            embedmessage = embeds.Embed(
                title=message['title'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=embedsepsifooter)
            embedmessage.set_thumbnail(url=thumbmaillink)
            for fields in message['courses']:
                embedmessage.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=True)
                embedmessage.add_field(name=fields['courseroom'], value=fields['courseteacher'], inline=True)

            await ctx.send(embed=embedmessage)

    @commands.command(name="nextroom", aliases=['classroom','lasalle'],
                      brief="give next classroom")
    async def display_today_next_classroom(self,ctx):
        for message in time_table_message.getRoomNextClassRoom():
            embedmessage = embeds.Embed(
                title=message['title'],
                colour=embededcoulour
            )
            embedmessage.set_footer(text=embedsepsifooter)
            embedmessage.set_thumbnail(url=thumbmaillink)
            for fields in message['courses']:
                embedmessage.add_field(name=fields['hourscourse'], value=fields['courselabel'], inline=True)
                embedmessage.add_field(name=fields['courseroom'], value=fields['courseteacher'], inline=True)

            await ctx.send(embed=embedmessage)


def setup(bot):
    bot.add_cog(EpsiCommands(bot))