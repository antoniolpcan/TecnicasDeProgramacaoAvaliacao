from gof.singleton import *

dash = DashBoard()

dash.mostra_placar()

time = TimeJogo(nome = "Brasil")
time2 = TimeJogo(nome = "Alemanha")

dash.adiciona_time(time)
dash.adiciona_time(time2)

dash.mostra_placar()

dash.retorna_jogadores_do_time('Brasil')

dash.adiciona_jogador_ao_time('Brasil', "Neymar")

dash.remove_jogador_do_time('Brasil', "Neymar")

dash.retorna_jogadores_do_time('Brasil')

dash.adiciona_jogador_ao_time('Brasil', "Neymar")

dash.adiciona_pontos_ao_time('Brasil')
dash.adiciona_pontos_ao_time('Brasil')

dash.mostra_pontos_do_time('Brasil')

