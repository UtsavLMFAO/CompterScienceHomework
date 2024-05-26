import pickle
import pyglet
from pyglet.window import key
from .AnswersPage import display_answer
import pyglet.clock

file = open('Main\Static\ElementSymbols.dat', 'rb')
elements = pickle.load(file)


COMP_SCI = "Computer Science"
AEROSPACE = "Aerospace Engineering"
SPACE = "Space Exploration"
MEDICAL = "Medical Fields"
PSYCHOLOGY = "Human Psychology"
SURGICAL = "Surgical Operations"
DETECTIVE = "Detective Work"
user_text = ''


def home():
    global user_text
    max = False
    window = pyglet.window.Window(caption="Periodic Study of Elements!", vsync=True)

    
    pyglet.gl.glClearColor(91/255, 91/255, 91/255, 1)
    label = pyglet.text.Label(text="Which element do you want to learn about? ", font_name="Roboto", font_size=30, color=(180, 218, 220, 255))
    entry_label = pyglet.text.Label(text=user_text, font_name="Roboto", font_size=30, color=(180, 218, 220, 255), height=100)


    def edit_label():
        label.x = window.width//2
        label.y = window.height-100
        label.anchor_x = "center"
        label.anchor_y = "center"


    def edit_entry_label():
        global user_text
        entry_label.x = window.width//2
        entry_label.y = window.height//2
        entry_label.anchor_x = "center"
        entry_label.anchor_y = "center"
        entry_label.text = user_text


    @window.event
    def on_text(text):
        global user_text
        user_text += text


    @window.event
    def on_key_press(symbol, modifiers):
        global user_text
        if symbol == key.F11:
            window.maximize()
            print('Done!')

        if symbol == key.BACKSPACE:
            user_text = user_text[:-1]

        if symbol == key.ENTER:
            if user_text in elements.keys():
                user_text = elements[user_text]
            display_answer(user_text.strip())
            user_text = ''



    @window.event
    def on_draw():
        window.clear()
        edit_label()
        label.draw()
        edit_entry_label()
        entry_label.draw()

        
        

    pyglet.app.run()



