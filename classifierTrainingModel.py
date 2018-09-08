import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

print("loading")
neg_reviews = []
i=0
for fileid in movie_reviews.fileids('neg'):
    if(i>10):
        break
    i = i+1
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "Negative"))
  
print("Negative",len(neg_reviews))
pos_reviews = []
i =0
for fileid in movie_reviews.fileids('pos'):
    if(i>10):
        break
    i = i+1
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "Positive"))
     

print("positive",len(pos_reviews))
train_set = neg_reviews[:8] + pos_reviews[:8]
test_set =  neg_reviews[8:] + pos_reviews[8:]
print(len(train_set),  len(test_set))
classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()