## This is a testor python file containing the testor class used to check the accuracy of our model 
# type: ignore
#the above line is just for pylance to ignore the missing import
class Testor():
    def __init__(self,statement,answer):
        self.statement=statement
        self.answer=answer
    @property #converted to property to avoid unecessary function building 
    def check(self):
        from transformers import pipeline
        expected=(pipeline('sentiment-analysis')(self.statement))
        userans=str(self.answer).upper()
        if expected[0].get('label')!= userans:
            print(f"Test Failed Expected:{expected[0].get('label')} and instead got:{self.answer}")
        else:
            print(f"Test Passed Confidence Value:{expected[0].get('score')//(1/100)}%")
        
# Example usecase Testor('i love you','positive').check
