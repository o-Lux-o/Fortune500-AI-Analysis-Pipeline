import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def metricas(ruta: str):

    data = pd.read_csv(ruta)

    def RoiAVG(data):
        roi_AVG = data.groupby(['Industry', 'Year'])['AI_ROI_Percent'].mean().reset_index()
        print(f"\n\nListado de ROI promedio clasificado por año e industria\n\n{roi_AVG}\n\n")
        return roi_AVG

    def CrecimientoPorSector(data):
        AIMaturityScore2020 = data[data['Year'] == 2020].groupby('Industry')['AI_Maturity_Score'].mean()
        AIMaturityScore2025 = data[data['Year'] == 2025].groupby('Industry')['AI_Maturity_Score'].mean()

        crecimiento = AIMaturityScore2025 - AIMaturityScore2020

        top_3 = crecimiento.sort_values(ascending=False).head(3)

        print(f"\n\nLos tres sectores con más crecimientop en su 'AI_Maturity_Score' entre 2020 y 2025 son:\n\n{top_3}\n\n")
        
    def RevenueComparative(data):
        comparativa_revenue = data.groupby(['Year', 'Uses_AI'])['Revenue_USD'].sum().unstack()
        print(f"\n\nDataFrame que compara el 'Revenue_USD' anual de las empresas entre las que usas IA y las que no:\n\n{comparativa_revenue}\n\n")

    RoiAVG(data)
    CrecimientoPorSector(data)
    RevenueComparative(data)
    