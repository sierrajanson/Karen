# Authors: Sierra Janson, Brendan Rose, Shubhi Mishra
# Date: 12/28/2023
# Project: Karen Sentiment Analysis
# python testing.py 
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
#from testor import Testorv2
# 4. uncomment this below and run once to download reviews to local system
    # nltk.download('movie_reviews') 

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()
#nltk.download('movie_reviews')

#size = 5                                                                                 # will adjust to a greater number once we are confident it is working as intended
#pos_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='pos')[0:size]) # movie_reviews.raw() seems to return a string with the amount of reviews you specify using size
#neg_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='neg')[0:size]) # 4124283 positive reviews and 3661721 negative reviews in total

def parsing(unparsed_text):                                                              # removes text that does not have a sentiment
    punctuation_chrs = "\"!,.?();:"                                                      # removing punctuation (these actually can contribute to sentiment but for our basic model we're gonna ignore them for now)
    filler_words = ["the","and","for", "with", "it's", "she","you","they","her","him","are"]   # removing preprepositional phrases 

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
    
def prediction(x,reviewLength):
    sentiment = None

    pos_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='pos')[0:reviewLength])
    neg_reviews = movie_reviews.raw(fileids=movie_reviews.fileids(categories='neg')[0:reviewLength])
    # Naive Bayes equation: P(c|x) = [ P(x|c) P(c) ]/ P(x)
    # x is text_inputted to Karen that has been parsed in list format 
        # for example: x = ['hello', 'today', 'great', 'day']
    # c is sentiment
        # for example: c = positive 
    # STEPS:
    # 1. Find P(x|c)
        # how many words in x are in c vocabulary (how many times they actually show up)
        # how many words in ['hello', 'today', 'great', 'day'] are in the positive vocabulary
    # 2. Find P(c)                                                                      
        # number of positive reviews in training_data / total # of reviews
        # should be a constant since number of positive reviews should be fixed
    # 3. Find P(x)
        # number of words in x that are in total vocabulary / # of total words in vocabulary
    # 4. Use Naive Bayes equation to find P(c|x)
    # 5. if P(c|x) > 0.5 the sentiment is positive, else the sentiment is negative 
    positiveWords = parsing(pos_reviews)
    negativeWords = parsing(neg_reviews)
    
    pxc = 0#words in positivitive vocabulary
    pc = 0.5 # this is true if reviewLength is used as the endpoint for both neg_reviews and pos_reviews above
    wordsinTotalVocab = 0
    for word in x:
        if word in positiveWords:
            wordsinTotalVocab += positiveWords.count(word)
        if word in negativeWords:
            wordsinTotalVocab += negativeWords.count(word)
    px = wordsinTotalVocab/(len(positiveWords)+len(negativeWords))#words in vocabulary
    for karenword in x:
       if karenword in positiveWords:
            pxc += positiveWords.count(karenword)
    pxc = pxc / len(positiveWords)
    pcx = (pxc * pc) / px

    pxc_neg = 0#words in positivitive vocabulary
    for karenword in x:
       if karenword in negativeWords:
            pxc_neg += negativeWords.count(karenword)
    pxc_neg /= len(negativeWords)
    pcx_neg = (pxc_neg * pc) / px
    
    if pxc > pxc_neg:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"
    
    # NOTES:
    # in Scai I think they used logarithms in their algorithm to increase the accuracy as well as some sort of smoothing.. 
    # we should eventually implement both
    # I think it would be a good idea to make a class that encapsulates the prediction and parsing functions for elegance
    # (something that could initialize constants like P(c), pos_vocab, neg_vocab)
    # even though Sankie is an oop hater (raised eyebrow emoji) no i love it!! I LOVE OOP
    return sentiment
def sentiment_analysis(input_text):
    import nltk 
    from nltk.corpus import movie_reviews
    nltk.download('movie_reviews')
    parsed_input = parsing(input_text)
    sentiment = prediction(parsed_input,100)
    return sentiment

if __name__ == "__main__":
    input_text = "unlikeable lame"     # on the react or python side we need to parse the transcript to surround all punctuation with a space so that it can be processed by parsing function correctly
    parsed_input = parsing(input_text)
    sentiment = prediction(parsed_input, 1115)
    print(sentiment)
