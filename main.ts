input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
    Cabeza.change(LedSpriteProperty.Y, -2)
    Tronco.change(LedSpriteProperty.Y, -2)
    Piernas.change(LedSpriteProperty.Y, -2)
    basic.pause(700 - 100 * Dificultad)
    Cabeza.delete()
    Tronco.delete()
    Piernas.delete()
    Cuerpo()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
    Cabeza.change(LedSpriteProperty.Y, -1)
    Tronco.change(LedSpriteProperty.Y, -1)
    Piernas.change(LedSpriteProperty.Y, -1)
    basic.pause(700 - 100 * Dificultad)
    Cabeza.delete()
    Tronco.delete()
    Piernas.delete()
    Cuerpo()
})
function Cuerpo() {
    
    Cabeza = game.createSprite(0, 2)
    Cabeza.set(LedSpriteProperty.Brightness, 100)
    Cabeza.set(LedSpriteProperty.Blink, 100)
    Tronco = game.createSprite(0, 3)
    Piernas = game.createSprite(0, 4)
    if (input.runningTime() > 30000) {
        if (input.runningTime() <= 60000) {
            Dificultad = 2
        } else if (input.runningTime() <= 90000) {
            Dificultad = 3
        } else {
            Dificultad = 4
        }
        
    }
    
}

let Obstaculo_2 : game.LedSprite = null
let Obstáculo_1 : game.LedSprite = null
let Piernas : game.LedSprite = null
let Tronco : game.LedSprite = null
let Cabeza : game.LedSprite = null
let Dificultad = 0
music.setVolume(255)
Dificultad = 1
game.setLife(3)
Cuerpo()
basic.forever(function on_forever() {
    
    Obstáculo_1 = game.createSprite(4, 4)
    Obstaculo_2 = game.createSprite(4, randint(3, 4))
    basic.pause(100)
    for (let index = 0; index < 4; index++) {
        basic.pause(700 - 100 * Dificultad)
        Obstáculo_1.change(LedSpriteProperty.X, -1)
        Obstaculo_2.change(LedSpriteProperty.X, -1)
    }
    basic.pause(100)
    if (Obstáculo_1.isTouching(Piernas) || Obstaculo_2.isTouching(Piernas)) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpDown), music.PlaybackMode.InBackground)
        game.removeLife(1)
        Obstáculo_1.delete()
        Obstaculo_2.delete()
    } else {
        game.addScore(Dificultad)
        Obstáculo_1.delete()
        Obstaculo_2.delete()
    }
    
})
