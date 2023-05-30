let raquete_x = 0
let bola_eixo_x = 0
let bola_eixo_y = 0
let bola_eixo_deslocamento_x = 0
let bola_eixo_deslocamento_y = 0
let pontuacao = 0
let intervalo = 0
let intervalo_passo = 0
let em_jogo = false
//  movimento para esquerda
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (raquete_x > 0) {
        led.unplot(raquete_x + 1, 4)
        raquete_x = raquete_x - 1
        led.plot(raquete_x, 4)
    }
    
})
//  movimento para direita
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (raquete_x < 3) {
        led.unplot(raquete_x, 4)
        raquete_x = raquete_x + 1
        led.plot(raquete_x + 1, 4)
    }
    
})
basic.forever(function on_forever() {
    
    raquete_x = 0
    bola_eixo_x = 3
    bola_eixo_y = 4
    bola_eixo_deslocamento_x = -1
    bola_eixo_deslocamento_y = -1
    pontuacao = 0
    intervalo = 500
    intervalo_passo = 10
    basic.showString("PLAY")
    em_jogo = true
    led.plot(bola_eixo_x, bola_eixo_y)
    led.plot(raquete_x, 4)
    led.plot(raquete_x + 1, 4)
    while (em_jogo) {
        if (bola_eixo_x + bola_eixo_deslocamento_x > 4) {
            bola_eixo_deslocamento_x = bola_eixo_deslocamento_x * -1
        } else if (bola_eixo_x + bola_eixo_deslocamento_x < 0) {
            bola_eixo_deslocamento_x = bola_eixo_deslocamento_x * -1
        }
        
        if (bola_eixo_y + bola_eixo_deslocamento_y < 0) {
            bola_eixo_deslocamento_y = bola_eixo_deslocamento_y * -1
        } else if (bola_eixo_y + bola_eixo_deslocamento_y > 3) {
            if (led.point(bola_eixo_x + bola_eixo_deslocamento_x, bola_eixo_y + bola_eixo_deslocamento_y)) {
                bola_eixo_deslocamento_y = bola_eixo_deslocamento_y * -1
                pontuacao = pontuacao + 1
                if (intervalo - intervalo_passo >= 0) {
                    intervalo = intervalo - intervalo_passo
                }
                
            } else {
                em_jogo = false
            }
            
        }
        
        if (em_jogo) {
            led.plot(bola_eixo_x + bola_eixo_deslocamento_x, bola_eixo_y + bola_eixo_deslocamento_y)
            led.unplot(bola_eixo_x, bola_eixo_y)
            bola_eixo_x = bola_eixo_x + bola_eixo_deslocamento_x
            bola_eixo_y = bola_eixo_y + bola_eixo_deslocamento_y
            basic.pause(intervalo)
        } else {
            game.setScore(pontuacao)
            game.gameOver()
        }
        
    }
})
