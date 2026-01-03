class MultipleFunctions():
     # Create a class and function, and list out the items in the list
    def Subfields():
        list2=['Sub-fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech','NLP']
        for temp in list2:
            print (temp)
            
    # Create a function that checks whether the given number is Odd or Even
    def OddEven():
        number=input("Enter number? : ")
        if (int(number)%2==0):
            print(number+" is even number")
        else:
            print(number+" is  odd number")
            
    # Create a function that tells elegibility of marriage for male and female according to thei
    # r age limit like 21 for male and 18 for female 
            
    def Eligible():
        gender=input("Enter gender? : ")
        age=int(input("Enter age? : "))
        if(gender=='Male' and age >= 21):
            print ("Eligible")
        elif (gender=="Female" and age>=18):
            print ("Eligible-female ")
        else:
            print("Not eligible")
        #return
    #a=Eligible()
    
    
    # calculate the percentage of your 10th mark
    def percentage():
        s1=int(input("Enter Subject1 = "))
        s2=int(input("Enter  Subject2 ="))
        s3=int(input("Enter : Subject3 ="))
        s4=int(input("Enter : Subject4 ="))
        s5=int(input("Enter  Subject5 ="))
        tot=s1+s2+s3+s4+s5
        perc=tot/5
        print(tot)
        return perc

    #print area and perimeter of triangle using class and functions
    def triangle(): 
        Height=int(input("Enter Height = ")) 
        Breadth=int(input("Enter Breadth =")) 
        area= (Height*Breadth)/2 
        print("Area of triangle=") 
        print(area) 
        #perimeter calc 
        Height1=int(input("Enter Height1 = ")) 
        Height2=int(input("Enter Height2 = ")) 
        Breadth=int(input("Enter Breadth =")) 
        peri= (Height1+Height2+Breadth)
        print("perimeter=") 
        print(peri)