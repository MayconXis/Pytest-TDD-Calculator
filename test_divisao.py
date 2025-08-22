import pytest
from calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_divisao(calculadora):
    assert calculadora.divisao(10, 2) == 5 

def test_divisaoZero():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.divisao(10, 0), "Não é possivel dividir por 0"

def test_divisaoDecimal(calculadora):
    assert calculadora.divisao(5, 2) == 2.5