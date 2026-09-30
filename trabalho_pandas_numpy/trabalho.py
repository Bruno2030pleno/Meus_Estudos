import numpy as np
import pandas as pd

# trabalho para a faculdade
# fiz oque deu, rsrsrsrs
df = pd.read_csv("dados.csv", sep=";", engine="python")
print("=== Passo 9.1: Informações gerais do conjunto original ===")

df.info()
print("\n=== Passo 9.2: Primeiras 5 linhas ===")
print(df.head())
print("\n=== Passo 9.2: Últimas 5 linhas ===")
print(df.tail())
# ------------------------------------------------------

df_limpo = df.copy()
df_limpo["Calories"] = df_limpo["Calories"].fillna(0)
print("\n=== Passo 12.2: Conferencia da alteracao na coluna 'Calories' ===")
print(df_limpo[["ID", "Calories"]].iloc[[18, 28]])  
# --------------------------------------------------------------------------------
df_limpo["Date"] = df_limpo["Date"].astype(str).str.replace("'", "").str.strip()
df_limpo["Date"] = df_limpo["Date"].replace(["1900/01/01", "nan", "NaN"], np.nan)
df_limpo["Date"] = df_limpo["Date"].replace("20201226", "2020/12/26")
df_limpo["Date"] = pd.to_datetime(
    df_limpo["Date"], format="%Y/%m/%d", errors="coerce"
)
print("\n=== Passo 23: DataFrame apos tratamento das datas ===")
print(df_limpo)
df_limpo = df_limpo.dropna(subset=["Date"])
print("\n=== Passo 27: DataFrame Final Limpo e Tratado ===")
print(df_limpo.to_string())
print("\n=== Informacoes Gerais do DataFrame Trata ===")
df_limpo.info()