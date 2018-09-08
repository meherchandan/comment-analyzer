import datetime
import json
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
    if(i>10):
        break
    i +=1
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "Negative"))
  
print("Negative",len(neg_reviews))
pos_reviews = []
i =0
for fileid in movie_reviews.fileids('pos'):
    if(i>10):
        break
    i +=1
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "Positive"))
     
print("positive",len(pos_reviews))
train_set = neg_reviews[:8] + pos_reviews[:8]
test_set =  neg_reviews[8:] + pos_reviews[8:]
print(len(train_set),  len(test_set))
classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)
def checkposneg(request):
    try:
        print("request received")
        json_data = json.loads(request.body)
        comment = json_data['data']
        words = word_tokenize(comment)
        words = create_word_features(words)
        print(classifier.classify(words))
        return HttpResponse(classifier.classify(words))
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

