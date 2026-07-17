def classify_temps(temps):
    if temps < 10:
        return "cold"
    elif temps < 25:
        return "mild"
    else:
        return"Hot"
    
def temperature_report(temp):
    counts={
        "cold":0,
        "mild":0,
        "Hot":0,
    }
    
    for t in temp:
      category=classify_temps(t)
      counts[category]+=1
    return counts
temp=[2, 37, 80, 49,190]
print(temperature_report(temp))


    
