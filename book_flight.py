import airportsdata

airports = airportsdata.load("IATA")  # key is ICAO code, the default
import sys

# sys.path.insert(1,"E:/Downloads/Python(2)/Modules")
# import access_data
import email_operations as email


def date_check(date):
    if date[0:1][0] == "0":
        dd = int(date[1])
    if date[2:3][0] == "0":
        mm = int(date[3])
    if date[4:5][0] == "0":
        return "False"
    dd = int(date[0:2])
    mm = int(date[2:4])
    yy = int(date[4:6])

    if dd > 28 and mm == 2:
        return "False"
    elif yy != 23:
        return "notavailable"
    elif dd > 31:
        return "False"
    elif dd == 31 and mm % 2 == 0 and mm != 8:
        return "False"
    elif (dd == 31 and mm % 2 != 0) and (mm == 9 or mm == 11):
        return "False"
    elif mm < 1 or mm > 12:
        return "False"
    else:
        DD = str(dd)
        MM = str(mm)
        YY = str(yy)
        if len(DD) == 1:
            DD = "0" + DD
        if len(MM) == 1:
            MM = "0" + MM
        flight_date = DD + "/" + MM + "/" + YY
        return flight_date


def write_confirmation_statement(
    flight_name, your_seats, confirm_date, origin_code, destination_code, name, email
):
    with open(
        f"FlightBookingSoftware/Confirmation Statements/{flight_name}{id(name)}.txt",
        "wt",
    ) as myfile:
        myfile.write(
            f"""
Dear {name},


Your {flight_name} Flight Has Successfully Been Booked.

Flying On: {confirm_date}

Origin: {airports[origin_code]['name']}, {airports[origin_code]['city']}, {airports[origin_code]['country']}

Destination: {airports[destination_code]['name']}, {airports[destination_code]['city']}, {airports[destination_code]['country']}

Number Of Passengers: {len(your_seats)}

Seat Numbers: {your_seats}


Any queries or information that you are unsure about, Please visit our website or contact us via phone/email.


Thanks,


{flight_name}

			"""
        )

    with open(
        f"FlightBookingSoftware/Confirmation Statements/{flight_name}{id(name)}.txt",
        "rb",
    ) as myfile:
        file_name = myfile.name
        host_email_address = "avenkumar54@gmail.com"
        host_password = "kkooyvvlqvsqtwrc"
        subject = "Flight Booked Successfully!"
        data = f"Hi {name}, Please See Attached, Your Flight Booking Details"
        subtype = "txt"
        email.send_email(
            file_name, email, host_email_address, subject, data, subtype, host_password
        )


def bookFlight(name, flight_name, your_seats):
    while True:
        email = input("Please Enter Your Email Address: ")
        origin_code = input("Enter The Origin Airport Code: ").upper()
        try:
            airports[origin_code]
        except KeyError:
            print("Invalid Origin Code!")
            continue
        else:
            while True:
                destination_code = input("Enter The Destination Airport Code: ").upper()
                try:
                    airports[destination_code]
                except KeyError:
                    print("Invalid Destination Code!")
                    continue
                else:
                    break
            while True:
                try:
                    date = int(input("Enter The Date Of Flight: "))
                except ValueError:
                    print("Invalid Date!")
                    continue
                else:
                    if date < 0:
                        print("Invalid Date!")
                        continue
                    date = str(date)
                    if len(date) == 5:
                        date = "0" + date
                    if len(date) == 6:
                        confirm_date = date_check(date)
                        if confirm_date == "False":
                            print("Invalid Date!")
                            continue
                        elif confirm_date == "notavailable":
                            print("Sorry! Only 2023 Flights Are Available!")
                            continue
                        else:
                            break
                    else:
                        print("Date Must be 6 Digits!")
                        continue

        write_confirmation_statement(
            flight_name=flight_name,
            your_seats=your_seats,
            confirm_date=confirm_date,
            origin_code=origin_code,
            destination_code=destination_code,
            name=name,
            email=email,
        )

        break
