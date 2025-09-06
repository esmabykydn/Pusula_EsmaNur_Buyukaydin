ESMA NUR BÜYÜKAYDIN
esmabykydn@gmail.com

Veri Keşfi ve Ön İşleme Özeti

1. Veri Yükleme

"Talent_Academy_Case_DT_2025.xlsx" dosyası Pandas ile yüklendi.

İlk 5 satır, sütun isimleri, veri tipleri ve temel istatistikler incelendi.

Eksik değerler tespit edildi.

2. Veri Görselleştirme

Histogramlar: Sayısal sütunların dağılımı.

Countplot: "Cinsiyet" dağılımı.

Scatterplot: "Yaş" ve "TedaviSuresi" ilişkisi.

Korelasyon matrisi: Sayısal değişkenler arasındaki korelasyon.

3. Veri Ön İşleme

Sütunların ayrılması

Sayısal: int64, float64

Kategorik: object, category

Eksik değerlerin doldurulması

Sayısal: Medyan

Kategorik: En sık değer

Sayısal verilerin ölçeklendirilmesi

StandardScaler ile standartlaştırıldı.

Kategorik verilerin kodlanması

OneHotEncoder ile sayısal hale getirildi.

Dummy değişken tuzağı önlendi (drop='first').

4. Sonuç

Veri temizlendi ve modellemeye hazır.

Eksik değerler giderildi, sayısal veriler standartlaştırıldı, kategorik veriler kodlandı.

Son veri boyutu: (satır sayısı, sütun sayısı)
