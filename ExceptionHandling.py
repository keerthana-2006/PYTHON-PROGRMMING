# Exception Handling
#Explanation: Exception handling allows graceful handling of runtime errors, preventing program crashes.

#Basic Exception Handling

# Try-except block
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions in one except
try:
    risky_operation()
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

# Generic exception (use sparingly)
try:
    something_risky()
except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")

# Try-except-else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero")
else:
    print(f"Result: {result}")  # Executes if no exception

# Try-except-else-finally
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(f"File content: {content}")
finally:
    # Always executes (for cleanup)
    if 'file' in locals():
        file.close()
    print("Cleanup complete")
