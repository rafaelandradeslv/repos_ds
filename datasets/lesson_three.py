import pandas as pd

# Launch Application
df = pd.read_csv('kc_house_data.csv')
print(df)
#________________________________________________________________________________________#
# Question one: Crie uma nova coluna chamada "dormitory_type"
    # 1.1 - Se o valor da coluna "bedrooms" for igual à 1 => "studio"
    # 1.2 - Se o valor da coluna 'bedrooms' for igual a 2 => 'apartament'
    # 1.3 - Se o valor da coluna 'bedrooms' for maior que 2 => 'house'
#________________________________________________________________________________________#
    
