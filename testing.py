import nltk 
# nltk.download('movie_reviews') # run once to download reviews to local system
from nltk.corpus import movie_reviews
size = 5
pos_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='pos')[0:size]) # 4124283 positive reviews
neg_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='neg')[0:size]) # 3661721 negative reviews 

def parsing(string_collection):
    punctuation_chrs = "\"!,.?();:0123456789"
    filler_words = ["the","and","for", "with", "it's", "she","you","they","her","him"]

    words = string_collection.split(" ")
    parsed_words = []
    for word in words:
        if word in punctuation_chrs or word in filler_words:
            pass
        elif "\n" in word:
            parsed_words.append(word[2:])
        elif len(word) < 3:
            pass
        else:
            try:
                word = int(word)
            except ValueError:
                parsed_words.append(word)

    return parsed_words
    
# STEP ONE --> TRAINING THE MODEl
def training(vocabulary): # Naive Bayes equation: P(c|x) = [ P(x|c) P(c) ]/ P(x)
    pass
    # make vocabularies and remove filter words --> so we can create X
    # find P(C) --> how many reviews from each class are we including
print(parsing(pos_reviews))



# then can use P(c|x) and find the probability of words given class, probability of class (constant), and probability of words in the training set 
# p(c) is the probability of class given all of the training data
# whereas p(c|x) is the specific probability of c given the features of x
# we do not know this so we use the naive bayes equation
# P(c) = # of positive reviews/ total # of reviews 
# P(x|c) = # of sample words in class / total words in class
# P(x) = # of times sample words show up / all words in class 
# probability of the features given the class 
# probability of class given words = probability of words given class  * probability of class all divided by probability of words