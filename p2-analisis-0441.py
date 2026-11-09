import pandas as pd
import numpy as np
# Ramirez Azul NC 0441  

print("Detección de Transacciones Fraudulentas Ramirez Azul NC 0441")
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df = pd.DataFrame(transacciones)
print(df)

print("--- Agrupar por una sola columna ---")
agrupado = df.groupby('Monto')
print(agrupado)
print("--- por agregacion ---")

# Salario promedio por monto
print(agrupado['Ubicacion_Inusual'].mean())
print("monto maxima")
#  Máximo en cada grupo 
print(agrupado['Es_Fraude'].max())

print("--Ramirez Azul--")
print("+-+-+-+-+Segunda parte+-+-+-+-+")
print("agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> suma")
resultado_agregado = agrupado['Monto'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("Columna Team --> Equipo")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Equipo', 'Ubicacion_Inusual'])['Monto'].mean()
print(agrupado_multiple)