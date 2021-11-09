from SampleMadlibs import *
import random 

if __name__=="__main__": # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
    obj=madlibs()
    m=random.choice([obj.action(),obj.romance(),obj.sport()])
    print(m)
