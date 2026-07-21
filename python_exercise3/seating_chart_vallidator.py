def seating_report(chart):
    if not chart:
        return {
            "total_seats": 0,
            "occupied": 0,
            "empty_rows": []
        }
    
    total_seats = 0
    occupied = 0
    empty_rows = []
    
    # Nested loops to go through each row and seat
    for row_idx in range(len(chart)):
        row = chart[row_idx]
        row_is_empty = True
        row_occupied_count = 0
        
        for seat in row:
            total_seats += 1
            if seat is not None:
                occupied += 1
                row_occupied_count += 1
                row_is_empty = False
        
        # If no occupied seats in this row, it's empty
        if row_occupied_count == 0:
            empty_rows.append(row_idx)
    
    return {
        "total_seats": total_seats,
        "occupied": occupied,
        "empty_rows": empty_rows
    }


# Example test
if __name__ == "__main__":
    chart = [
        ["Alice", None, "Bob"],
        [None, None, None],
        ["Charlie", "David", None],
        [None, None, None]
    ]
    
    result = seating_report(chart)
    print(result)