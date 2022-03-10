#Name: Ibrahim Salisu #123
#quizgenerator.py

while True:# Using infinite loop to restart the quiz.
    
    # a) three variables initialization

    correct = int(0)
    count = int(0)
    totalquestions = int(5)

    # b) Initializing timer using time library
    import time

    #Storing time in startTime variable using  time() method.
    startTime = time.time()

    print("\nThe quiz has started")


    # c) Importing Random Module 

    import random



    #Generating two single integers using randint() method 
    # d) Asking the student question and looping through total number of questions
    while count<totalquestions:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        answer = int(input("What is "+str(num1)+"**"+str(num2)+" ?\n"))
        if(answer != num1**num2):
            print("You are wrong!, Correct answer is "+str(int(num1**num2)))
        else:
            print("You are Correct!")
            correct+=1
        count+=1

    # e) Calculating total time taken 
    endTime = time.time()
    totalTime = int(endTime-startTime)

    # f) Printing number of points received based on correct answers
    print("*"*50)
    print("The number of points received are "+str(correct)+" out of "+str(totalquestions))
    print("The total test time taken is "+str(totalTime)+" seconds.")
    
    # g) Asking user to retake or exit the program
    retake = input("Do you want to retake the quiz? Type Y/N\n")
    
    if(retake.upper()=="N"):
        print("Thanks for taking this quiz Bye...\n")
        break
    else:
        continue



        
    




