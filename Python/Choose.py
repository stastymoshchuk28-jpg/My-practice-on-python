print("Welcome to the physics lab!")
print("Choose an action:")
print("1 - Calculate force using Newton's second law (F = m * a)")
print("2 - Calculate kinetic energy (E = 0.5 * m * v^2)")
print("3 - Calculate free fall velocity (v = sqrt(2 * g * h))")

diya = int(input("Enter action number (1, 2 or 3): "))
if diya > 3:
    print("Incorrect choice! Try again.")
else:
    if diya == 2:
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter velocity (m/s): "))
        E = 0.5 * m * v**2
        print(f"Kinetic Energy (E) = {E} J")
    else:
        if diya == 1:
            print("Error! This action is not implemented yet.")
        else:
            if diya == 3:
                print("Error! This action is not implemented yet.")