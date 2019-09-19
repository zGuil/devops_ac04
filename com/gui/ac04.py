# Atividade Contínua 04
# Aluno 01: Guilherme Ferreira


# Implemente abaixo a classe Elevador, conforme descrição no enunciado da AC04

class Elevador:
    def __init__(self, capacidade, total_andares):
        self.andar_atual = 0
        self.total_andares = total_andares
        self.capacidade = capacidade
        self.quantidade_pessoas = 0

    def entrar(self):
        if self.capacidade > self.quantidade_pessoas:
            self.quantidade_pessoas += 1

    def sair(self):
        if self.quantidade_pessoas > 0:
            self.quantidade_pessoas -= 1

    def subir(self):
        if self.total_andares > self.andar_atual:
            self.andar_atual += 1

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual += 1

    def ir_para_andar(self, andar):
        if andar < self.total_andares and andar >= 0:
            self.andar_atual = andar
