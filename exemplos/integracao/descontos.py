"""Calculador de Descontos"""


def aplicar_desconto_avista(valor):
    """Aplica 10% de desconto"""
    return valor * 0.1


def aplicar_desconto_parcelado(valor):
    """Aplica 5% de desconto"""
    return valor * 0.05


def calcular(valor_total, tipo_pagamento):
    """Calcula o desconto de acordo com as regras de desconto"""
    if tipo_pagamento == "avista":
        desconto = aplicar_desconto_avista(valor_total)
        return desconto

    if tipo_pagamento == "parcelado":
        desconto = aplicar_desconto_avista(valor_total)
        return desconto

    return 0
