import unittest
from unittest.mock import patch
from io import StringIO


class Usuario:
    def __init__(self, nome, usuario, senha, endereco, numero):
        self._nome = nome
        self._usuario = usuario
        self._senha = senha
        self._endereco = endereco
        self._numero = numero

    def formatar_endereco(self):
        return f"{self._endereco}, {self._numero}"

    def __str__(self):
        return (f'{self._nome} ({self._usuario}) mora na '
                f'{self.formatar_endereco()} e tem a senha {self._senha}')


def lazy_request_usuario(user_id):
    # Deveria buscar de algum lugar, mas estou com preguiça :(
    return Usuario("Élysson MR", "elyssonmr", "minhasenhasecreta",
                   "Rua ABC", "123")


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
