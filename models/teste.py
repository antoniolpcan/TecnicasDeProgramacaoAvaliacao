class Jogador:

    def __init__(self, nome: str):
        self.nome = nome
    
    def retorna_nome(self):
        print("Nome do jogador: ", self.nome)

class Time(Jogador):
    jogadores: list

    def __init__(self, time: str):
        self.time = time
    
    def adiciona_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def mostra_time(self):
        return self.__dict__

class Pontos(Time):
    def __init__(self, pontos: int, time: Time):
        self.pontos = pontos
        self.time = time
    
    def realiza_ponto(self):
        self.pontos += 1
        return self.pontos