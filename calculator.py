def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a / b


def modulus(a, b):
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a % b


def power(a, b):
	return a ** b


def prompt_number(prompt):
	while True:
		s = input(prompt).strip()
		if s.lower() in ("q", "quit", "exit"):
			raise SystemExit
		try:
			return float(s)
		except ValueError:
			print("Please enter a valid number or 'q' to quit.")


def main():
	ops = {
		"1": ("Add", add),
		"2": ("Subtract", subtract),
		"3": ("Multiply", multiply),
		"4": ("Divide", divide),
		"5": ("Modulus", modulus),
		"6": ("Power", power),
	}

	menu = """
Simple Python Calculator

Choose an operation:
1) Add
2) Subtract
3) Multiply
4) Divide
5) Modulus
6) Power
Type 'q' to quit.
"""

	try:
		while True:
			print(menu)
			choice = input("Operation (1-6) or 'q' to quit: ").strip().lower()
			if choice in ("q", "quit", "exit"):
				break
			if choice not in ops:
				print("Invalid choice — pick 1-6 or 'q'.")
				continue

			try:
				a = prompt_number("Enter first number: ")
				b = prompt_number("Enter second number: ")
			except SystemExit:
				break

			try:
				name, fn = ops[choice]
				result = fn(a, b)
			except ZeroDivisionError:
				print("Error: division by zero.")
				continue

			print(f"{name} result: {result}\n")

			again = input("Another calculation? [Y/n]: ").strip().lower()
			if again and again[0] == "n":
				break
	except KeyboardInterrupt:
		print("\nGoodbye.")


if __name__ == "__main__":
	main()
