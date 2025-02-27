import pandas as pd


data_url = "https://raw.githubusercontent.com/gazzola/pima_dataset/main/diabetes.csv"
df = pd.read_csv(data_url)


print(" Primeiras 5 linhas:")
print(df.head())
print("\n Informações gerais:")
print(df.info())
print("\n Estatísticas descritivas:")
print(df.describe())


print("\n Dimensões do DataFrame")
print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")


colunas_novas = {
    "Pregnancies": "Gravidez",
    "Glucose": "Glicose",
    "BloodPressure": "Pressao_Sanguinea",
    "SkinThickness": "Espessura_Pele",
    "Insulin": "Insulina",
    "BMI": "IMC",
    "DiabetesPedigreeFunction": "Funcao_Historico_Diabetes",
    "Age": "Idade",
    "Outcome": "Resultado"
}
df.rename(columns=colunas_novas, inplace=True)
print("\n Novos nomes das colunas")
print(df.columns)


desc = df.describe()
exp = {}

for coluna in df.columns:
    min_val = desc.loc["min", coluna]
    if coluna in ["Glicose", "Pressao_Sanguinea", "Espessura_Pele", "Insulina", "IMC"] and min_val == 0:
        exp[coluna] = "Analisar valor min. zero"
    else:
        exp[coluna] = "OK"

print("\n Análise de valores mínimos")
print(exp)