import random
from datetime import datetime, timedelta

# Listas de nombres y apellidos
nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Laura', 'Pedro', 'Paula', 'Jorge', 'Mónica']
apellidos = ['Pérez', 'González', 'Fernández', 'Martínez', 'López', 'Rodríguez', 'García', 'Romero', 'Sosa', 'Benítez']
estados_civiles = ['Soltero', 'Casado', 'Divorciado', 'Viudo']
cargos = ['Meteorólogo', 'Ingeniero de datos', 'Analista', 'Técnico en telecomunicaciones', 'Programador', 'Asistente administrativo',
          'Ingeniero de software', 'Analista de sistemas', 'Coordinador', 'Secretaria']

# Función para generar una fecha aleatoria entre dos fechas
def generar_fecha(inicio, fin):
    delta = fin - inicio
    random_dias = random.randint(0, delta.days)
    return inicio + timedelta(days=random_dias)

# Parámetros de fecha de comienzo
fecha_inicio = datetime(2000, 1, 1)
fecha_fin = datetime(2023, 12, 31)

# Generar el archivo SQL
with open("insert_empleados.sql", "w") as file:
    file.write("USE smn_empleados;\n\n")
    file.write("INSERT INTO empleados (nombre, apellido, estado_civil, antiguedad, fecha_comienzo, cargo, legajo)\nVALUES\n")
    
    for i in range(1, 620):
        # Datos aleatorios para cada empleado
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        estado_civil = random.choice(estados_civiles)
        antiguedad = random.randint(1, 30)
        fecha_comienzo = generar_fecha(fecha_inicio, fecha_fin).strftime('%Y-%m-%d')
        cargo = random.choice(cargos)
        
        # Generar legajo con letra de A a D y número de 1 a 999
        letra_legajo = random.choice(['A', 'B', 'C', 'D'])
        numero_legajo = random.randint(1, 9999)
        legajo = f"{letra_legajo}{str(numero_legajo).zfill(4)}"
        
        # Escribir línea SQL
        file.write(f"('{nombre}', '{apellido}', '{estado_civil}', {antiguedad}, '{fecha_comienzo}', '{cargo}', '{legajo}')")
        
        if i < 619:
            file.write(",\n")
        else:
            file.write(";\n")
    
print("Archivo insert_empleados.sql generado correctamente.")
