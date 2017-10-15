import unittest
from unittest.mock import patch
from io import StringIO


class Usuario:
    def __init__(self, nome, sobrenome, usuario, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._usuario = usuario
        self._senha = senha

    def nome_completo(self):
        return f"{self._nome} {self._sobrenome}"

    def __str__(self):
        return self.nome_completo()


class RequestUsuarioTestCase(unittest.TestCase):
    def test_nome_completo(self):
        usuario = Usuario("Élysson", "MR", "elyssonmr", "12345")
        esperado = "Élysson MR"
        resposta = usuario.nome_completo()

        self.assertEqual(esperado, resposta)

    def test_str(self):
        usuario = Usuario("Élysson", "MR", "elyssonmr", "12345")
        esperado = "Élysson MR"
        resposta = str(usuario)
        self.assertEqual(esperado, resposta)


if __name__ == '__main__':
    unittest.main()
