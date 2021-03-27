from calculadora import som
from calculadora import sub
from calculadora import mult
from calculadora import div

def teste_som():
    assert som(10,10) == 20

def teste_sub():
    assert sub(12,5) == 7

def teste_mult():
    assert mult(6,6) == 36

def teste_div():
    assert div(30,10) == 3


