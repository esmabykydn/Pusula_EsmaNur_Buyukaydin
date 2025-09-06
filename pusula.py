import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx")

print("Veri boyutu:", df.shape)
print("\nSütunlar ve veri tipleri:")
df.info()  

print("\nTemel istatistikler:\n", df.describe())
print("\nEksik değerler:\n", df.isnull().sum())


# Histogramlar
df.hist(figsize=(12, 10), bins=20)
plt.show()


sns.countplot(data=df, x="Cinsiyet") 
plt.show()


#İki değişken arasındaki ilişkileri görselleştir
# Scatter plot örneği
sns.scatterplot(data=df, x='Yas', y='TedaviSuresi')
plt.show()


#Korelasyon matrisi ve heatmap

numerik_df = df.select_dtypes(include=['int64', 'float64'])

# Korelasyon matrisi
sns.heatmap(numerik_df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Sayısal ve kategorik sütunları ayırma
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Eksik değerleri doldurma
df[num_cols] = SimpleImputer(strategy='median').fit_transform(df[num_cols])
df[cat_cols] = SimpleImputer(strategy='most_frequent').fit_transform(df[cat_cols])

#Kategorik verileri sayısala çevirme (OneHotEncoder)
ohe = OneHotEncoder(sparse_output=False, drop='first')  # eski 'sparse' yerine 'sparse_output'
encoded = ohe.fit_transform(df[cat_cols])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(cat_cols))
df = pd.concat([df.drop(cat_cols, axis=1), encoded_df], axis=1)

# Sayısal verileri standardize etme
df[num_cols] = StandardScaler().fit_transform(df[num_cols])

# Temizlenmiş veri hazır
print("Veri temizlendi ve modellemeye hazır.")
print("Son veri boyutu:", df.shape)

