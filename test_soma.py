import pytest
from calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_soma_dois_numeros_inteiros(calculadora):
    assert calculadora.soma(2, 3) == 5