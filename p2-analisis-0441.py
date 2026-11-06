import pandas as pd
import numpy as np

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