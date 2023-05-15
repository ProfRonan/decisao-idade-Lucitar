valor = int(input())

if valor < 0:
    print("Impossível!")
if valor < 18:
    print("Não precisa se alistar.")
elif valor < 65 and valor > 18:
    print("Não esqueça de votar na próxima eleição.")
elif valor > 65:
    print("Vá descansar.")
else:
    print("Eita!")

    