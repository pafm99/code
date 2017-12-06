def str_analysis(answer):
    question = ""
    while question != answer: 
        question = input("enter a word or an integer ")
        if input == None:
            print(question = input("enter a word or an integer "))
        elif question.isalpha() == True:
            print(question + " is all aphabetical characters")
        elif question.isdigit() == True:
            if int(question) < 50:
                print(question + " is a smaller number than expected")
            else:
                print(question + " is a pretty large number")       
        elif question.isalnum() == True:
            print(question + " has multiple character types")

        else:
            print(question + "is none of the above")

str_analysis(10)
                  
