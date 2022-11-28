from time import Pontos


class Dashboard(Pontos):

    def __init__(self, pontos):
        super(Pontos, self).__init__(pontos)
        self.pontos = pontos
    
    def mostra_pontos(self):
        print(self.pontos)
