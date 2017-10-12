"""Exemplo Teste Integração"""

import unittest

import descontos


class CarrinhoCompras:
    def __init__(self, produtos=[], tipo_pagamento="parcelado"):
        self._produtos = produtos
        self._tipo_pagamento = tipo_pagamento

    def calcular_descontos(self):
        """calcula os descontos aplicados no carrinho"""
        desconto = descontos.calcular(self.total, self._tipo_pagamento)
        return desconto

    @property
    def total(self):
        """Retorna o total do carrinho"""
        total = 0
        for produto in self._produtos:
            total += produto["valor"]

        return total


class CarrinhoComprasTestCase(unittest.TestCase):
    def test_fechar_compra(self):
        produtos = [
            {"nome": "ProdutoA", "valor": 10},
            {"nome": "ProdutoB", "valor": 90}
        ]
        tipo_pagamento = "avista"
        carrinho = CarrinhoCompras(produtos, tipo_pagamento)
        esperado = 10
        desconto = carrinho.calcular_descontos()

        self.assertEqual(esperado, desconto)



if __name__ == '__main__':
    unittest.main()
