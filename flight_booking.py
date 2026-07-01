import book_flight

import access_data as ad


def main(Flight, flight_list):
    while True:
        role = (
            input(
                f"\nWelcome To {Flight.name}!\nMAIN MENU:\nADMIN (a)\nPassenger (p)\nBusiness Man (b)\nDisplay (d)\n(Exit) (Q)\nEnter Your Role/Option: "
            )
            .lower()
            .replace(" ", "")
        )

        if role == "admin" or role == "a":
            if Flight.adminPIN == 0:
                while True:
                    print("Please Create A PIN")
                    try:
                        adminPIN = int(input())
                    except ValueError:
                        print("Sorry! PIN can only consist of numbers!")
                        continue
                    else:
                        if adminPIN <= 0:
                            print("Invalid PIN")
                            continue
                        elif len(str(adminPIN)) != 6:
                            print("Sorry! PIN must be 6 Digits")
                        else:
                            Flight.adminPIN = adminPIN
                            break
                while True:
                    try:
                        seatsamt = int(input("How many seats do you want to run: "))
                    except ValueError:
                        print("Invalid Number of Seats!")
                        continue
                    else:
                        if seatsamt < 0:
                            print("Invalid Number of Seats!")
                            continue
                    if seatsamt <= Flight.max_seatsamt:
                        print(f"Allocated {seatsamt} seats Successfully")
                        Flight.seatsamt = seatsamt
                        break
                    else:
                        print("Over Max Seats! Please Enter Less Amount")
                        continue
            else:
                print("Please Enter The PIN")
                PIN = input()
                if str(Flight.adminPIN) == PIN:
                    pf = input(
                        "Type (E) to edit no. of seats or (Q) to return back to main menu: "
                    ).lower()
                    if pf == "e":
                        while True:
                            try:
                                seatsamt = int(
                                    input("How many seats do you want to run: ")
                                )
                            except ValueError:
                                print("Invalid Number of Seats!")
                                continue
                            if seatsamt <= Flight.max_seatsamt:
                                print(f"Allocated {seatsamt} seats Successfully")
                                Flight.seatsamt = seatsamt
                                Flight.bookedseats.clear()
                                break
                            else:
                                print("Over Max Seats! Please Enter Less Amount")
                                continue
                    elif pf == "q":
                        continue
                    else:
                        print("ERROR")
                else:
                    print("Incorrect PIN")

        elif role == "passenger" or role == "p":
            print("Welcome! Please Enter Your Name:")
            name = input()

            booked = False

            while True:
                try:
                    seats = int(input("How many seats do you want to book: "))
                except ValueError:
                    print("Invalid Number of Seats!")
                    continue

                if seats < 0:
                    print("Invalid Number of Seats!")
                    continue
                if Flight.seatsamt == 0 and not Flight.booked:
                    print("Sorry! Seats aren't allocated yet")
                    break
                elif Flight.seatsamt == 0 and seats > Flight.seatsamt:
                    print("Sorry! Seats are Fully Booked!")
                    print(f"Why not try our other {len(flight_list)-1} Flights!")
                    y = 1
                    for flight in flight_list:
                        if flight != Flight.name:
                            print(f"{y}.{Flight.name}")
                            y += 1
                    break

                elif Flight.seatsamt == 1 and seats > Flight.seatsamt:
                    print(f"Sorry! There is only {Flight.seatsamt} seat available")

                elif Flight.seatsamt >= seats:
                    your_seats = []
                    count = 0
                    x = 1
                    while count < seats:
                        if x in Flight.bookedseats:
                            x += 1
                            continue
                        else:
                            if len(str(x)) == 1:
                                your_seats.append(f"00{x}")
                                Flight.bookedseats.append(x)
                            elif len(str(x)) == 2:
                                your_seats.append(f"0{x}")
                                Flight.bookedseats.append(x)
                            else:
                                your_seats.append(str(x))
                                Flight.bookedseats.append(x)
                            x += 1
                            count += 1
                    book_flight.bookFlight(
                        name=name, flight_name=flight.name, your_seats=your_seats
                    )
                    seatsamt -= seats
                    booked = True
                    break

                elif Flight.seatsamt > 1 and seats > Flight.seatsamt:
                    print(f"Sorry! There are only {Flight.seatsamt} seats available")
                    continue

                else:
                    continue

        elif role == "display" or role == "d":
            if Flight.seatsamt == 0 and not booked:
                print("Seats aren't allocated yet")
            elif Flight.seatsamt == 1:
                print(f"There is {seatsamt} Seat Available")
            elif Flight.seatsamt == 0:
                print("Seats Fully Booked")
            else:
                print(f"There Are {Flight.seatsamt} Seats Available")

        elif role == "exit" or role == "q":
            ad.saveData(f"{Flight.name}.dat", Flight)

        elif role == "businessman" or role == "b":
            print("Role not available yet")

        else:
            print("Oops! Invalid Role/Option!")
