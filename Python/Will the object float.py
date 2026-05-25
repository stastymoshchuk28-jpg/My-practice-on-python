g = 9.81  # speed of the free fall (m/s^2)
rho = 1000  # water thickness (kg/m^3)

M = int(input("Enter the mass of the object (kg): "))

V = int(input("Enter the volume of displaced water (m^3): "))

FG = M*g
FA = rho*V*g
if FG > FA:
    print("The object will sink.")
else:
    print("The object will float.")