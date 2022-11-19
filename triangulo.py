
lado_a = input("Informe o primeiro lado do triângulo: ")
lado_b = input("Informe o segundo lado do triângulo: ")
lado_c = input("Informe o terceiro lado do triângulo: ")

if float(lado_a) == float(lado_b) and float(lado_b) == float(lado_c):
    print("É um triângulo equilátero")
else:
    if float(lado_a) == float(lado_b) or float(lado_b) == float(lado_c) or float(lado_a) == float(lado_c):
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")