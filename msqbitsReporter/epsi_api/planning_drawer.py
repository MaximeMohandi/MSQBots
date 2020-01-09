from PIL import Image, ImageDraw, ImageFont
from msqbitsReporter.epsi_api import time_table_api as timetable


BACKGROUND_PLANNING = 'asset/planning_bg.png'
FONT = 'asset/Roboto-Regular.ttf'

class planningDrawer():
    def __init__(self):
        self.days_map = [(1, 'lundi'), (2, 'mardi'), (3, 'mercredi'), (4, 'jeudi'), (5, 'vendredi')]
        self.hour_coord_map = [(i, 66 * 1) for i in range(1, 13)]
        self.day_coord_map = [(i, 114 + (i * 280)) for i in range(0, 5)]

    def draw_planning(self):
        img = Image.open(BACKGROUND_PLANNING)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT, 15)

    def __planning_for_draw(self):
        result = []
        week_planning = timetable.get_week_planning()
        for plannified in week_planning:
            day_title = plannified['title'].split('0')


# for days in day_coord_mapper:
#     for hour in hour_coord_mapper:
#         draw.text((days[1], hour[1]), "Draw This Text", 0, font=font)


img.show()
