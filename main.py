import DataCleaning
import Metricas
import Analisis_Especifico
import Visualizacion

df = DataCleaning.Data_Cleaning('DataSetIa.csv')
df.to_csv('DataSetClean.csv', index=False)

Metricas.metricas('DataSetClean.csv')

Analisis_Especifico.Analytics('DataSetClean.csv')

Visualizacion.graficas('DataSetClean.csv')

print(f"\n\nFin\n\n")
