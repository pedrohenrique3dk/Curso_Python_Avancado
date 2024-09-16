from sys import path

from Aula36_package.modulo import soma_do_modulo
from Aula36_package import modulo
from Aula36_package.modulo import *

print(__name__) # primeiro modulo de entrada 


print(soma_do_modulo(2, 3))
print(modulo.soma_do_modulo(3, 4))
print(x)

# Você pode importar o módulo de várias formas como visto acima..

from Aula36_package.modulo import soma_do_modulo

# Se você tentar importar um módulo que tem outro módulo importar, sendo esse outro módulo "irmão" do modulo, porém não é irmão do main, vai dar erro.

# Para dar certo temos que mostrar todo o caminho que o main deve percorrer 