from datetime import date
import unittest


class CalculadoraDesconto:
    def __init__(self):
        self._inicio_verao = date(2017, 11, 1)
        self._final_verao = date(2018, 3, 31)

    def esta_no_verao(self, data_compra):
        maior_inicio = data_compra > self._inicio_verao
        menor_final = data_compra < self._final_verao
        return maior_inicio and menor_final

    def calcular_desconto(self, valor, data_compra):
        if self.esta_no_verao(data_compra):
            return valor * 10
        return valor * 1.1



class CalculadoraDescontoTestCase(unittest.TestCase):
    def test_calcular_desc_verao(self):
        data_compra = date(2017, 11, 15)
        valor = 100
        esperado = 1000
        calculadora = CalculadoraDesconto()
        preco_desconto = calculadora.calcular_desconto(valor, data_compra)

        self.assertEqual(esperado, preco_desconto)

    def test_calcular_desc_fora_verao(self):
        data_compra = date(2017, 10, 14)
        valor = 1000
        esperado = 1100
        calculadora = CalculadoraDesconto()
        preco_desconto = calculadora.calcular_desconto(valor, data_compra)
        self.assertEqual(esperado, preco_desconto)



if __name__ == '__main__':
    unittest.main()
