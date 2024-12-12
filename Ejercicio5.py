# %% [markdown]
# ## EJERCICIOS 5
# 
# 1 - Implementa una función que verifique si una palabra dada es un palíndromo (se lee igual adelante o atrás).
# 2 - Implementa un función que reciba una serie de números como parámetro y determine cuantos impares hay en ella.
# 3 - Dada una lista de alumnos, donde cada alumno es un dictionario con "nombre, direccion y edad"; implementa una solución basada en funciones que transforme la letra intermedia (o más cercana al centro) del nombre de cada alumno en mayúscula y el resto en minúsculas.
# 	+ Pedro > peDro, Luis > luIs
# 4 - Dada una lista de alumnos anterior, donde cada alumno es un dictionario con nombre, direccion y edad; implementa una solución basada en funciones que transforme la lista en dos listas de tuplas del tipo (nombre, direccion), (nombre, edad).
# 5 - Escribe una expresión lambda que eleve al cubo todos los números de la lista siguiente: [1,2,3,4,5,6,7,8], usando la función map
#  

# %%
# 1 - Implementa una función que verifique si una palabra dada es un palíndromo (se lee igual adelante o atrás).

def funcion1(palabra):
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print('Es un palíndromo')
    else:
        print('No es un palíndromo')
    

palabra_dada = input()

funcion1(palabra_dada)

    


# %%
# 2 - Implementa un función que reciba una serie de números como parámetro y determine cuantos impares hay en ella.

def funcion2(param):
    contador=0
    # Recorrer la lista de números
    for numero in param:
        # Verificar si el número es impar
        if numero % 2 != 0:
            contador += 1
    return contador


parametros = (1, 2, 3, 4, 5, 6 , 7, 8, 9, 10)

funcion2(parametros)


# %%
# 3 - Dada una lista de alumnos, donde cada alumno es un dictionario con "nombre, direccion y edad"; implementa una solución basada en funciones que transforme la letra intermedia (o más cercana al centro) del nombre de cada alumno en mayúscula y el resto en minúsculas.

def transformaNombres(students):
	for un_alumno in students:
		nombre_mod = un_alumno['Nombre'].lower()
		l_nombre_mod = list(nombre_mod)
		medio = len(l_nombre_mod)//2
		l_nombre_mod[medio] += l_nombre_mod[medio].upper()
		un_alumno['Nombre'] = ''.join(l_nombre_mod)

	return students

alumnos = [
	{'Nombre': 'Ana', 'direccion': 'Calle x', 'edad': 22},
	{'Nombre': 'Luis', 'direccion': 'Calle y', 'edad': 24},
	{'Nombre': 'Juanna', 'direccion': 'Calle z', 'edad': 43},
	{'Nombre': 'Meteoro', 'direccion': 'Calle a', 'edad': 16}
]

transformaNombres(alumnos)


# %%
# 4 - Dada una lista de alumnos anterior, donde cada alumno es un dictionario con nombre, direccion y edad;
#     implementa una solución basada en funciones que transforme la lista en dos listas de tuplas del tipo (nombre, direccion), (nombre, edad).

def transformaEnTuplas(students):

    nueva_lista1 = []
    nueva_lista2 = []

    for un_alumno in students:
        nueva_lista1.append((un_alumno['Nombre'], un_alumno['direccion']))
        nueva_lista2.append((un_alumno['Nombre'], un_alumno['edad']))

    return nueva_lista1, nueva_lista2


l1, l2 =transformaEnTuplas(alumnos)

print(l1)
print(l2)

# %%
# 5 - Escribe una expresión lambda que eleve al cubo todos los números de la lista siguiente: [1,2,3,4,5,6,7,8], usando la función map

lista = [1, 2, 3, 4, 5, 6, 7, 8]

result = map(lambda x: x**3, lista)

list(result)


