from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import ReviewForm, Review
from django.template import RequestContext
from django.db.models import signals
from .model.predictions import MODEL_PATH, TOKENIZER_PATH, evaluate_text
import tensorflow
import pickle

with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)
model = tensorflow.keras.models.load_model(MODEL_PATH)


def predict_sentiment(sender, instance, *args, **kwargs):
    instance.rating, instance.sentiment = evaluate_text(instance.description, tokenizer, model)
signals.pre_save.connect(receiver=predict_sentiment, sender=Review)


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            form = ReviewForm()
        else:
            print(form.errors)
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})
    else:
        form = ReviewForm()
        reviews = Review.objects.all()
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})



