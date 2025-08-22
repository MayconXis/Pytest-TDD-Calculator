import pytest
from calculadora import Calculadora

# Esses testes parametrizados para a função soma foram realizados para aprendizado com base no curso da udemy, 
# tendo o mesmo valor dos outros testes não parametizados
@pytest.mark.parametrize("a, b, resultado_esperado", [
    (2, 3, 5),          
    (0, 0, 0),          
    (-1, 1, 0),         
    (12, -5, 7),        
    (-5, -5, -10)   
])
def test_soma(a, b, resultado_esperado):
    calculadora = Calculadora()
    assert calculadora.soma(a, b) == resultado_esperado