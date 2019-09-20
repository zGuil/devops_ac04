from unittest import TestCase
from com.gui.ac04 import Elevador


class TestCaseElevador(TestCase):

    elevador = Elevador(5, 20)

    def test_elevador1(self):
        assert self.elevador.andar_atual == 0
        assert self.elevador.quantidade_pessoas == 0

    def test_elevador2(self):
        self.elevador.subir()
        self.elevador.entrar()
        self.elevador.entrar()
        self.elevador.subir()
        self.elevador.subir()
        assert self.elevador.andar_atual == 3
        assert self.elevador.quantidade_pessoas == 2

    def test_elevador3(self):
        self.elevador.sair()
        self.elevador.ir_para_andar(19)
        assert self.elevador.andar_atual == 19
        assert self.elevador.quantidade_pessoas == 1

    def test_elevador4(self):
        self.elevador.entrar()
        self.elevador.entrar()
        self.elevador.subir()
        self.elevador.subir()
        self.elevador.subir()
        assert self.elevador.andar_atual == 20
        assert self.elevador.quantidade_pessoas == 3

    def test_elevador5(self):
        self.elevador.ir_para_andar(30)
        assert self.elevador.andar_atual == 20
        assert self.elevador.quantidade_pessoas == 3

    def test_elevador6(self):
        self.elevador.ir_para_andar(-5)
        assert self.elevador.andar_atual == 20
        assert self.elevador.quantidade_pessoas == 3

    def test_elevador7(self):
        self.elevador.ir_para_andar(0)
        self.elevador.entrar()
        self.elevador.entrar()
        self.elevador.entrar()
        self.elevador.entrar()
        assert self.elevador.andar_atual == 0
        assert self.elevador.quantidade_pessoas == 5

    def test_elevador8(self):
        self.elevador.descer()
        self.elevador.descer()
        assert self.elevador.andar_atual == 0
        assert self.elevador.quantidade_pessoas == 5

    def test_elevador9(self):
        self.elevador.sair()
        self.elevador.sair()
        self.elevador.sair()
        self.elevador.sair()
        self.elevador.sair()
        self.elevador.sair()
        self.elevador.sair()
        assert self.elevador.andar_atual == 0
        assert self.elevador.quantidade_pessoas == 0
