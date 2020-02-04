def calculate_area (radius):
	global area
    area = 3.14 * radius**2    return area

area = 0
calculate_area(10)
print("넓이:", area)
