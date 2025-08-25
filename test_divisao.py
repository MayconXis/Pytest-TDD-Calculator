import pytest
from calculadora import Calculadora

@pytest.fixture


def calculadora():
    return Calculadora()
#@pytest.mark.divisao
def test_divisao(calculadora):
    assert calculadora.divisao(10, 2) == 5 
#@pytest.mark.divisaoZero
def test_divisaoZero():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.divisao(10, 0), "Não é possivel dividir por 0"
#@pytest.mark.divisaoDecimal
def test_divisaoDecimal(calculadora):
    assert calculadora.divisao(5, 2) == 2.5