def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
scores = [95, 85, 75, 65, 55, 42]
for s in scores:
    print(f"Score: {s} -> Grade: {get_grade(s)}")