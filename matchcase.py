# match-case (similar to switch)
def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print(get_day_type("Monday"))    # Weekday
print(get_day_type("Sunday"))    # Weekend

# Pattern matching with structures
def process_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y):
            return f"Point at ({x},{y})"
        case _:
            return "Not a point"

print(process_point((0, 5)))   # On Y-axis at y=5
