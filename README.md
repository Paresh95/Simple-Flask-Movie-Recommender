# Simple-Flask-Movie-Recommender
Flask Movie Recommender - input text synopsis and get back similar movies.

Uses Doc2Vec model trained on text movie synopisis. 

### Folder structure

```
~/Simple-Flask-Movie-Recommender
    |-- Word2Vec, Doc2Vec and TFIDF.ipynb #notebook with example for training the model
    |-- app.py #python file containing the flask app
    |-- requirements.txt #a list of python modules to be installed
    |-- /data
        |-- movie_plots.csv #data used for training
    |-- /templates
        |-- index.html #HTML webpage with text input
    |-- /models
        |-- dv2.model #doc2vec model
    |-- /env

### Set up

- Download files from this GitHub repo
- Download the [data](https://www.kaggle.com/cryptexcode/mpst-movie-plot-synopses-with-tags).
- Install the requirements in a virtual environment
- Train the Doc2Vec model using the Jupyter Notebook code as an example
- Run the Flask app and input a movie synposis to get movie recommendations
