"""Exemplo Teste Unitário"""

import unittest


def impar_par(numero):
    if numero % 2:
        return "Ímpar"
    else:
        return "Par"


class ImparParTestCase(unittest.TestCase):
    def test_impar_par_retorna_par(self):
        esperado = "Par"
        resposta = impar_par(2)
        self.assertEqual(esperado, resposta)


if __name__ == '__main__':
    unittest.main()
