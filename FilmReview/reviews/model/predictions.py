from tensorflow.keras.models import Model
import tensorflow
from tensorflow.keras.layers import Embedding,Conv1D,LSTM,GRU,BatchNormalization,Flatten,Dense, Input
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re


MODEL_PATH='reviews/model/caselabs_model.keras'
TOKENIZER_PATH = 'reviews/model/tokenizer.pickle'
MAX_LEN = 2525


def clean_sentences(line):
    line = line.strip().lower()
    line=re.sub('<.*?>','',line)
    line=re.sub("isn't",'is not',line)
    line=re.sub("he's",'he is',line)
    line=re.sub("wasn't",'was not',line)
    line=re.sub("did't",'did not',line)
    line=re.sub("doesn't",'does not',line)
    line=re.sub("there's",'there is',line)
    line=re.sub("couldn't",'could not',line)
    line=re.sub("won't",'will not',line)
    line=re.sub("they're",'they are',line)
    line=re.sub("she's",'she is',line)
    line=re.sub("there's",'there is',line)
    line=re.sub("wouldn't",'would not',line)
    line=re.sub("haven't",'have not',line)
    line=re.sub("that's",'that is',line)
    line=re.sub("you've",'you have',line)
    line=re.sub("what's",'what is',line)
    line=re.sub("weren't",'were not',line)
    line=re.sub("we're",'we are',line)
    line=re.sub("hasn't",'has not',line)
    line=re.sub("you'd",'you would',line)
    line=re.sub("shouldn't",'should not',line)
    line=re.sub("let's",'let us',line)
    line=re.sub("they've",'they have',line)
    line=re.sub("you'll",'you will',line)
    line=re.sub("i'm",'i am',line)
    line=re.sub("we've",'we have',line)
    line=re.sub("it's",'it is',line)
    line=re.sub("don't",'do not',line)
    line=re.sub("that´s",'that is',line)
    line=re.sub("I´m",'I am',line)
    line=re.sub("it’s",'it is',line)
    line=re.sub("she´s",'she is',line)
    line=re.sub("he’s'",'he is',line)
    line=re.sub('I’m','I am',line)
    line=re.sub('I’d','I did',line)
    line=re.sub("he’s'",'he is',line)
    line=re.sub('there’s','there is',line)
    line=re.sub('\x97','',line)
    line=re.sub('\x84','',line)
    line=re.sub('\uf0b7','',line)
    line=re.sub('¡¨','',line)
    line=re.sub('\x95','',line)
    line=re.sub('\x8ei\x9eek','',line)
    line=re.sub('\xad','',line)

    punctuations = '@#!~?+&*[]-%._-:/£();$=><|{}^' + '''"“´”'`'''
    for p in punctuations:
        line = line.replace(p, f' {p} ')

    line=re.sub(',',' , ',line)
    line = line.replace('...', ' ... ')
    if '...' not in line:
        line = line.replace('..', ' ... ')
    return line


def evaluate_text(text, tokenizer, model):
  text = [clean_sentences(text)]
  text = pad_sequences(tokenizer.texts_to_sequences(text),maxlen=MAX_LEN)
  output = model.predict(text)
  rating = round(output[0][0][0]*10)
  sentiment = output[1][0].argmax()
  return rating, sentiment

