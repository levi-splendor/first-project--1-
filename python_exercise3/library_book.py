def available_books(library):
    """Return a list of book titles that have at least one copy available."""
    available = []
    for title, info in library.items():
        if info.get("copies_total", 0) - info.get("copies_borrowed", 0) > 0:
            available.append(title)
    return available


def borrow_book(library, title):
    """Borrow a book if available, otherwise show appropriate message."""
    if title not in library:
        print(f"The book '{title}' does not exist.")
        return
    
    info = library[title]
    if info["copies_total"] - info["copies_borrowed"] > 0:
        info["copies_borrowed"] += 1
        print(f"You borrowed '{title}'.")
    else:
        print(f"The book '{title}' is currently unavailable.")


def return_book(library, title):
    """Return a book. Never let copies_borrowed go below 0."""
    if title not in library:
        print(f"The book '{title}' does not exist.")
        return
    
    info = library[title]
    if info["copies_borrowed"] > 0:
        info["copies_borrowed"] -= 1
        print(f"You returned '{title}'.")
    else:
        print(f"'{title}' has no borrowed copies to return.")


# Example usage:
if __name__ == "__main__":
    library = {
        "The Great Gatsby": {"copies_total": 3, "copies_borrowed": 1},
        "1984": {"copies_total": 2, "copies_borrowed": 2},
        "To Kill a Mockingbird": {"copies_total": 5, "copies_borrowed": 0}
    }

    print("Available books:", available_books(library))
    
    borrow_book(library, "The Great Gatsby")
    borrow_book(library, "python crash course")           # should say unavailable
    borrow_book(library, "Nonexistent Book")
    
    return_book(library, "The Great Gatsby")
    return_book(library, "python crash course")           # should say no borrowed copies
    
    print("Available books now:", available_books(library))