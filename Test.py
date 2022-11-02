def contar_letras(texto):
    a = texto.replace(" ", "").replace(",", "").replace(".", "")
    diccionario = {}
    for letras in a:
        if letras != "á" and letras != "é" and letras != "í" and letras != "ó" and letras != "ú":
            if letras != letras.upper():
                if letras in diccionario:
                    diccionario[letras] += 1
                else:
                    diccionario[letras] = 1
    return diccionario


def ordenar_diccionario(**args):
    valor = sorted(args.values())
    ordenado = {}
    for i in valor:
        for k in args.keys():
            if args[k] == i:
                ordenado[k] = args[k]
                break
    return ordenado


texto1 = "hoeeeeeeeeeeelaaaaaa"
texto2 = "mundoooo"

dict2 = contar_letras(texto1)
dict2 = contar_letras(texto2)

x1 = ordenar_diccionario(**dict1)
x2 = ordenar_diccionario(**dict2)


contador1 = 0
contador2 = 0

for valor in x1.values():
    if valor > contador1:
        contador1 = valor

for valor in x2.values():
    if valor > contador2:
        contador2 = valor

if contador1 > contador2:
    print(x1)
elif contador1 < contador2:
    print(x2)
else:
    print("No se encontro una consonante con mayor frecuencia")
