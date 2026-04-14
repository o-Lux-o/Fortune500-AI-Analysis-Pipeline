import pandas as pd
import matplotlib.pyplot as plt


def Data_Cleaning(Ruta: str):
    
    data = pd.read_csv(Ruta)
    
    def DatosDuplicados(data):
        count = data.duplicated().sum()
        print(f"\n\nDuplicados: {count}")
        return count

    def ValoresNulos(data):
        print(f"\nValores NaN antes \n{data[data['Use_Case'].isna()]['Use_Case'].head()}\n")
        data['Use_Case'] = data['Use_Case'].fillna('No usa')
        print(f"\nValos NaN Ahora\n{data[data['Use_Case'] == 'No usa']['Use_Case'].head()}")
        return data

    def Formato(data):
        resultFormat = data.info()
        print(f'\n {resultFormat} \n')

    def Outliers(data):
        ColumnasNumber = ['Year', 'Revenue_USD','AI_ROI_Percent','AI_Maturity_Score']
        for x in ColumnasNumber:
            Q1 = data[x].quantile(0.25)
            Q3 = data[x].quantile(0.75)
            IQR = Q3 - Q1
            LimiteInferior = Q1 - 1.5 * IQR
            if LimiteInferior < 0:
                LimiteInferior = 0
            LimiteSuperior = Q3 + 1.5 * IQR
            DataOutliers = data[(data[x] < LimiteInferior) | (data[x] > LimiteSuperior)]
            if not DataOutliers.empty:
                print(f"- {x} Tiene Outliers: ({DataOutliers.shape[0]})")
                print(f"\nTodo valor de {x} abajo de {LimiteInferior} o arriba de {LimiteSuperior} son outliers\n")
            else:
                print(f"- {x} No tiene Outliers:")
                print(f"\nTodo valor de {x} abajo de {LimiteInferior} o arriba de {LimiteSuperior} serian outliers\n")
            plt.boxplot(data[x])
            plt.title(x)
            plt.savefig(f"graficas/Outliers_{x}.png")
            plt.close()
        return DataOutliers
    
    DatosDuplicados(data)
    data = ValoresNulos(data)
    Formato(data)
    Outliers(data)
    
    return data
    
    