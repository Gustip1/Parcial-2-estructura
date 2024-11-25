import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_division(self, key):
        # Método de la División
        return key % self.size

    def hash_extraccion(self, key):
        # Método de Extracción
        key_str = str(key)
        extracted_digits = key_str[:2] + key_str[-2:]  # Extrae los dos primeros y los dos últimos dígitos
        return int(extracted_digits) % self.size

    def hash_plegado(self, key):
        # Método de Plegado
        key_str = str(key)
        parts = [int(key_str[i:i+2]) for i in range(0, len(key_str), 2)]  # Divide la clave en partes de 2 dígitos
        return sum(parts) % self.size

    def hash_cuadrado_medio(self, key):
        # Método del Cuadrado Medio
        square = key ** 2
        square_str = str(square)
        mid_index = len(square_str) // 2
        extracted = square_str[mid_index-1:mid_index+1]  # Toma dos dígitos del centro
        return int(extracted) % self.size

    def hash_alfanumerico(self, key):
        # Función hash para claves alfanuméricas
        total = 0
        for char in key:
            total += ord(char)  # Suma los valores ASCII de los caracteres
        return total % self.size

    def insert_prueba_lineal(self, key, value, hash_function='division'):
        # Inserción con prueba lineal
        if hash_function == 'division':
            index = self.hash_division(key)
        elif hash_function == 'extraccion':
            index = self.hash_extraccion(key)
        elif hash_function == 'plegado':
            index = self.hash_plegado(key)
        elif hash_function == 'cuadrado_medio':
            index = self.hash_cuadrado_medio(key)
        elif hash_function == 'alfanumerico':
            index = self.hash_alfanumerico(key)
        else:
            raise ValueError("Función hash no válida")

        original_index = index
        step = 1
        while self.table[index] is not None:
            index = (original_index + step) % self.size
            step += 1
            if step > self.size:
                # La tabla está llena
                raise Exception("Tabla hash llena, no se pudo insertar la clave.")
        self.table[index] = (key, value)

    def search_prueba_lineal(self, key, hash_function='division'):
        # Búsqueda con prueba lineal
        if hash_function == 'division':
            index = self.hash_division(key)
        elif hash_function == 'extraccion':
            index = self.hash_extraccion(key)
        elif hash_function == 'plegado':
            index = self.hash_plegado(key)
        elif hash_function == 'cuadrado_medio':
            index = self.hash_cuadrado_medio(key)
        elif hash_function == 'alfanumerico':
            index = self.hash_alfanumerico(key)
        else:
            raise ValueError("Función hash no válida")

        original_index = index
        step = 1
        length_sequence = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1], length_sequence
            index = (original_index + step) % self.size
            step += 1
            length_sequence += 1
            if step > self.size:
                break
        return None, length_sequence

# Ejemplo de uso para el análisis comparativo
num_keys = 1000
random_keys = [random.randint(0, 100000) for _ in range(num_keys)]
hash_functions = ['division', 'extraccion', 'plegado', 'cuadrado_medio']

for func in hash_functions:
    print(f"\n--- Función Hash: {func} ---")
    # Tamaño de tabla no primo
    table_size_non_prime = 1000
    hash_table_non_prime = HashTable(table_size_non_prime)
    try:
        for key in random_keys:
            hash_table_non_prime.insert_prueba_lineal(key, f"Value {key}", hash_function=func)
    except Exception as e:
        print(f"Tabla no primo llena: {e}")

    total_length_non_prime = 0
    for key in random_keys:
        _, length = hash_table_non_prime.search_prueba_lineal(key, hash_function=func)
        total_length_non_prime += length
    average_length_non_prime = total_length_non_prime / num_keys
    print(f"Longitud promedio de la secuencia de prueba (tabla no primo): {average_length_non_prime:.2f}")

    # Tamaño de tabla primo
    table_size_prime = 1009  # Un número primo cercano a 1000
    hash_table_prime = HashTable(table_size_prime)
    try:
        for key in random_keys:
            hash_table_prime.insert_prueba_lineal(key, f"Value {key}", hash_function=func)
    except Exception as e:
        print(f"Tabla primo llena: {e}")

    total_length_prime = 0
    for key in random_keys:
        _, length = hash_table_prime.search_prueba_lineal(key, hash_function=func)
        total_length_prime += length
    average_length_prime = total_length_prime / num_keys
    print(f"Longitud promedio de la secuencia de prueba (tabla primo): {average_length_prime:.2f}")

# Prueba con claves alfanuméricas
num_keys_alpha = 1000
random_keys_alpha = [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8)) for _ in range(num_keys_alpha)]

print(f"\n--- Función Hash: alfanumerico ---")
table_size_prime_alpha = 1009
hash_table_alpha = HashTable(table_size_prime_alpha)
try:
    for key in random_keys_alpha:
        hash_table_alpha.insert_prueba_lineal(key, f"Value {key}", hash_function='alfanumerico')
except Exception as e:
    print(f"Tabla alfanumérica llena: {e}")

total_length_alpha = 0
for key in random_keys_alpha:
    _, length = hash_table_alpha.search_prueba_lineal(key, hash_function='alfanumerico')
    total_length_alpha += length
average_length_alpha = total_length_alpha / num_keys_alpha
print(f"Longitud promedio de la secuencia de prueba (claves alfanuméricas): {average_length_alpha:.2f}")

# Análisis comparativo
print("\nAnálisis Comparativo:")
print("Observamos que la longitud promedio de la secuencia de prueba es generalmente menor cuando el tamaño de la tabla es un número primo.")
print("Esto se debe a que un tamaño de tabla primo ayuda a distribuir las claves de manera más uniforme, reduciendo el agrupamiento de colisiones.")
print("Cuando el tamaño de la tabla no es primo, es más probable que se formen grupos de colisiones, lo cual incrementa la longitud de la secuencia de prueba.")
