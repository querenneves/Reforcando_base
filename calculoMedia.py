def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

# Exemplo de uso
lista_numeros = [10, 15, 20, 25, 30]
media_resultante = calcular_media(lista_numeros)

print(f'A média dos números é: {media_resultante}')
