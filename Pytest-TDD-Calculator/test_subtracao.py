import pytest
from calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()
def test_subtracao(calculadora):
    assert calculadora.subtracao(5, 2) == 3
    