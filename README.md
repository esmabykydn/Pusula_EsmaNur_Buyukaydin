ESMA NUR BÜYÜKAYDIN
esmabykydn@gmail.com

Veri Keşfi ve Ön İşleme Özeti

1. Veri Keşfi

İlk olarak veri setinin yapısını inceledik. Veri setinde [satır sayısı] gözlem ve [sütun sayısı] sütun bulunuyor. Sütunlar arasında sayısal ve kategorik değişkenler yer alıyor. Sayısal sütunlar arasında “Yaş” ve “Tedavi Süresi” gibi değişkenler bulunurken, “Cinsiyet” gibi kategorik değişkenler de mevcut.

Eksik değerleri kontrol ettik ve bazı sütunlarda eksik veri olduğunu gözlemledik. Bu eksik veriler daha sonra uygun yöntemlerle dolduruldu.

Veri dağılımını anlamak için histogramlar oluşturduk. Sayısal değişkenlerin dağılımları, verinin genel eğilimini ve olası uç değerleri görmemizi sağladı. Cinsiyet gibi kategorik değişkenlerin dağılımını ise countplot ile inceledik; bu sayede erkek ve kadın gözlemlerinin sayısını kolayca görebildik.

Sayısal değişkenler arasındaki ilişkiyi scatter plot ve korelasyon matrisi ile inceledik. Özellikle “Yaş” ve “Tedavi Süresi” arasındaki ilişkiyi görselleştirdik ve veri setindeki değişkenlerin birbirleriyle olan bağlantılarını gözlemledik.

2. Veri Ön İşleme

EDA sürecinden sonra veriyi modellemeye hazırlamak için çeşitli ön işleme adımları uyguladık:

Sayısal ve Kategorik Sütunların Ayrılması:
Sayısal ve kategorik değişkenler ayrılarak farklı işlemler uygulamak mümkün oldu.

Eksik Değerlerin Doldurulması:

Sayısal sütunlarda eksik değerler medyan ile dolduruldu.

Kategorik sütunlarda eksik değerler ise en sık görülen değerle tamamlandı.

Sayısal Verilerin Standardize Edilmesi:
Sayısal veriler StandardScaler ile ölçeklendirildi. Böylece değişkenler aynı ölçeğe getirilerek modellemelerde tutarlılık sağlandı.

Kategorik Verilerin Dönüştürülmesi:
Kategorik değişkenler OneHotEncoder ile sayısal forma dönüştürüldü. Bu sayede modeller kategorik değişkenleri de anlayabilecek hale geldi.

3. Sonuç

Sonuç olarak veri seti, eksik değerler doldurulmuş, sayısal değişkenler ölçeklendirilmiş ve kategorik değişkenler sayısal formata çevrilmiş olarak modellemeye hazır hale getirildi. EDA sürecinde veri dağılımları, değişkenler arası ilişkiler ve olası anormallikler gözlemlenmiş oldu.

Eksik değerler giderildi, sayısal veriler standartlaştırıldı, kategorik veriler kodlandı.




