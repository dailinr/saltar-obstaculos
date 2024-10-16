def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    Cabeza.change(LedSpriteProperty.Y, -2)
    Tronco.change(LedSpriteProperty.Y, -2)
    Piernas.change(LedSpriteProperty.Y, -2)
    basic.pause(700 - 100 * Dificultad)
    Cabeza.delete()
    Tronco.delete()
    Piernas.delete()
    Cuerpo()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
    Cabeza.change(LedSpriteProperty.Y, -1)
    Tronco.change(LedSpriteProperty.Y, -1)
    Piernas.change(LedSpriteProperty.Y, -1)
    basic.pause(700 - 100 * Dificultad)
    Cabeza.delete()
    Tronco.delete()
    Piernas.delete()
    Cuerpo()
input.on_button_pressed(Button.B, on_button_pressed_b)

def Cuerpo():
    global Cabeza, Tronco, Piernas, Dificultad
    Cabeza = game.create_sprite(0, 2)
    Cabeza.set(LedSpriteProperty.BRIGHTNESS, 100)
    Cabeza.set(LedSpriteProperty.BLINK, 100)
    Tronco = game.create_sprite(0, 3)
    Piernas = game.create_sprite(0, 4)
    if input.running_time() > 30000:
        if input.running_time() <= 60000:
            Dificultad = 2
        else:
            if input.running_time() <= 90000:
                Dificultad = 3
            else:
                Dificultad = 4
Obstaculo_2: game.LedSprite = None
Obstáculo_1: game.LedSprite = None
Piernas: game.LedSprite = None
Tronco: game.LedSprite = None
Cabeza: game.LedSprite = None
Dificultad = 0
music.set_volume(255)
Dificultad = 1
game.set_life(3)
Cuerpo()

def on_forever():
    global Obstáculo_1, Obstaculo_2
    Obstáculo_1 = game.create_sprite(4, 4)
    Obstaculo_2 = game.create_sprite(4, randint(3, 4))
    basic.pause(100)
    for index in range(4):
        basic.pause(700 - 100 * Dificultad)
        Obstáculo_1.change(LedSpriteProperty.X, -1)
        Obstaculo_2.change(LedSpriteProperty.X, -1)
    basic.pause(100)
    if Obstáculo_1.is_touching(Piernas) or Obstaculo_2.is_touching(Piernas):
        music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_DOWN),
            music.PlaybackMode.IN_BACKGROUND)
        game.remove_life(1)
        Obstáculo_1.delete()
        Obstaculo_2.delete()
    else:
        game.add_score(Dificultad)
        Obstáculo_1.delete()
        Obstaculo_2.delete()
basic.forever(on_forever)
