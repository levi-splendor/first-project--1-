def count_words(sentence):
    words = sentence.split()         
    count = {}                        
    
    for word in words:
        if word in count:
            count[word] += 1          
        else:
            count[word] = 1           
    return count


result = count_words("i am learning python am AM")
print(result)