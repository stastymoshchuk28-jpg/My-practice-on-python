Height = float(input("Enter the height of the rocket in kilometers: "))

if Height < 200:
    print(f"For orbit at an altitude {Height} km, the required rocket speed is 7.8 km/s")
else:
    if Height < 500:
        print(f"For orbit at an altitude {Height} km, the required rocket speed is 8.5 km/s")
    else:
        if Height > 500:
            print(f"For orbit at an altitude {Height} km, the required rocket speed is 9.0 km/s")