import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficas(ruta: str):
    
    data = pd.read_csv(ruta)
    
    def Year_ROI_Values(data):
        valoresROI_year = data.groupby('Year')
        valoresROI_year = valoresROI_year['AI_ROI_Percent'].mean()
        fig, ax = plt.subplots()
        ax.plot(valoresROI_year)
        plt.savefig(f"graficas/Year_ROI_Values.png")
        plt.show()
        plt.close()

        
    def Relacion_MaturityS(data):
        
        TablaPivote = pd.pivot_table(data, values='AI_Maturity_Score',index='Industry',aggfunc='mean')
        TablaPivote = TablaPivote.sort_values(by='AI_Maturity_Score', ascending=False)

        sns.heatmap(TablaPivote, annot=True, cmap='coolwarm')
        plt.title('Nivel de Madurez de IA por Industria', fontsize=15)
        plt.ylabel('Industria')
        plt.xlabel('Puntaje Promedio')
        plt.savefig(f"graficas/Relacion_Maturity_Grafica.png")
        plt.show()
        plt.close()
        
    Year_ROI_Values(data)
    Relacion_MaturityS(data)

