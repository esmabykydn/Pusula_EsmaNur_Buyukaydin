import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx")

print("İlk 5 satır:", df.head())
print("Veri boyutu:", df.shape)
print("Sütun isimleri:", df.columns)
print("\nSütunlar ve veri tipleri:")
df.info()  
print("\nTemel istatistikler:\n", df.describe())
print("Veri tipleri:", df.dtypes) 
print("\nEksik değerler:\n", df.isnull().sum())


# Histogram grafiği
df.hist(figsize=(12, 10), bins=20)
plt.show()


sns.countplot(data=df, x="Cinsiyet") 
plt.show()

# Scatter plot
sns.scatterplot(data=df, x='Yas', y='TedaviSuresi')
plt.show()

# Korelasyon matrisi
numerik_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numerik_df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Sayısal ve kategorik sütunları ayırma
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Eksik değerleri doldurma
df[num_cols] = SimpleImputer(strategy='median').fit_transform(df[num_cols])
df[cat_cols] = SimpleImputer(strategy='most_frequent').fit_transform(df[cat_cols])

# Sayısal verileri standardize etme
df[num_cols] = StandardScaler().fit_transform(df[num_cols])

# Kategorik verileri OneHotEncoder ile dönüştürme
ohe = OneHotEncoder(sparse_output=False, drop='first')
encoded = ohe.fit_transform(df[cat_cols])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(cat_cols), index=df.index)

# Kategorik sütunları çıkarma ve yeni sütunları ekleme
df = pd.concat([df.drop(cat_cols, axis=1), encoded_df], axis=1)

# Sonuç
print("Veri temizlendi ve modellemeye hazır.")
print("Son veri boyutu:", df.shape)


