import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerar dados de exemplo
np.random.seed(42)  # Para reprodutibilidade

num_clients = 1000

data = {
    'Client_ID': range(1, num_clients + 1),
    'Age': np.random.randint(18, 70, size=num_clients),
    'Income': np.random.randint(2000, 10000, size=num_clients),
    'Interest_Level': np.random.randint(1, 6, size=num_clients)  # 1 a 5 (1: baixo interesse, 5: alto interesse)
}  

df = pd.DataFrame(data)

# Estatísticas descritivas
print(df.describe())

# Visualizar a distribuição de interesse dos clientes
plt.figure(figsize=(10, 6))
sns.histplot(df['Interest_Level'], bins=5, kde=True)
plt.title('Distribuição do Nível de Interesse dos Clientes')
plt.xlabel('Nível de Interesse')
plt.ylabel('Número de Clientes')
plt.show()

# Filtrar clientes com alto interesse (nível 4 ou 5) e renda acima de 5000
high_interest_clients = df[(df['Interest_Level'] >= 4) & (df['Income'] > 5000)]

print(high_interest_clients)

high_interest_clients.to_csv('high_interest_clients.csv', index=False)



