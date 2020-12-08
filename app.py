from flask import Flask, request, render_template
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
from SimpleText.preprocessor import preprocess 

model= Doc2Vec.load("models/d2v.model")

df = pd.read_csv('data/movie_plots.csv')
# only keep training data
df = df[df.split != 'val']

# delete split column
del df['split']

# reset the index 
df = df.reset_index(drop=True)

def get_similar_movies_from_new(plot_synoposis, df, topn):
    
    # pre-process text
    processed_tokens = preprocess(plot_synoposis, n_grams=(1,1), remove_accents=True, lower=True, remove_less_than=1, 
                                            remove_more_than=15,remove_punct=True, remove_alpha=True, 
                                            remove_stopwords=True, remove_custom_stopwords = [], 
                                            lemma=False, stem=False, remove_url=True)
    
    new_vector = model.infer_vector(processed_tokens)
    similar_doc = model.docvecs.most_similar([new_vector], topn=topn)
    indexes = [tup[0] for tup in similar_doc]
    return list(df.loc[df.index.isin(indexes)]['title'].values)

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    search1 = request.form['text1']
    return "<h3>{}</h3>".format(get_similar_movies_from_new(search1, df, topn=20))
    #return "<h1>Was this your search: {}</h1>".format(search1)
   

if __name__ == '__main__':
    app.run()