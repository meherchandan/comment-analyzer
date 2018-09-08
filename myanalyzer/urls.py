"""myanalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from myanalyzer.views import hello, current_datetime,hours_ahead,checkposneg
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from django.http import HttpResponse

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

neg_reviews = []
i = 0
for fileid in movie_reviews.fileids('neg'):
    if(i>100):
        break
    i +=1
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "Negative"))
  
print("Negative",len(neg_reviews))
pos_reviews = []
i =0
for fileid in movie_reviews.fileids('pos'):
    if(i>100):
        break
    i +=1
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "Positive"))
     
print("positive",len(pos_reviews))
train_set = neg_reviews[:80] + pos_reviews[:80]
test_set =  neg_reviews[80:] + pos_reviews[80:]
print(len(train_set),  len(test_set))
classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', hello),
    url(r'^datetime/plus/(\d{1,2})$', hours_ahead),
    url(r'^datetime$', current_datetime),
    url(r'^analyzedata$',checkposneg,{'classifier':classifier}),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
