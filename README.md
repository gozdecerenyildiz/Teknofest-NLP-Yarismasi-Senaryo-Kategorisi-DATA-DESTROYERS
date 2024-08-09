# Teknofest2024 Türkçe Doğal Dil İşleme Yarışması   -Senaryo Kategorisi-  Takım: DATA DESTROYERS
**Takım Adı:** DATA DESTROYERS  
**Başvuru Id:** 2290170  
![image](https://github.com/user-attachments/assets/4505e9fa-d976-4fc8-8405-8e172ee0211d)

## Ekibimiz
![image](https://github.com/user-attachments/assets/6f053871-50cf-468c-bce0-4f456586f187)

## 📜 Projenin Tanımı
Bu FastAPI projesi, Teknofest2024 Türkçe Doğal Dil İşleme Yarışması Senaryo Kategorisi için Data Destroyers Ekibi tarafından, Turkcell final senaryosu kapsamında; belirli bir metin girdisine dayalı olarak varlık (entity) tanıma ve duygu (sentiment) analizi yapan bir API hizmeti sunmak amacıyla yapılmıştır. Yapmış olduğumuz bu proje, kullanıcıdan bir metin alır, bu metin üzerinde analiz yapar ve belirli varlıkları tanıyarak her bir varlık için duygu analizini gerçekleştirir.
Özellikle sosyal medya, müşteri geri bildirimleri veya herhangi bir metin tabanlı veri kaynağındaki varlıkların (şirket isimleri, ürünler, hizmetler vb.) tespit edilmesi ve bu varlıklarla ilgili olumlu, olumsuz veya nötr duyguların sınıflandırılması hedeflenmektedir.

## 🎯 Projenin Amacı
- **Varlık Tanıma (Entity Recognition):** Metin içerisindeki belirli kişi, yer, organizasyon vb. varlıkları tanımlamak.
- **Duygu Analizi (Sentiment Analysis):** Tanımlanan her bir varlık için metindeki duygusal tonu (olumlu, olumsuz, nötr) belirlemek.

## 🚀 Projemizin Sağladığı Çözümler
- Kullanıcıların metinlerinde yer alan varlıkların (entitelerin) doğru bir şekilde tanınması.Tanınan her varlık için duygu analizi yapılarak, varlığın taşıdığı duygunun belirlenmesi (olumlu, olumsuz, nötr).

- Proje FastAPI framework'ü kullanılarak bir API olarak sunulmaktadır. Bu API'ye gönderilen metinler üzerinde varlık tanıma ve duygu analizi gerçekleştirilir ve sonuçlar JSON formatında döndürülür.

- Bu proje, varlık tanıma (NER) ve duygu analizi (sentiment analysis) için bir FastAPI uygulaması sunar. Kullanıcılar API'ye bir metin gönderir ve sistem, metin içerisinde yer alan varlıkları tespit eder ve bu varlıkların duygu durumunu belirler. 

- Ayrıca, bu tür projeler, Türkçe dilinde veri analizi yapma kapasitesini artırarak, Türkçe'nin dijital dünya üzerindeki kullanımını ve dil teknolojileri alanındaki temsilini güçlendirmektedir.
- 
## 📂 Dosyalar

- `main.py`: Uygulamanın ana dosyası.
- `requirements.txt`: Projede kullanılan Python bağımlılıklarının listesi.
-`sentiment_data.7z` : Projede kullanılan datanın son hali
-`analiz.ipynb` : Proje modelleme aşamalarının bulunduğu jupyternotebook dosyası


## 📈 Proje Aşamaları
Proje 4 ana aşamadan oluşmaktadır:

### A) Web-Scraping ile Negatif Veri Toplama Aşamaları
- **Web-scraping kullanılarak sikayetvar.com sitesindeki Turkcell'e ait Türkçe şikayet yorumları (negatif sentiment verileri) nlp de kullanılmak üzere kategorilerine göre (cayma, superbox vb.) otomatik olarak toplanıp analiz edilebilir hale getirildi.**

#### Web Scraping Kullanılan Kütüphaneler ve Amaçları
1. **Selenium (webdriver, By, WebDriverWait, EC, ActionChains):**
   - `webdriver`: Web tarayıcısını otomatikleştirmek için kullanıldı.
   - `By`: Web sayfasındaki öğeleri bulmak için çeşitli yöntemler sağladığı için kullanıldı.
   - `WebDriverWait`, `EC`: Tanımlanmış belirli koşulların oluşmasını beklemek için kullanıldı.
   - `ActionChains`: Web sayfasında çeşitli etkileşimler (Örneğin; fare hareketleri, tıklamalar) gerçekleştirmek için kullanıldı.
2. **BeautifulSoup (BeautifulSoup):** 
   - Web sayfasının HTML içeriğini ayrıştırmak ve belirli öğeleri bulmak için kullanıldı.
3. **Urllib (urljoin):**
   - Göreceli URL'leri tam URL'lere dönüştürmek için kullanıldı.

#### Kodun İşleyişi
1. **Başlatma ve URL'leri Ziyaret Etme:**
   - WebDriver başlatılır ve sikayetvar.com sitesindeki Turkcellin kategorilerine ait  şikayet sayfaları ayrı ayrı ziyaret edilir.
2. **Veri Toplama:**
   - Her ayrı kategori ve sayfada bulunan şikayetlerin detay sayfalarına gidilir ve şikayetlerin başlıkları ve içerikleri toplanır.
3. **Verileri Düzenleme ve Kaydetme:**
   - Toplanan veriler pandas DataFrame'e dönüştürülür ve bir CSV dosyasına kaydedilir.

### B) HuggingFace ile Veri Toplama
- **Sentiment sütununa sahip Türkçe yorum verilerinin (https://huggingface.co/datasets/asparius/Turkish-Product-Review) (https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset) elde edilmesi:**

#### 📥 Veri Setini İndirme
1.  Hugging Face Datasets kütüphanesini kullanarak "asparius/Turkish-Product-Review" ve "turkish-sentiment-analysis-dataset" veri setinin eğitim bölümü şu kod ile indirilir:

train_dataset = dataset['train']

![image](https://github.com/user-attachments/assets/ce50092d-e606-456d-917c-4d168ef64c47)


### C) Verilerin Ön Temizleme İşlem Adımları
- **Web scraping ve Hugging Face Datasets ile elde edilen tüm verilerin ön temizleme işlemleri:**

- Sayıları kaldırma,
- Fazla boşlukları kaldırma,
- Türkçe durdurma işaretlerini (stopwords-tr.txt) kaldırma,
- Noktalama işaretlerini kaldırma,
- Özel karakterleri kaldırma vb. işlem adımları ile yapılır.

![WhatsApp Image 2024-08-09 at 10 03 47](https://github.com/user-attachments/assets/8f7bc47e-6e57-4cf0-b7ae-129757b54fdc)

![WhatsApp Image 2024-08-09 at 10 03 53](https://github.com/user-attachments/assets/c41a927f-c8e6-42f5-89b1-cef4183d0902)

![WhatsApp Image 2024-08-09 at 10 03 57](https://github.com/user-attachments/assets/5958de1e-0ba5-446f-83e0-29a9fd3deec3)

  
### D) Doğal Dil İşleme Süreci Adımları 
#### 1. Kullanılan Kütüphaneler
- **pandas:** CSV dosyasını okumak ve veri işlemek için kullanılır.
- **matplotlib:** Grafik çizimleri yapmak için kullanılır.
- **sklearn:** Performans metriklerini hesaplamak için kullanılır.
- **wordcloud:** Metin verilerini görselleştirmek için kullanılır. Kelime bulutu (word cloud) oluşturma amaçlıdır.
- **sklearn.model_selection.train_test_split:** Verileri eğitim ve test setlerine ayırmak için kullanılır. Model doğruluğunu değerlendirmek için gereklidir.
- **sklearn.feature_extraction.text.CountVectorizer:** Metin verilerini sayısal verilere dönüştürmek için kullanılır. Bu dönüşüm, tokenization ve sayma işlemiyle yapılır.
- **sklearn.linear_model.LogisticRegression:** Lojistik regresyon modeli oluşturmak için kullanılır. Bu model, sınıflandırma problemleri için yaygın olarak kullanılır.
- **sklearn.metrics:** Model performansını değerlendirmek için çeşitli metrikler sağlar, örneğin doğruluk, hassasiyet, kesinlik, F1 skoru gibi.
- **seaborn:** Veri görselleştirme için kullanılır ve özellikle istatistiksel grafikler oluşturmak için uygundur.
- **sklearn.naive_bayes:** Naive Bayes sınıflandırıcı modelleri oluşturmak için kullanılır.
- **sklearn.feature_extraction.text.TfidfVectorizer:** Metin verilerini sayısal verilere dönüştürmek için kullanılır. Term Frequency-Inverse Document Frequency (TF-IDF) yöntemini kullanır.
- **joblib:** Modeli seri hale getirmek (serialize) ve kaydetmek için kullanılır. Eğitilen modellerin yeniden kullanılabilir hale getirilmesini sağlar.
  
#### 2. Veriyi Okuma
- Pandas kütüphanesi, ön temizleme yapılmış verilerin CSV dosyasından yüklenmesi için kullanıldı.

#### 3. Metin ve Etiketlerin Hazırlanması
- Modelin anlayabileceği bir formatta metin verileri ve etiketler hazırlandı. astype(str) ve astype(int) ile tip dönüşümleri yapılarak veriler listelere dönüştürüldü.

#### 4. Vektörizasyon Teknikleri
- Bu projede vektörizasyon işlemi CountVectorizer ve TfidfVectorizer kullanılarak gerçekleştirilmiştir:

**CountVectorizer:** Metin içerisindeki her kelimeyi bir token olarak alır ve bu kelimelerin dokümandaki sayısını hesaplar. Bu yöntem, metni kelime sayılarıyla temsil eden bir matrise dönüştürür.
- 1-Gram: Her bir kelime için vektörler oluşturulmuştur.
- 2-Gram: 1 ve 2 kelimelik kombinasyonlar için vektörler oluşturulmuştur (N-Gram yöntemi).
**TfidfVectorizer:*** CountVectorizer'a benzer şekilde metni kelime tokenlerine ayırır, ancak bu kelimelerin önemini de dikkate alır. TF-IDF skoru, bir kelimenin bir dokümandaki önemini hesaplamak için kullanılır. Daha sık geçen ancak çok yaygın olmayan kelimelere daha yüksek ağırlık verilir.
- 1-Gram TF-IDF: Tek kelimelik tokenlar için TF-IDF vektörleri oluşturulmuştur.
- 2-Gram TF-IDF: 1 ve 2 kelimelik kombinasyonlar için TF-IDF vektörleri oluşturulmuştur.
Bu iki teknik, metin verilerinin makine öğrenimi modelleri için uygun hale getirilmesini sağlar. Tokenization, kelime öbeklerini **(n-grams)** de hesaba katarak, daha anlamlı bir metin temsili oluşturulur.

#### 5.Model Kurulumu ve Eğitimi
**Logistic Regression:**
* LogisticRegression modeli kullanılarak sınıflandırma modeli oluşturulmuş ve eğitim verileri ile eğitilmiştir.
* Hem kelime bazlı vektörlerle (CountVectorizer kullanarak) hem de N-Gram vektörleriyle (N-Gram CountVectorizer) modeller eğitilmiştir.
* Ayrıca, TF-IDF vektörleri ile Logistic Regression modelleri de oluşturulmuştur.
**Naive Bayes:**
* MultinomialNB ve BernoulliNB algoritmaları kullanılarak Naive Bayes modelleri eğitilmiştir.
* Bu modeller, hem kelime vektörleri hem de N-Gram vektörleri ile eğitilmiş ve test edilmiştir.
#### 6.Model Performans Değerlendirmesi
* Karışıklık Matrisi (Confusion Matrix):
* Modellerin performansı, karışıklık matrisi kullanılarak değerlendirilmiştir. Bu matriste, modelin tahmin ettiği ve gerçek sınıflar karşılaştırılmıştır.
* Metrikler: Doğruluk, hassasiyet, kesinlik, F1 skoru gibi metrikler hesaplanmış ve sonuçlar görselleştirilmiştir.
#### 7.Modelin Kaydedilmesi
* Eğitilen modeller, ileride kullanılmak üzere joblib kütüphanesi ile kaydedilmiştir. Ayrıca, vektörizasyon işlemleri için kullanılan CountVectorizer da kaydedilmiştir.
* Model ve vektörizer birlikte kaydedilerek, tahmin işlemleri için tekrar kullanılabilir hale getirilmiştir.
* Bu adımlar, metin verileri üzerinde gerçekleştirilen sınıflandırma işleminin tam iş akışını ve kullanılan yöntemleri kapsamaktadır.

#### 8.Performans Metriklerinin Hesaplanması
- Kurulan Derin Öğrenme Modelinin performansının değerlendirilmesi için Sklearn Metrikleri(Doğruluk, precision, recall, F1-score, Confisuon Matrix ve ROC AUC) hesaplandı.
  
#### 9.Performans Metriklerinin Grafiğinin Çizdirilmesi
- Eğitim ve validasyon kayıpları ile doğruluklarını görselleştirmek, modelin performansını ve öğrenme sürecini anlamamıza yardımcı olacağı için daha sonra sunum dosyasında kullanmak ve değerlendirmek üzere kaydedildi.

![image](https://github.com/user-attachments/assets/be0e968b-0b1a-40dc-bcc5-cacbc3843510)

### E) 🖥 FastAPI (main.py) İşleyişi
#### 📜 1. Metin Girdisi Alma
- Kullanıcı, bir metin girdisi gönderir. Bu metin, içinde çeşitli varlıklar (örneğin, şirket isimleri, platformlar) içerebilir.

#### 💬 2. Varlık Tanıma ve Duygu Analizi
- Gönderilen metin üzerinde model çalıştırılarak varlıklar tanımlanır ve her bir varlık için duygu analizi yapılır.

#### 📈 3.Sonuçları Döndürme
- Tanımlanan varlıklar ve bunlara ilişkin duygu analizi sonuçları (pozitif, negatif, nötr) kullanıcıya JSON formatında geri döndürülür.

### F) 📊 SONUÇLAR-ARAYÜZ
![Ekran görüntüsü 2024-08-09 092035](https://github.com/user-attachments/assets/6dc06251-728c-452d-a23b-afe52312988f)
![Ekran görüntüsü 2024-08-09 092041](https://github.com/user-attachments/assets/8ca8d80b-3dab-479d-80ca-d124859b75f3)
![Ekran görüntüsü 2024-08-09 092111](https://github.com/user-attachments/assets/f025e7f2-ffd9-4ca6-938a-0c50e142c67e)
![Ekran görüntüsü 2024-08-09 092623](https://github.com/user-attachments/assets/e2c4f594-51e9-40d7-a211-a023246ef91a)
![Ekran görüntüsü 2024-08-09 093512](https://github.com/user-attachments/assets/8f751805-0fe2-4f2a-9208-5536c8a72893)
![Ekran görüntüsü 2024-08-09 093528](https://github.com/user-attachments/assets/6a7ea041-1ead-47c8-829c-fd996a82a6cb)
![Ekran görüntüsü 2024-08-09 091910](https://github.com/user-attachments/assets/ea5a2bc7-7ac3-4ed0-af99-10074cadfd8a)
![Ekran görüntüsü 2024-08-09 091921](https://github.com/user-attachments/assets/02b5a838-f74c-440f-b681-b72c91d1f3e9)
![Ekran görüntüsü 2024-08-09 091941](https://github.com/user-attachments/assets/2307e3f8-2f22-47f6-8e62-0b95ee3cda66)
![Ekran görüntüsü 2024-08-09 091949](https://github.com/user-attachments/assets/dfc7c2cc-b75c-4e4b-bc73-d02de8e5aee1)


### G) 🔧 Kurulum

1. Projeyi klonlayın:

    ```bash
    git clone https://github.com/sevimonline/Musteri-Hizmetleri-Cozumleri-Turkce-Platformu-DATA-DESTROYERS](https://github.com/gozdecerenyildiz/Teknofest-NLP-Yarismasi-Seneryo-Kategorisi-DATA-DESTROYERS.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd Teknofest-NLP-Yarismasi-Seneryo-Kategorisi-DATA-DESTROYERS
    ```

3. Gerekli paketleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Uygulamayı başlatın:

    ```bash
    python -m uvicorn main:app --reload
    ```

5. Tarayıcınızda `http://localhost:8000` adresine gidin ve uygulamayı kullanmaya başlayın.

### 👥 İletişim

- LinkedIn: [Berke Sevim](https://www.linkedin.com/in/berke-sevim-1565161a2/)
- LinkedIn: [Gözde Ceren Yıldız](https://www.linkedin.com/in/gözde-ceren-yıldız/)
- LinkedIn: [Büşra Sulukan](https://www.linkedin.com/in/büşra-sulukan-82299a177/)

### 📄 Lisans

Bu proje Apache 2.0 Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.





