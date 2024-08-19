import re
cadena = "me acuerdo ; de ti : y no se como hacerlo"
result = re.split('[;:]', cadena)
print(result)
