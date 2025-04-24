def flatten(lista_anidada):
    lista_flattened = []
    for elemento in lista_anidada:
        if isinstance(elemento, (list, tuple)):  
            lista_flattened.extend(flatten(elemento))
        elif isinstance(elemento, dict):  
            lista_flattened.extend(flatten(list(elemento.items())))  
        else:
            lista_flattened.append(elemento)
    return lista_flattened