#!/usr/bin/env python

import sys, logging, os, yaml
import pandas as pd
import pprint

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

from flask import Flask, request, g

pp = pprint.PrettyPrinter(indent=2)
app = Flask(__name__)


def train_model():
  df = pd.read_csv("Dataset_N.csv", sep=';')
  df.dropna(inplace=True)
  logging.info("df.shape: %s", df.shape)
  df['Text'] = df.V3.str.cat(df.V4)
  df.drop(columns=['V1', 'V3', 'V4', 'V5'], inplace=True)
  df.V2 = pd.Categorical(df.V2)
  df['category_id'] = df.V2.cat.codes
  X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['category_id'], random_state = 0)
  count_vect = CountVectorizer()
  X_train_counts = count_vect.fit_transform(X_train)
  tfidf_transformer = TfidfTransformer()
  X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
  clf = MultinomialNB().fit(X_train_tfidf, y_train)
  return (clf, count_vect)

def predict(clf, count_vect, input_str):
  return clf.predict(count_vect.transform([input_str]))

def read_config(file_path):
  logging.info("Function: %s", sys._getframe().f_code.co_name)
  config = yaml.safe_load(open(file_path))
  return config


def get_state():
  state = getattr(g, 'state', None)
  logging.info('State: %s', state)
  if state is None:
    logging.info('Creating state...')
    state = g.state = train_model()
  return state

@app.route('/query-example')
def query_example():
  clf, count_vect = get_state()
  input_str = request.args['input_str']
  pred = predict(clf, count_vect, input_str)
  return str(pred[0])

def main():
  try:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')
    logging.info('Interpreter location: %s', sys.executable)
    category_dict = {
      0: 'BICYCLES',
      1: 'CONTACT LENSES',
      2: 'USB MEMORY',
      3: 'WASHINGMACHINES',
    }
    app.run(debug=True, port=5000)
  except KeyboardInterrupt:
    logging.info("Ctrl+c was pressed, exiting...")
    sys.exit()

if __name__ == '__main__':
  main()

