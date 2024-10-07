import pandas as pd 

vendas_df = pd.read_excel("Vendas.xlsx")
vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")
gerentes_df = pd.read_excel("Gerentes.xlsx")

#Ler dados e filtrar dentro das tabelas
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja']=='Norte Shopping',['ID Loja', 'Produto','Quantidade']]
#print(vendas_norteshopping_df)
#print(vendas_df.loc[10,'Produto'])

transacoes_loja = vendas_df['ID Loja'].value_counts()
#print(transacoes_loja)

faturamento_produtos = vendas_df[['Produto','Valor Final']].groupby('Produto').sum()
#print(faturamento_produtos)

vendas_df = vendas_df._append(vendas_dez_df)
vendas_df = vendas_df.merge(gerentes_df)

vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05
#print(vendas_df)

vendas_df.loc[:,'Imposto'] = 0  #Ainda não definido os impostos
#print(vendas_df)

print(vendas_df)
