def average_rating_by_genre(movies):
    genre_ratings = {}                    # Dictionary to store genre data
    
    for movie in movies:
        genre = movie["genre"]
        rating = movie["rating"]
        
        if genre in genre_ratings:
            genre_ratings[genre].append(rating)   # Add rating to existing genre
        else:
            genre_ratings[genre] = [rating]       # Create new list for genre
    
    # Calculate average for each genre
    averages = {}
    for genre in genre_ratings:
        avg = sum(genre_ratings[genre]) / len(genre_ratings[genre])
        averages[genre] = round(avg, 2)           # Round to 2 decimal places
    
    return averages


def movies_above(movies, min_rating):
    result = []                           # List to store qualifying movie titles
    
    for movie in movies:
        if movie["rating"] >= min_rating:     # Check condition
            result.append(movie["title"])
    
    return result


# Example usage
movies = [
    {"title": "Movie A", "genre": "Action", "rating": 7.5},
    {"title": "Movie B", "genre": "Comedy", "rating": 6.0},
    {"title": "Movie C", "genre": "Action", "rating": 8.8},
    {"title": "Movie D", "genre": "Drama", "rating": 9.1}
]

print(average_rating_by_genre(movies))
print(movies_above(movies, 7.5))
