import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle
from tensorflow.keras.models import load_model

df = pd.read_csv('crawling_data/naver_shopping_20240126.csv')
print(df.head())
df.info()

X = df['titles']
Y = df['category']

with open('./models/label_encoder.pickle','rb') as f:
    label_encoder = pickle.load(f)

labeled_y = label_encoder.transform(Y)
label = label_encoder.classes_
print(labeled_y)
print(label)

okt = Okt()

for i in range(len(X)):
    X[i] = okt.morphs(X[i],stem=True)
stopword = pd.read_csv('./stopwords.csv',index_col=0)
for j in range(len(X)):
    words=[]
    for i in range(len(X[j])):
        if len(X[j][i]) >1:         #1글자는 제거
            if X[j][i] not in list(stopword['stopword']):   #stopword에 없으면 X에 추가
                words.append(X[j][i])
    X[j] = ' '.join(words)
#print(X[0])
#토큰화
with open('./models/news_token.pickle','rb') as f:
    token = pickle.load(f)
tokened_X = token.texts_to_sequences(X)     #번호부여
for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 29:
        tokened_X[i] = tokened_X[i][:29]

x_pad = pad_sequences(tokened_X,29)

model = load_model('./models/news_category_classification_model_0.9050343036651611.h5')
preds = model.predict(x_pad)

predicts = []
for pred in preds:
    most = label[np.argmax(pred)]
    pred[np.argmax(pred)] = 0
    second = label[np.argmax(pred)]
    predicts.append([most, second])
df['predict'] = predicts
print(df)

df['OX'] = 0
for i in range(len(df)):
    if df.loc[i, 'category'] in df.loc[i, 'predict']:
        df.loc[i, 'OX'] = 'O'
    else: df.loc[i, 'OX'] = 'X'
print(df['OX'].value_counts())
print(df['OX'].value_counts()/len(df))

for i in range(len(df)):
    if df['category'][i] not in df['predict'][i]:
        print(df.iloc[i])