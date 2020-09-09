from flask import render_template
from flask import request
from flask import redirect
from models import Book
from config import app, db
from utils import process_url_params
from logic import model_set
import json

@app.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/api/<model>/", methods=["GET"])
def api_get_model(model):
    query_dict = process_url_params(request.args)
    model = model_set[model](query_dict)
    return json.dumps({'prediction': model.get_prediction()})
