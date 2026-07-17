def student_averages(students):
    averages = {}       # Dictionary to store name: average
    for student in students:
        name = student["name"]
        marks = student["marks"]
        avg = sum(marks) / len(marks)    # Calculate average
        averages[name] = avg             # Store name and average
    return averages
def top_student(averages):
    top_name = ""      
    top_avg = -1    
    for name in averages:
        # If current student has higher average
        if averages[name] > top_avg:     
            top_avg = averages[name]
            top_name = name
    return top_name
students = [
    {"name": "Alice", "marks": [85, 90, 78]},
    {"name": "Bob", "marks": [60, 55, 70]},
    {"name": "Cara", "marks": [95, 92, 89]}
]
averages = student_averages(students)
print(averages)
print("Top Student:", top_student(averages))