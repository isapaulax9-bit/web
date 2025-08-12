numero = int(input("Deseja a tabuada de qual numero? "))

while numero < 0:
    print("Numero invalido")
    print("Por favor,insira um numero positivo.")
    numero = int(input("Deseja a tabuada de qual numero? "))

    for i in range(1,11):
produto = numero * 1
    print(f"{numero} x {1} = {produto}")