def calculate_grade(score):
    if score>=90:
        return "A-Excellent"
    elif score>=80:
        return("B-very Good")
    elif score>=70:
      return("C-Good")
    elif score >=60:
       return("D-average")
    elif score >=50:
       return("E-fair")
    else:
       return("F-failed"),

print("===students grade calculator===")
name=input("enter students name")
subject=input("enter subject")
score=float(input("enter student score"))

#calculate grade
grade = calculate_grade(score)

#store in dictionary
student_record={
   "name":name,
   "subject":subject,
   "score":score,
   "grade":grade,
}
print(f"key.capitalize",student_record)

