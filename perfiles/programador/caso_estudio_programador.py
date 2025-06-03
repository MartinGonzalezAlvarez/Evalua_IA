# caso_estudio_programador.py
import math
import unittest

# Función para calcular el factorial de un número
# TODO: Corregir el error en esta función
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "El factorial no está definido para números negativos"
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact


# Función para verificar si un número es primo
# TODO: Implementar esta función
def es_primo(n):
    # Esta función debe devolver True si n es primo, False en caso contrario
    # Debe manejar casos especiales como n < 2
    # Debe ser eficiente (no probar todos los números hasta n-1)
    pass  # Reemplaza "pass" con tu implementación

# Función para encontrar el número más grande en una lista
# TODO: Corregir el error en esta función
def numero_mas_grande(lista_numeros):
    if not lista_numeros:
        return None  # Devuelve None si la lista está vacía
    mas_grande = lista_numeros[0]
    for numero in lista_numeros:
        if numero > mas_grande:
            mas_grande = numero
    return mas_grande

# Función para calcular la distancia euclidiana entre dos puntos
# TODO: Implementar esta función
def distancia_euclidiana(punto1, punto2):
    # punto1 y punto2 son tuplas o listas de coordenadas (ej. (x1, y1), (x2, y2))
    # Debe devolver la distancia euclidiana entre los dos puntos
    pass  # Reemplaza "pass" con tu implementación

# Clase para pruebas unitarias (opcional, pero valorado)
class TestFunciones(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-1), "El factorial no está definido para números negativos")

    # TODO: Añadir pruebas para las otras funciones (es_primo, numero_mas_grande, distancia_euclidiana)
    # Por ejemplo:
    # def test_es_primo(self):
    #     self.assertTrue(es_primo(7))
    #     self.assertFalse(es_primo(4))

if __name__ == '__main__':
    # Ejemplos de uso (puedes modificarlos o añadir más)
    print(f"Factorial de 5: {factorial(5)}")
    print(f"¿7 es primo?: {es_primo(7)}")
    print(f"Número más grande en [1, 5, 2, 8, 3]: {numero_mas_grande([1, 5, 2, 8, 3])}")
    print(f"Distancia entre (1, 2) y (4, 6): {distancia_euclidiana((1, 2), (4, 6))}")

    # Ejecutar las pruebas unitarias (si las implementas)
    # unittest.main()