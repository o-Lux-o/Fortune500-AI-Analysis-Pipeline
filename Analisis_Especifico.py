import pandas as pd


def Analytics(ruta: str):
    
    data = pd.read_csv(ruta)

    def Top_IAs(data):
        IAsUseYes = data[data['Uses_AI'] == 'Yes']

        TopIAs = IAsUseYes['Use_Case'].value_counts().sort_values(ascending=False)
        TopIA = IAsUseYes['Use_Case'].value_counts().idxmax()
        print(f'\n\nEstas son las Ias mas usadas:\n\n{TopIAs}\n\nPero la ganadora es: \n\n{TopIA}\n\n')

    NewValuesEmployee_Size = {
        'Enterprise' : 1,
        'SME' : 0
    }

    def Correspondencia(data):
        
        data['Employee_Size'] = data['Employee_Size'].map(NewValuesEmployee_Size)

        correspondencia = data['Employee_Size'].corr(data['AI_Maturity_Score'], method='pearson')

        print(f'\n\nLa correspondencia entre el tamaño de la empresa y el puntaje de madurez de IA es: {correspondencia}\n\n')

    def ROIEnterprise(data):
        EnterpriseROI = data[(data['AI_ROI_Percent'] > 30) & (data['Employee_Size'] == 1)]
        EnterpriseROI.to_csv("high_roi_enterprise.csv", index=False)
        print(f'\n\n Estas son todas las "Enterprise" con un "Porcentaje ROI" > 30 \n\n{EnterpriseROI}\n\nDatos guardados en "high_roi_enterprise.csv"\n\n')

    Top_IAs(data)
    Correspondencia(data)
    ROIEnterprise(data)
    
