import datetime
import json
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from django.http import HttpResponse
from afinn import Afinn

import pickle
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

def checkposneg(request):
    try:
        json_data = json.loads(request.body)
        comment = json_data['data']
        afinn = Afinn()
        result = afinn.score(comment)
        if(result>0):
            return HttpResponse("Positive")
        elif(result<0):
            return HttpResponse("Negative")
        else:
            return HttpResponse("Neutral")


        # classifier_f = open("naivebayes.pickle", "rb")
        # classifier = pickle.load(classifier_f)
        # classifier_f.close()
        # print("request received")
        # json_data = json.loads(request.body)
        # comment = json_data['data']
        # words = word_tokenize(comment)
        # print("word length",len(words))
        # if(len(words)<10):
        #    return HttpResponse("Comment is too short. Unable to analyze.") 
        # words = create_word_features(words)
        # print(classifier.classify(words))
        # return HttpResponse(classifier.classify(words))
    except:
        import sys
        print(str(sys.exc_info()))
        return "Internal Server Error"

    

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    html = "<html><body>It is now %s.</body></html>" % datetime.datetime.now()
    return HttpResponse(html)

def hours_ahead(request, offset):
    dt = datetime.datetime.now() +datetime.timedelta(hours = int(offset))
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

