from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import spacy

app = FastAPI()

model, vectorizer = joblib.load('logistic_regression_model_with_vectorizer.pkl')

nlp = spacy.load('xx_ent_wiki_sm')


class TextItem(BaseModel):
    text: str

@app.post("/predict")
async def predict(item: TextItem):

    text_vector = vectorizer.transform([item.text])
    prediction = model.predict(text_vector)
    
    sentiment = "olumlu" if prediction[0] == 0 else "olumsuz" if prediction[0] == 1 else "nötr"

    doc = nlp(item.text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    results = []
    entity_list = []
    for ent_text, ent_label in entities:
        if ent_text not in entity_list:
            entity_list.append(ent_text)
        results.append({
            "entity": ent_text,
            "sentiment": sentiment
        })

    result = {
        "entity_list": entity_list,
        "results": results
    }
    
    return result

@app.get("/")
def read_root():
    return {"message": "Teknofest 2024, Türkçe Doğal Dil İşleme Yarışması-Senaryo Kategorisine Hoşgeldiniz!"}
