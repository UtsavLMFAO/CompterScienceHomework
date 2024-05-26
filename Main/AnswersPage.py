import pickle
import pyglet
from pyglet.window import key

def read_file(name):
    with open("Main\Static\Database.db", "rb") as file:
        while True:
            try:
                element = pickle.load(file)
                if element["Element"].capitalize() == name.capitalize():
                    return element
            except:
                break

def show_answer_with_set_format(Name, Data):
    Name = Name.capitalize()
    window = pyglet.window.Window(caption=Name, width=1500, height=850, resizable=True)
    pyglet.gl.glClearColor(44/255, 44/255, 44/255, 1)

    labels = []

    def create_label(text, x, y, color):
        return pyglet.text.Label(text=text, font_name="Roboto", x=x, y=y, color=color, batch=batch)

    def update_labels_position():
        y = window.height - 50
        for label in labels:
            label.y = y
            y -= 50

    def scroll_text(dy):
        for label in labels:
            label.y -= dy  # Invert the scrolling direction

    def move_text(dx):
        for label in labels:
            label.x += dx

    batch = pyglet.graphics.Batch()

    labels.append(create_label(f'Name: {Data["Element"]}', x=50, y=window.height - 50, color=(191, 230, 225, 255)))
    labels.append(create_label(f'Atomic number: {Data["Atomic_number"]}', x=50, y=labels[-1].y - 50, color=(191, 230, 225, 255)))
    labels.append(create_label(f'Atomic mass: {Data["Atomic_mass"]}', x=50, y=labels[-1].y - 50, color=(191, 230, 225, 255)))

    uses = Data["Main_uses"]
    labels.append(create_label(f'Uses of {Name}:', x=50, y=labels[-1].y - 50, color=(191, 230, 225, 255)))
    for use, info in uses.items():
        labels.append(create_label(f"\t{use}: {info}", x=50, y=labels[-1].y - 50, color=(121, 130, 208, 255)))

    fun_facts = Data["Fun_facts"]
    labels.append(create_label('Fun Facts:', x=50, y=labels[-1].y - 50, color=(191, 230, 225, 255)))
    for count, facts in enumerate(fun_facts, 1):
        labels.append(create_label(f"\t{count}: {facts}", x=50, y=labels[-1].y - 50, color=(121, 130, 208, 255)))

    not_fun_facts = Data["Not_so_fun_facts"]
    labels.append(create_label(f'Not so fun facts about {Name}:', x=50, y=labels[-1].y - 50, color=(191, 230, 225, 255)))
    for count, facts in enumerate(not_fun_facts, 1):
        labels.append(create_label(f"\t{count}: {facts}", x=50, y=labels[-1].y - 50, color=(121, 130, 208, 255)))

    leave = pyglet.text.Label(text="Press 'esc' to exit!", color=(255, 100, 100, 255), x=0, y=window.height - 11, font_size=15, font_name="Roboto")
    hint_horizontal = pyglet.text.Label(text="Scroll right: Right Arrow, Scroll left: Left Arrow", color=(255, 255, 0, 255), x=0, y=0, font_name="Roboto", font_size=15)
    hint_vertical = pyglet.text.Label(text="Scroll Up or Down with the mouse!", color=(255, 255, 0, 255), x=0, y=0, font_name="Roboto", font_size=15)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

        leave.y = window.height - 60
        leave.x = window.width - leave.content_width - 10
        leave.draw()

        hint_horizontal.x = window.width - hint_horizontal.content_width - 10
        hint_horizontal.y = window.height - 40
        hint_horizontal.draw()
        
        hint_vertical.x = window.width - hint_vertical.content_width - 10
        hint_vertical.y = window.height - 20
        hint_vertical.draw()

    @window.event
    def on_resize(width, height):
        update_labels_position()

    @window.event
    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        scroll_text(scroll_y * 50)  # Adjust the scroll speed here



    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.RIGHT:
            move_text(50)
        if symbol == key.LEFT:
            move_text(-50)

    pyglet.app.run()

def display_answer(Name_of_Element):
    Element_data = read_file(Name_of_Element)
    show_answer_with_set_format(Name_of_Element, Element_data)
