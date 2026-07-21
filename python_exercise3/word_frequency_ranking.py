def rank_words(text, top_n):
    # Step 1: Clean and split the text into words
    words = text.lower().split()
    
    # Step 2: Build frequency dictionary using a loop
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    # Step 3: Get list of (word, count) pairs
    items = list(freq.items())
    
    # Step 4: Manual ranking using loops and conditions (no sorted with key)
    ranked = []
    for _ in range(min(top_n, len(items))):
        max_count = -1
        max_index = -1
        
        # Find the word with highest frequency
        for i in range(len(items)):
            if items[i][1] > max_count:
                max_count = items[i][1]
                max_index = i
        
        # Add to result and remove from items
        if max_index != -1:
            ranked.append(items.pop(max_index))
    
    return ranked


# Test the function
if __name__ == "__main__":
    result = rank_words("the fox and the hound and the cat", 2)
    print(result)
    