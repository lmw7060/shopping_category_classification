import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
import pickle

df=pd.read_csv('./shopping_titles_20240130.csv')
print(df.head())
df.info()

X=df['titles']
Y=df['category']

encoder=LabelEncoder()
labeled_y=encoder.fit_transform(Y)
#print(labeled_y[:3])
label =encoder.classes_
#print(label)

with open('./models/label_encoder.pickle' , 'wb') as f:
    pickle.dump(encoder, f)

onehot_y = to_categorical(labeled_y)
#print(onehot_y[:3])

okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)      #형태소로 나눔 stem은 원형으로 나올것인지 확인
#print(X[0])
#필요없는 단어를 삭제
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
token = Tokenizer()
token.fit_on_texts(X)       #순서
tokened_X = token.texts_to_sequences(X)     #번호부여
wordsize = len(token.word_index) +1     #인덱스가 1부터 생기기때문에 1을 더해준다 0을 쓰려고
#print(tokened_X[:3])
#print(wordsize)
#피클링
with open('./models/news_token.pickle','wb') as f:
    pickle.dump(token, f)
#가장 긴 단어에 맞춰준다
max = 0
for i in range(len(tokened_X)):
    if max < len(tokened_X[i]):
        max = len(tokened_X[i])
print(max)
#빈 공간을 0으로 채워준다
x_pad = pad_sequences(tokened_X,max)
print(x_pad[:3])
#모델 트레이닝테스트
X_train, X_test,Y_train, Y_test = train_test_split(x_pad,onehot_y,test_size=0.2)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)
#저장
xy = X_train, X_test,Y_train, Y_test
xy = np.array(xy,dtype=object)
np.save('./shopping_data_max_{}_wordsize_{}'.format(max, wordsize), xy)