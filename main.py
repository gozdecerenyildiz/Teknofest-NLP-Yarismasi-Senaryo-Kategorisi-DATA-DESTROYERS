from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import spacy

# FastAPI uygulaması oluşturma
app = FastAPI()

# Model ve vektörizeri yükleme
model, vectorizer = joblib.load('logistic_regression_model_with_vectorizer.pkl')

# spaCy çok dilli modeli yükleme
nlp = spacy.load('xx_ent_wiki_sm')

# İstek verisini tanımlama
class TextItem(BaseModel):
    text: str

@app.post("/predict")
async def predict(item: TextItem):
    # Gelen metni vektörizer ile dönüştürme
    text_vector = vectorizer.transform([item.text])
    # Model ile tahmin yapma
    prediction = model.predict(text_vector)
    
    # Tüm metin için sentiment tahmini yapma
    sentiment = "olumlu" if prediction[0] == 0 else "olumsuz" if prediction[0] == 1 else "nötr"

    # Entity çıkarma
    doc = nlp(item.text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Sonuçları oluşturma
    results = []
    entity_list = []
    for ent_text, ent_label in entities:
        if ent_text not in entity_list:
            entity_list.append(ent_text)
        results.append({
            "entity": ent_text,
            "sentiment": sentiment
        })

    # Sonuç formatı
    result = {
        "entity_list": entity_list,
        "results": results
    }
    
    return result

# Hızlı test için kök endpointi
@app.get("/")
def read_root():
    return {"message": "Teknofest 2024, Türkçe Doğal Dil İşleme Yarışması-Senaryo Kategorisine Hoşgeldiniz!"}
