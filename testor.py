## This is a testor python file containing the testor class used to check the accuracy of our model 
from transformers import pipeline
class Testor():
    def __init__(self,statement,answer):
        self.answer=answer
        self.statement=statement
        self.classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True)
    def check(self,statement,answer):
        classifier=self.classifier
        highest_val=["default",0]
        for i in classifier(statement)[0]:
            if i.get('score')>=highest_val[-1]:
                highest_val=[f"{i.get('label')}",f"{i.get('score')}"]
        if answer!=highest_val[0]:
            return f"Failure: Expected answer:{highest_val[0]},got answer {answer}"
        else: 
            return f"Correct Answer"

            
Testor().check("I'm feeling good!","positive")
        
