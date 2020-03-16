from guizero import App, Text, PushButton, TextBox, Combo
import gif_generator
import sys

app = App(title="GIF Countdown Generator", layout='grid')

heading = Text(app, text='Countdown GIF Generator', size=18, grid=[0,0,3,1], width="fill")
minutes_label = Text(app, text='Minutes', grid=[0,1], width="fill", align="left")
seconds_label = Text(app, text='Seconds', grid=[1,1], width="fill", align="left")
minutes_input = TextBox(app, text='0', grid=[0,2], width="fill")
seconds_input = TextBox(app, text='0', grid=[1,2], width="fill")

background_color_dropdown_label = Text(app, text='Background colour', grid=[0,3], align="left")
text_color_dropdown_label = Text(app, text='Countdown text colour', grid=[0,5], align="left")


background_color_dropdown = Combo(
    app, 
    grid=[0,4,2,1], 
    options=['White', 'Grey', 'Blue', 'Transparent'], 
    width=20, 
    align="left"
    )

text_color_dropdown = Combo(
    app, 
    grid=[0,6,2,1], 
    options=['Blue', 'Orange', 'Turquois', 'Grey', 'White'], 
    width=20, 
    align="left"
    )

generate = PushButton(
    app, 
    command=lambda: gif_generator.generate_gif(
        minutes_input.value, 
        seconds_input.value,
        background_color_dropdown.value,
        text_color_dropdown.value
        ), 
    grid=[2,2],
    text='Generate'
    )

exit_button = PushButton(
    app,
    command=sys.exit,
    grid=[0,7,3,1],
    text='Quit'
)

app.display()