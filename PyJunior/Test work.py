import pandas as pd
import numpy as np
import statsmodels.api as sm

# Загрузка данных о цене ETHUSDT и BTCUSDT
eth_data = pd.read_csv('ethusdt_data.csv')
btc_data = pd.read_csv('btcusdt_data.csv')

# Объединение данных в один DataFrame
data = pd.merge(eth_data, btc_data, on='timestamp', how='inner')

# Выбор регрессора и зависимой переменной
X = data['close_btcusdt']
y = data['close_ethusdt']

# Добавление константы
X = sm.add_constant(X)

# Создание модели линейной регрессии
model = sm.OLS(y, X)

# Обучение модели
results = model.fit()

# Вывод результатов модели
print(results.summary())
