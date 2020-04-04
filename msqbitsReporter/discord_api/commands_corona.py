from msqbitsReporter.corona import covid_stat as covid
from msqbitsReporter.common import credentials, exception as common_error
from discord.ext import commands, tasks
from discord import embeds, colour
import logging


EMBEDDED_COLOR = colour.Colour.dark_orange()
IMAGE_LINK = '//msqbitsReporter/corona/ressource/corona_logo.png'
EMBED_FOOTER = "https://www.worldometers.info/coronavirus/"

ERROR_MESSAGE = "hmm something happened, check the logs for more details"


class CoronaCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.news_channel = int(credentials.get_credentials('discord')['idNewsChannel'])
        self.display_planning_covid_daily.start()

    @commands.command(name='covid',
                      brief='display covid stats',
                      help='display number of covid case for the selected country or worldwide')
    async def display_covid_stat(self, ctx, arg=None):
        if arg is not None:
            await self.__display_covid(arg)
        else:
            await self.__display_covid()

    @tasks.loop(hours=24)
    async def display_planning_covid_daily(self):
        await self.__display_covid()

    async def __display_covid(self, country='world'):
        try:
            death = covid.get_death(country)
            cases = covid.get_cases(country)
            survivor = covid.get_survivors(country)

            await self.__send_embed_corona(cases, death, survivor)

        except common_error.HttpError:
            await self.__send_text(ERROR_MESSAGE)
            logging.exception('Something got wrong with the parsing of time table website', exc_info=True)

    async def __send_embed_corona(self, cases, death, survivors):
        embed_message = embeds.Embed(
            title=cases['country'],
            colour=EMBEDDED_COLOR
        )
        embed_message.set_footer(text="faites vos jeux")
        embed_message.set_image(url="attachment:{}//".format(IMAGE_LINK))

        embed_message.add_field(name='Cases', value="Total : {}  |  New : {}"
                                .format(cases['cases'], cases['new_cases']), inline=False)
        embed_message.add_field(name='Death', value="Total : {}  |  New : {}"
                                .format(death['death'], death['new_death']), inline=False)
        embed_message.add_field(name='Survivor', value="Total : {}".format(survivors['survivors']), inline=False)

        await self.bot.get_channel(self.news_channel).send(embed=embed_message)

    async def __send_text(self, message):
        await self.bot.get_channel(self.news_channel).send(message)


def setup(bot):
    bot.add_cog(CoronaCommands(bot))
