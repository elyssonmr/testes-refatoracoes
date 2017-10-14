import unittest
from unittest.mock import patch
from io import StringIO


def imprimir_dados(dados):
    if dados["sexo"] == "F":
        print("Dados da Funcionária")
    else:
        print("Dados do Funcionário")

    # Dados Básicos
    print(f"Nome: {dados['nome']}")
    print(f"Email: {dados['email']}")
    print(f"Sexo: {dados['sexo']}")

    # Endereço
    print(f"Rua: {dados['endereco']['rua']}")
    print(f"Número: {dados['endereco']['numero']}")
    print(f"Bairro: {dados['endereco']['bairro']}")


@patch("sys.stdout", new_callable=StringIO)
class CalculadoraTestCase(unittest.TestCase):
    def test_calcular_valores_negativos(self, _out):
        esperado = (
            "Dados da Funcionária\nNome: Margarida\n"
            "Email: margarida@email.com\nSexo: F\nRua: Rua 12345\n"
            "Número: 1000\nBairro: Centro\n"
        )
        dados = {
            "nome": "Margarida",
            "email": "margarida@email.com",
            "sexo": "F",
            "endereco": {
                "rua": "Rua 12345",
                "numero": 1000,
                "bairro": "Centro"
            }
        }

        imprimir_dados(dados)

        self.assertEqual(esperado, _out.getvalue())

    def test_imprimir_dados(self, _out):
        esperado = (
            "Dados do Funcionário\nNome: Élysson MR\n"
            "Email: elyssonmr@email.com\nSexo: M\nRua: Rua 12345\n"
            "Número: 1000\nBairro: Centro\n"
        )

        dados = {
            "nome": "Élysson MR",
            "email": "elyssonmr@email.com",
            "sexo": "M",
            "endereco": {
                "rua": "Rua 12345",
                "numero": 1000,
                "bairro": "Centro"
            }
        }

        imprimir_dados(dados)

        self.assertEqual(esperado, _out.getvalue())



if __name__ == '__main__':
    unittest.main()
