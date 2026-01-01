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