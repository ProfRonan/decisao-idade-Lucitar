valor = int(input())

if valor < 0:
    print("impossível!")
if valor < 18:
    print("não precisa se alistar.")
elif valor < 65 and valor > 18:
    print("Não esqueça de votar na próxima eleição.")
elif valor > 65:
    print("Vá descansar.")
else:
    print("eita!")

    