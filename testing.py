# Authors: Sierra Janson,
# Date: 12/28/2023
# Project: Karen Sentiment Analysis

# for setting up, follow these steps: ----------------------------------------------------------------------------
# 1. install a virtual python environment to VSC
    # this way when you are pip installing things you are not modifying the python version on your hardware system
    # but one isolated to the project folder you have it in 
    # it makes it easier to control what external libraries and versions you are using per project essentially 

    # a. CTRL + SHIFT + P
    # b. type in Python Environment to the URL bar and it should pop up
    # c. select .venv and wait for it to download
# 2. you should see a green (.venv) in your terminal to the left of the file path to your project file
    # a. if not enter in the command ".venv/scripts/activate" + wait for this to be true
# 3. enter the command "pip install nltk" in your terminal

import nltk 
# 4. uncomment this below and run once to download reviews to local system
    # nltk.download('movie_reviews') 

from nltk.corpus import movie_reviews
size = 5                                                                                 # will adjust to a greater number once we are confident it is working as intended
pos_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='pos')[0:size]) # movie_reviews.raw() seems to return a string with the amount of reviews you specify using size
neg_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='neg')[0:size]) # 4124283 positive reviews and 3661721 negative reviews in total

def parsing(unparsed_text):                                                              # removes text that does not have a sentiment
    punctuation_chrs = "\"!,.?();:"                                                      # removing punctuation (these actually can contribute to sentiment but for our basic model we're gonna ignore them for now)
    filler_words = ["the","and","for", "with", "it's", "she","you","they","her","him"]   # removing preprepositional phrases 

    words = unparsed_text.split(" ")                                                     # split into individual words and remove spaces
    parsed_words = []
    for word in words:
        if word in punctuation_chrs or word in filler_words:
            pass
        elif "\n" in word:                                                               # removes newline characters
            parsed_words.append(word[2:])                                               
        elif len(word) < 3:                                                              # removes single chars and a decent amount of preprepositional phrases
            pass
        else:
            try:                                                                         # removes integers
                word = int(word)
            except ValueError:
                parsed_words.append(word)
    return parsed_words
    
def prediction(x):
    sentiment = None
    # Naive Bayes equation: P(c|x) = [ P(x|c) P(c) ]/ P(x)
    # x is text_inputted to Karen that has been parsed in list format 
        # for example: x = ['hello', 'today', 'great', 'day']
    # c is sentiment
        # for example: c = positive 
    # STEPS:
    # 1. Find P(x|c)
        # how many words in x are in c vocabulary
        # how many words in ['hello', 'today', 'great', 'day'] are in the positive vocabulary
    # 2. Find P(c)                                                                      
        # number of positive reviews in training_data / total # of reviews
    # 3. Find P(x)
        # number of words in x that are in total vocabulary / # of total words in vocabulary
    # 4. Use Naive Bayes equation to find P(c|x)
    # 5. if P(c|x) > 0.5 the sentiment is positive, else the sentiment is negative 

    # NOTES:
    # in Scai I think they used logarithms in their algorithm to increase the accuracy as well as some sort of smoothing.. 
    # we should eventually implement both
    # I think it would be a good idea to make a class that encapsulates the prediction and parsing functions for elegance
    # (something that could initialize constants like P(c), pos_vocab, neg_vocab)
    # even though Sankie is an oop hater (raised eyebrow emoji)
    return sentiment

if __name__ == "__main__":
    input_text = "hello ! today is a great day"     # on the react or python side we need to parse the transcript to surround all punctuation with a space so that it can be processed by parsing function correctly
    parsed_input = parsing(input_text)
    sentiment = prediction(parsed_input)

    



