import unittest
from unittest.mock import patch
from io import StringIO

class Endereco:
    def __init__(self, endereco, numero):
        self._endereco = endereco
        self._numero = numero


class Usuario:
    def __init__(self, nome, usuario, senha, endereco):
        self._nome = nome
        self._usuario = usuario
        self._senha = senha
        self._endereco = endereco

    def formatar_endereco(self):
        return f"{self._endereco._endereco}, {self._endereco._numero}"

    def __str__(self):
        return (f'{self._nome} ({self._usuario}) mora na '
                f'{self.formatar_endereco()} e tem a senha {self._senha}')


def lazy_request_usuario(user_id):
    # Deveria buscar de algum lugar, mas estou com preguiça :(
    endereco = Endereco("Rua ABC", "123")
    return Usuario("Élysson MR", "elyssonmr", "minhasenhasecreta",
                   endereco)


@patch("sys.stdout", new_callable=StringIO)
class RequestUsuarioTestCase(unittest.TestCase):
    def test_request_usuario(self, _out):
        usuario = lazy_request_usuario(12354)

        self.assertEqual(
            'Élysson MR (elyssonmr) mora na Rua ABC, 123 '
            'e tem a senha minhasenhasecreta', str(usuario)
        )


if __name__ == '__main__':
    unittest.main()
