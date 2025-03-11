#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N")
#take input of attendence
atten = int(input("enter the atendence of students: "))

#checking the user input predicting output accordingly

if medical_cause == 'y':
    print("your allowed")

else:
    if atten>=75: #checking the condition 2
      print("allowed")
    else:
        print("not allowed")

