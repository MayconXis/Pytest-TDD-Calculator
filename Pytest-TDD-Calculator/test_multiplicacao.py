import pytest
from calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()
def test_divisao(calculadora):
    assert calculadora.multiplicacao(5, 2) == 10