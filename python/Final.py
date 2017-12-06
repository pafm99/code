def adding_report(report):
    items = ""
    answer = True   
    question = 0
    Q = "quit"
    A = "add"
    total = 0
    while answer == True:
        question = input('Enter an integer or "Q" to Quit ')
        if question.isdigit() == True:
            total = total + int(question)
            items +=str(question)
        elif question.isalnum() == True:
            if question == "A":
                print("Items:")
                for item in items:
                    print(item)
                print("Total:" + str(total))
            elif question == "T":
                print("Total:" + str(total))
                break
            elif question =="Q":
                break
            else:
                print(question + ' is invalid input')
adding_report(A)


