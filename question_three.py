# part (i)
# part (ii)
grade_students = int(input("Enter the student's score   :"))

if 90 <= grade_students <= 100:
   print("Grade is A")
elif 80 <= grade_students<= 89:
   print("Grade is B")
elif 70 <= grade_students<= 79:
   print("Grade is C")
elif 60 <= grade_students<= 69:
   print("Grade is D")
elif 0<= grade_students<= 59:
     print("Grade is F")

# part(iv)
def grade_students():
        score = int(input("Enter the student's score: "))
        print("Valid Input")
        
        if 90 <= score <= 100:
            print("Grade is A")
        elif 80 <= score <= 89:
            print("Grade is B")
        elif 70 <= score <= 79:
            print("Grade is C")
        elif 60 <= score <= 69:
            print("Grade is D")
        elif 0 <= score <= 59:
            print("Grade is F")
        else:
            print(f"Score is out of valid range.")
        print("Invalid Input")

# part(v)
grade_students = int(input("Enter the student's score   :"))

if 90 <= grade_students <= 100:
   print("Grade is A - Excellent")
elif 80 <= grade_students <= 89:
   print("Grade is B - Excellent")
elif 70 <= grade_students <= 79:
   print("Grade is C - Good")
elif 60 <= grade_students <= 69:
   print("Grade is D - Satisfactory")
elif 0 <= grade_students <= 59:
   print("Grade is F - Needs Improvement")



