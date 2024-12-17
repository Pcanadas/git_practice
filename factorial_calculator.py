def get_factorial_input():
	try:
		number = int(input("Enter a number to calculate its factorial: "))
		if number < 0:
			print("Factorial is not defined for negative numbers.")
			return None
		return number
	except ValueError:
		print("Invalid input. Please enter an integer.")
		return None
	
def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = get_factorial_input() 
print(f"The factorial of {number} is {factorial(number)}") 


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(3) == 6
    assert factorial(7) == 5040
    assert factorial(4) == 24
    assert factorial(2) == 2
    assert factorial(6) == 720
    assert factorial(9) == 362880
    print("All tests passed successfully.")
	
test_factorial()