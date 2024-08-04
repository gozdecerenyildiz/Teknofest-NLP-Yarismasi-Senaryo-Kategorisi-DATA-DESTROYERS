# #Teknofest2024 Türkçe Doğal Dil İşleme Yarışması   -Senaryo Kategorisi-  Takım: DATA DESTROYERS
**Takım Adı:** DATA DESTROYERS  
**Başvuru Id:** 2290170  

## 📜 Projenin Tanımı
Bu FastAPI projesi, Teknofest2024 Türkçe Doğal Dil İşleme Yarışması Senaryo Kategorisi için Data Destroyers Ekibi tarafından, Turkcell final senaryosu kapsamında; belirli bir metin girdisine dayalı olarak varlık (entity) tanıma ve duygu (sentiment) analizi yapan bir API hizmeti sunmak amacıyla yapılmıştır. Yapmış olduğumuz bu proje, kullanıcıdan bir metin alır, bu metin üzerinde analiz yapar ve belirli varlıkları tanıyarak her bir varlık için duygu analizini gerçekleştirir.

## 🎯 Projenin Amacı
- **Varlık Tanıma (Entity Recognition):** Metin içerisindeki belirli kişi, yer, organizasyon vb. varlıkları tanımlamak.
- **Duygu Analizi (Sentiment Analysis):** Tanımlanan her bir varlık için metindeki duygusal tonu (olumlu, olumsuz, nötr) belirlemek.

## 📂 Dosyalar

- `main.py`: Uygulamanın ana dosyası.
- `requirements.txt`: Projede kullanılan Python bağımlılıklarının listesi.
-
-
-


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

#### Veri Setini İndirme
1.  Hugging Face Datasets kütüphanesini kullanarak "asparius/Turkish-Product-Review" ve "turkish-sentiment-analysis-dataset" veri setinin eğitim bölümü şu kod ile indirilir:

train_dataset = dataset['train']

   ------------ VERİ SETİ HAKKINDA BİLGİ GÖRSELİ BURAYA EKLENECEK ( KAÇ ADET DATA, KAÇI NÖTR,KAÇI POZİTİF,KAÇI NEGATİF VB) ------- 

### C) Verilerin Ön Temizleme İşlem Adımları
- **Web scraping ve Hugging Face Datasets ile elde edilen tüm verilerin ön temizleme işlemleri:**

- Sayıları kaldırma,
- Fazla boşlukları kaldırma,
- Türkçe durdurma işaretlerini (stopwords-tr.txt) kaldırma,
- Noktalama işaretlerini kaldırma,
- Özel karakterleri kaldırma vb. işlem adımları ile yapılır.

  ----------- VERİ SETİ WORD CLOUD GÖRSELİ VE NLP GÖRSELLERİ BURAYA EKLENECEK------------
  
### D) Doğal Dil İşleme Süreci Adımları - Derin Öğrenme
#### 1. Kullanılan Kütüphaneler
- pandas: CSV dosyasını okumak ve veri işlemek için kullanılır.
- tensorflow: Model eğitimi ve veri işleme için kullanılır.
- matplotlib: Grafik çizimleri yapmak için kullanılır.
- sklearn: Performans metriklerini hesaplamak için kullanılır.
- transformers: BERT modelini ve tokenizer'ı yüklemek için kullanılır.
#### 2. Veriyi Okuma
- Pandas kütüphanesi, ön temizleme yapılmış verilerin CSV dosyasından yüklenmesi için kullanıldı.

#### 3. Metin ve Etiketlerin Hazırlanması
- Modelin anlayabileceği bir formatta metin verileri ve etiketler hazırlandı. astype(str) ve astype(int) ile tip dönüşümleri yapılarak veriler listelere dönüştürüldü.

#### 4. Tokenizasyon
- BertTokenizer, metinlerin belirli bir formatta token'lara dönüştürülerek işlenmesi (metin tokenizasyonu) için kullanıldı. Bu tokenizasyon işlemi, metinlerin modelin anlayabileceği input_ids ve attention_mask gibi tensörlere dönüştürülmesini sağladı. truncation ve padding parametreleri, metinlerin belirli bir uzunlukta olmasını ve gerekli dolguların yapılmasını sağladı.

#### 5. TensorFlow Veri Kümesi Oluşturma
- Verilerin TensorFlow veri kümesi formatına dönüştürülmesi, modelin eğitim sürecinde verilerin verimli bir şekilde işlenmesini sağlar. Verileri eğitim ve validasyon kümelerine ayırmak, modelin performansını değerlendirmek için önemli olduğundan TensorFlow veri kümesi oluşturuldu.

#### 6. Öğrenme Oranı Zamanlayıcısı ve Optimizasyon
- PolynomialDecay, öğrenme oranının zamanla azalmasını sağlayarak modelin eğitim sürecinde daha stabil hale gelmesine yardımcı olduğu için kullanıldı. Adam optimizasyon algoritması ise gradyan inişini hızlandırarak daha verimli hale getirdiği için derin öğrenme modelinde kullanıldı.

#### 7. Eğitim ve Validasyon Adımları İçin Fonksiyonlar
- tf.GradientTape kullanarak gradyanları hesaplayan ve optimizer ile modelin ağırlıklarını güncelleyen, @tf.function dekoratörü ile TensorFlow grafik modunda çalışarak performansı artıran fonksiyonlar derin öğrenme modeli işlem adımlarında kullanıldı.

#### 8. Eğitim Döngüsü
- Eğitim döngüsü, modelin belirli sayıda epoch boyunca eğitim ve validasyon adımlarını tekrarlamasını sağlar. Her epoch'ta modelin performansı değerlendirilir ve kaydedilir. En uygun Epoch bulma algoritması kullanılarak derin öğrenme modeli için Epoch sayısı 3 olarak belirlendi.

#### 9. Model Kurma
-Yukarıda bahsedilen işlem adımları ile derin öğrenme modeli kuruldu.

#### 10. Modeli Kaydetme
- Eğitilmiş modelin ve tokenizer'ın FastAPI arayüzünde kullanmak için kaydedildi.

#### 11. Performans Metriklerinin Hesaplanması
- Kurulan Derin Öğrenme Modelinin performansının değerlendirilmesi için Sklearn Metrikleri(Doğruluk, precision, recall, F1-score, Confisuon Matrix ve ROC AUC) hesaplandı.
  
#### 12. Performans Metriklerinin Grafiğinin Çizdirilmesi
- Eğitim ve validasyon kayıpları ile doğruluklarını görselleştirmek, modelin performansını ve öğrenme sürecini anlamamıza yardımcı olacağı için daha sonra sunum dosyasında kullanmak ve değerlendirmek üzere kaydedildi.

- ----------- PERFORMANS METRİĞİ VE GRAFİKLERİ BURAYA EKLENECEK --------------------------------

### E) 🖥 FastAPI (main.py) İşleyişi
#### 1. Metin Girdisi Alma
- Kullanıcı, bir metin girdisi gönderir. Bu metin, içinde çeşitli varlıklar (örneğin, şirket isimleri, platformlar) içerebilir.

#### 2. Varlık Tanıma ve Duygu Analizi
- Gönderilen metin üzerinde model çalıştırılarak varlıklar tanımlanır ve her bir varlık için duygu analizi yapılır.

#### 3. Sonuçları Döndürme
- Tanımlanan varlıklar ve bunlara ilişkin duygu analizi sonuçları (pozitif, negatif, nötr) kullanıcıya JSON formatında geri döndürülür.

-
-
-
-
-
-
------------ YAPILAN DİĞER İŞLEM ADIMLARI DETAYLANDIRILACAK VE FASTAPI ARAYÜZ ÇIKTILARI BURAYA EKLENECEK --------------------


## F) 🔧 Kurulum

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
    uvicorn main:app --reload
    ```

5. Tarayıcınızda `http://localhost:8000` adresine gidin ve uygulamayı kullanmaya başlayın.

## 👥 İletişim

- LinkedIn: [Berke Sevim](https://www.linkedin.com/in/berke-sevim-1565161a2/)
- LinkedIn: [Gözde Ceren Yıldız](https://www.linkedin.com/in/gözde-ceren-yıldız/)
- LinkedIn: [Büşra Sulukan](https://www.linkedin.com/in/büşra-sulukan-82299a177/)

## 📄 Lisans

Bu proje Apache 2.0 Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.





