from fastapi import FastAPI
from pydantic import BaseModel
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import stanza
import nltk

# NLTK ve Stanza için gerekli indirmeler
nltk.download('punkt')
stanza.download('tr')

# Stanza Türkçe pipeline'ı oluşturma
nlp = stanza.Pipeline('tr', processors='tokenize,mwt,pos,lemma,depparse,ner')

# FastAPI uygulamasını başlatma
app = FastAPI()

# Model ve tokenizer'ı yükleyin
model_path = 'sentiment_model'
model = TFBertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

class Comment(BaseModel):
    text: str

@app.post("/analyze/")
async def analyze(comment: Comment):
    # Sentiment Analizi
    inputs = tokenizer(comment.text, return_tensors='tf', max_length=128, padding='max_length', truncation=True)
    outputs = model(inputs)
    scores = outputs[0][0].numpy()
    sentiment = 'positive' if scores[1] > scores[0] else 'negative'
    
    # Entity Extraction
    doc = nlp(comment.text)
    entities = [ent.text for ent in doc.ents]
    
    # Burada her bir entity'nin sentiment analizini yapmalıyız
    # Bu örnek basit bir yaklaşım sunar; gerçek uygulamada daha sofistike yöntemler gerekebilir.
    entity_list = []
    results = []
    for ent in entities:
        # Örnek olarak, her bir entity'nin sentimentini belirliyoruz
        # Bu kısımda gerçek analizlerinizi gerçekleştirin
        entity_sentiment = 'nötr'
        if 'olumsuz' in sentiment:  # Örneğin, genel sentiment'e bağlı olarak entity'nin sentimentini belirliyoruz
            entity_sentiment = 'olumsuz'
        elif 'olumlu' in sentiment:
            entity_sentiment = 'olumlu'
        
        entity_list.append(ent)
        results.append({"entity": ent, "sentiment": entity_sentiment})

    return {
        "entity_list": entity_list,
        "results": results
    }
