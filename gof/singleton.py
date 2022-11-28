from abc import ABC, abstractclassmethod
from typing import List
from models.time import TimeJogo

class CompeticaoABC(ABC):

    @abstractclassmethod
    def mostra_placar(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def mostra_pontos_do_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def adiciona_pontos_ao_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def retorna_jogadores_do_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def adiciona_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def adiciona_jogador_ao_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

    @abstractclassmethod
    def remove_jogador_do_time(self):
        raise RuntimeError('TODO: Método ainda não implementado')

class DashBoard(CompeticaoABC):

    times: List[TimeJogo] = []

    @classmethod
    def mostra_placar(self):
        for time in self.times:
            print(time.__dict__)

    @classmethod
    def mostra_pontos_do_time(self, nome_time: str):
        for time in self.times:
            if nome_time == time.nome:
                print(f"Times do {time.nome}:", time.pontos)
                return time.pontos
        return "Não encontrado"
    
    @classmethod
    def adiciona_pontos_ao_time(self, nome_time: str):
        for time in self.times:
            if nome_time == time.nome:
                time.pontos = time.pontos + 1
        return "Não encontrado"

    @classmethod
    def retorna_jogadores_do_time(self, nome_time: str):
        for time in self.times:
            if nome_time == time.nome:
                print(f'Jogadores do {time.nome}:', time.jogadores)
                return time.jogadores
        return "Não encontrado"

    @classmethod
    def adiciona_time(self, time: TimeJogo):
        self.times.append(time)

    @classmethod
    def adiciona_jogador_ao_time(self, nome_time: str, jogador: str):
        for time in self.times:
            if nome_time == time.nome:
                time.jogadores.append(jogador)
                print(f"Jogador adicionado ao {time.nome}:", jogador)
                return time.jogadores
        return "Não encontrado"

    @classmethod
    def remove_jogador_do_time(self, nome_time: str, jogador: str):
        for time in self.times:
            if nome_time == time.nome:
                if jogador in time.jogadores:
                    time.jogadores.remove(jogador)
                    print(f"Jogador removido do {time.nome}:", jogador)

