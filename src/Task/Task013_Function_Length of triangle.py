# Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isosceles
# o/p = result in string - iso, eq, scalene

def triangle_type(side1, side2, side3):
    # Check if sides are positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid triangle"

    # Triangle inequality rule
    if (side1 + side2 <= side3 or
        side2 + side3 <= side1 or
        side1 + side3 <= side2):
        return "Invalid triangle"

    # Check triangle type
    if side1 == side2 == side3:
        return "eq"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "iso"
    else:
        return "scalene"


# Taking input from user
try:
    s1 = int(input("Enter side 1: "))
    s2 = int(input("Enter side 2: "))
    s3 = int(input("Enter side 3: "))

    result = triangle_type(s1, s2, s3)
    print("Triangle type:", result)

except ValueError:
    print("Please enter valid integers.")


# def triangle_type(a, b, c):
#     if min(a, b, c) <= 0:
#         return "Invalid"
#
#     if a + b <= c or b + c <= a or a + c <= b:
#         return "Invalid"
#
#     if a == b == c:
#         return "eq"
#     if a == b or b == c or a == c:
#         return "iso"
#     return "scalene"