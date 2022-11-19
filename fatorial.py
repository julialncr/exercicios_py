atual = 1
fatorial = 1

numero = int(input("Digite um número: "))

while (atual <= numero):
    fatorial = fatorial * atual
    atual += 1

print("O fatorial de ", numero, " é: ", fatorial, "\n")