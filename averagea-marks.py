#create function one for average marks only

def find_average_marks(marks):
    average_marks = sum(marks)/len(marks)

#retruning the avarage mark to the function
    return average_marks
marks = [55,64,75,80, 65]
#pasing the function to average marks
average_marks = find_average_marks(marks)

# creating function two for grades
def my_Grade(average_marks):
    if average_marks >=80:
        grade = "A"
    elif average_marks >=60:
        grade = "B"
    elif average_marks >=50:
        grade = "C"
    else:
        grade = "F"
#returng grads back to function
    return grade
#passing function to grade as variable
grade = my_Grade(average_marks)

#printing grade and average marks
print("Your average marks is:",average_marks)
print("And your gade is:",grade)
