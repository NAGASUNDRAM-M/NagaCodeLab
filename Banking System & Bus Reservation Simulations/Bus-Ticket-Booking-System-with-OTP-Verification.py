import random

# Welcome and Journey Selection
name = input("Enter your name: ")
print("Welcome", name, "To Your Comfort Journey!")

# Available Journeys
a = "Chennai to Madurai"
b = "Madurai to Chennai"
c = "Madurai to Viruthunagar"

print("1:", a)
print("2:", b)
print("3:", c)

# Journey Selection Loop
while True:
    try:
        n = int(input("Select your journey (1/2/3): "))
        if n == 1:
            print(a)
            route = a
            break
        elif n == 2:
            print(b)
            route = b
            break
        elif n == 3:
            print(c)
            route = c
            break
        else:
            print("Invalid journey selection. Please choose again.")
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")

# Bus Type Selection
print("1: Non-AC 500")
print("2: AC 900")

while True:
    try:
        bus_type = int(input("Select bus type (1 for Non-AC, 2 for AC): "))
        if bus_type == 1:
            print("Non-AC 500")
            privilege = "Non-AC 500"
            seat_rate = 500
            break
        elif bus_type == 2:
            print("AC 900")
            privilege = "AC 900"
            seat_rate = 900
            break
        else:
            print("Invalid bus type. Please choose again.")
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")

# Travels Selection
print("1. KP TRAVELS")
print("2. YOLO TRAVELS")

while True:
    try:
        bus_name = int(input("Select Your Bus (1/2): "))
        if bus_name == 1:
            print("KP TRAVELS")
            Travels = "KP TRAVELS"
            break
        elif bus_name == 2:
            print("YOLO TRAVELS")
            Travels = "YOLO TRAVELS"
            break
        else:
            print("Invalid travel selection. Please choose again.")
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")

# Seat Booking
seat_capacity = 25
print("Total seat capacity:", seat_capacity)

while True:
    try:
        booking_seat = int(input("Enter number of seats to book: "))
        if 1 <= booking_seat <= seat_capacity:
            print("Your seat(s) is/are booked.")
            total_rate = booking_seat * seat_rate
            seat_capacity -= booking_seat
            print(f"Total amount: {total_rate}")
            print(f"Remaining seat capacity: {seat_capacity}")
            
            # Generate and display OTP
            otp = random.randint(1000, 9999)
            print(f"Your OTP for seat confirmation is: {otp}")
            
            # Verify OTP
            while True:
                try:
                    entered_otp = int(input("Enter the OTP to confirm your booking: "))
                    if entered_otp == otp:
                        print("Booking confirmed successfully!")
                        break
                    else:
                        print("Invalid OTP. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid 4-digit OTP.")
            break
        else:
            print(f"Invalid number of seats. Available capacity: {seat_capacity}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Passenger Details
passengers = []
for i in range(1, booking_seat + 1):
    passenger_name = input(f"Enter the name of passenger {i}: ")
    while True:
        try:
            passenger_age = int(input(f"Enter the age of passenger {i}: "))
            break
        except ValueError:
            print("Invalid age. Please enter a valid number.")
    passengers.append({"name": passenger_name, "age": passenger_age})

print("Passengers and their details:")
for passenger in passengers:
    print(f"Name: {passenger['name']}, Age: {passenger['age']}")

# Post-Booking Options
while True:
    print("\n1. Cancel Seat(s)\n2. Show Booking Details\n3. Exit")
    try:
        select = int(input("Select your choice: "))
        if select == 1:
            cancelling_seat = int(input("Enter number of seats to cancel: "))
            if 1 <= cancelling_seat <= booking_seat:
                booking_seat -= cancelling_seat
                seat_capacity += cancelling_seat
                total_rate -= cancelling_seat * seat_rate
                print(f"{cancelling_seat} seat(s) cancelled.")
                print(f"Updated seat capacity: {seat_capacity}")
            else:
                print(f"Invalid number of seats. You have {booking_seat} booked seats.")
        elif select == 2:
            print("\nYour Booking Details:")
            print("Journey:", route)
            print("Privilege:", privilege)
            print("Travels:", Travels)
            print("Number of booked seats:", booking_seat)
            print("Total amount:", total_rate)
            print("Passenger List:")
            for passenger in passengers:
                print(f"Name: {passenger['name']}, Age: {passenger['age']}")
        elif select == 3:
            print("Thanks for visiting! Have a safe journey!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
