raquete_x = 0
bola_eixo_x = 0
bola_eixo_y = 0
bola_eixo_deslocamento_x = 0
bola_eixo_deslocamento_y = 0
pontuacao = 0
intervalo = 0
intervalo_passo = 0
em_jogo = False
# movimento para esquerda

def on_button_pressed_a():
    global raquete_x
    if raquete_x > 0:
        led.unplot(raquete_x + 1, 4)
        raquete_x = raquete_x - 1
        led.plot(raquete_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

# movimento para direita

def on_button_pressed_b():
    global raquete_x
    if raquete_x < 3:
        led.unplot(raquete_x, 4)
        raquete_x = raquete_x + 1
        led.plot(raquete_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global raquete_x, bola_eixo_x, bola_eixo_y, bola_eixo_deslocamento_x, bola_eixo_deslocamento_y, pontuacao, intervalo, intervalo_passo, em_jogo
    raquete_x = 0
    bola_eixo_x = 3
    bola_eixo_y = 4
    bola_eixo_deslocamento_x = -1
    bola_eixo_deslocamento_y = -1
    pontuacao = 0
    intervalo = 500
    intervalo_passo = 10
    basic.show_string("PLAY")
    em_jogo = True
    led.plot(bola_eixo_x, bola_eixo_y)
    led.plot(raquete_x, 4)
    led.plot(raquete_x + 1, 4)
    while em_jogo:
        if bola_eixo_x + bola_eixo_deslocamento_x > 4:
            bola_eixo_deslocamento_x = bola_eixo_deslocamento_x * -1
        elif bola_eixo_x + bola_eixo_deslocamento_x < 0:
            bola_eixo_deslocamento_x = bola_eixo_deslocamento_x * -1
        if bola_eixo_y + bola_eixo_deslocamento_y < 0:
            bola_eixo_deslocamento_y = bola_eixo_deslocamento_y * -1
        elif bola_eixo_y + bola_eixo_deslocamento_y > 3:
            if led.point(bola_eixo_x + bola_eixo_deslocamento_x,
                bola_eixo_y + bola_eixo_deslocamento_y):
                bola_eixo_deslocamento_y = bola_eixo_deslocamento_y * -1
                pontuacao = pontuacao + 1
                if intervalo - intervalo_passo >= 0:
                    intervalo = intervalo - intervalo_passo
            else:
                em_jogo = False
        if em_jogo:
            led.plot(bola_eixo_x + bola_eixo_deslocamento_x,
                bola_eixo_y + bola_eixo_deslocamento_y)
            led.unplot(bola_eixo_x, bola_eixo_y)
            bola_eixo_x = bola_eixo_x + bola_eixo_deslocamento_x
            bola_eixo_y = bola_eixo_y + bola_eixo_deslocamento_y
            basic.pause(intervalo)
        else:
            game.set_score(pontuacao)
            game.game_over()
basic.forever(on_forever)
