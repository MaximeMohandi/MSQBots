from PIL import Image, ImageDraw, ImageFont
import textwrap

BACKGROUND_PLANNING = 'asset/planning_template.png'
FONT = 'asset/Roboto-Regular.ttf'

img = Image.open(BACKGROUND_PLANNING)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FONT, 15)


def make_rectangle(texts, top, bottom, left, right, color):
    """
        Draw rectangle with text inside

        :param text: list of text to display in rectangle
        :param top: rectangle's top x position
        :param bottom: rectangle's bottom x position
        :param left: rectangle's left y position
        :param right: rectangle's right y position
        :param color: rectangle's background color
    """
    shape = ImageDraw.Draw(img)
    x_text = top + 10
    y_text = left
    shape.rectangle(((top, left), (bottom, right)), fill=color)
    for line in texts:
        draw.text((x_text, y_text), line, font=font, fill='#000000')
        y_text += 10


# lines
y_begin = 107
y_step = 60
y_end = 60*12
y = [i for i in range(y_begin, y_end, y_step)]

# schedules columns
x_time = 10
nb_times = 11
times = [(8+i, 9+i) for i in range(0, nb_times)]

# days column
x_step_day = 170
x_day_begin = 109
x_day_end = x_step_day*6
x_day = [i for i in range(x_day_begin, x_day_end, x_step_day)]

make_rectangle(['titre', 'prof', 'cours', 'heure'], x_day[0], x_day[1], y[1], y[2], "#ffffff")


img.show()
