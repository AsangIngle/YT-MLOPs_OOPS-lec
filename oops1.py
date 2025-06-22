class employtee:
    #special fuction
    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation="ML engineer"
        
    def work(self,destination):  #function iside class is called method
        print(f"travling to {destination} with {self.salary}")
       
    
sam=employtee()
print(sam.salary,sam.id)
print(type(sam))
print(sam.work("bhopal"))