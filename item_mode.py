import game_framework
from pico2d import *
import game_world
import play_mode

image = None


def init():
    global image

    image = load_image('item_select.png')


def finish():
    global image
    del(image)


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mode.boy.item = None
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.boy.item = 'BALL'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.boy.item = 'BIG_BALL'
