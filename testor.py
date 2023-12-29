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
class Testorv2():
    def __init__(self,linput) -> None:
        self.linput=linput
    @property
    def check(self):
        outputlist_failed=[]
        for i in self.linput:
            self.answer=i[1]
            self.statement=i[0]
            from transformers import pipeline
            pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
            expected=(pipe(self.statement))
            userans=str(self.answer).upper()
            if expected[0].get('label')!= userans:
                print(f"Test Failed Expected:{expected[0].get('label')} and instead got:{userans}")
                outputlist_failed.append([i,"expected:"+expected[0].get('label')])
            else:
                print(f"Test Passed Confidence Value:{expected[0].get('score')//(1/100)}%")
        if outputlist_failed==[]:
            print("No failures.. All Cases Pass")
        else:
            print(f"Number of failures:{len(outputlist_failed)}")
            print(f"Output list of all the failures:{outputlist_failed}")
# Example Use Case Testorv2([('i love you','positive'),('i love you','negative')]).check