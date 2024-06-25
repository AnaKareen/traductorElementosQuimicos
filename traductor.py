def traducir_letra_a_simbolo(letra):
    letras_a_simbolos = {
        'A': 'Au',
        'B': 'Be',
        'C': 'C',
        'D': 'Dy',
        'E': 'Er',
        'F': 'F',
        'G': 'Ga',
        'H': 'H',
        'I': 'I',
        'J': 'Jn',
        'K': 'K',
        'L': 'Li',
        'M': 'Mg',
        'N': 'N',
        'O': 'O',
        'P': 'P',
        'Q': 'Qu',
        'R': 'Rb',
        'S': 'S',
        'T': 'Ti',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'Xe',
        'Y': 'Y',
        'Z': 'Zn'
    }
    
    if letra.upper() in letras_a_simbolos:
        return letras_a_simbolos[letra.upper()]
    else:
        return letra  
def traducir_frase_a_simbolos(frase):
    resultado = ""
    for letra in frase:
        resultado += traducir_letra_a_simbolo(letra) 
    return resultado.strip()

entrada = input("Ingresa una palabra o frase para traducir: ")

resultado = traducir_frase_a_simbolos(entrada)
print(f"La traducción de '{entrada}' es: {resultado}")
