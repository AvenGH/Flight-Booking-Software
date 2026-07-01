'''
import importlib
book_flight = importlib.import_module('.book_flight', package='FlightBookingSoftware')
flight_booking = importlib.import_module('.flight_booking', package='FlightBookingSoftware')
_Flight_ = importlib.import_module('._Flight_', package='FlightBookingSoftware')
'''
import flight_booking
import _Flight_

import access_data as ad

print("Program Started!")

Flight1=_Flight_.Flight(name="British Airways",max_seats=45)
Flight2=_Flight_.Flight(name="Air India",max_seats=34)
Flight3=_Flight_.Flight(name="Emirates",max_seats=39)
		
while True: 
	print("\nWelcome!\nPlease Choose A Flight:\n1.British Airways\n2.Air India\n3.Emirates")
	flight=input("Enter Your Flight Option or Press (Q) to Exit: ").lower()
	flight=flight.replace(" ","")

	if flight=="britishairways" or flight=='1':
		flight_booking.main(Flight1,["British Airways","Air India","Emirates"])
	elif flight=="airindia" or flight=='2':
		flight_booking.main(Flight2,["British Airways","Air India","Emirates"])
	elif flight=="emirates" or flight=='3':
		flight_booking.main(Flight3,["British Airways","Air India","Emirates"])
	elif flight=="q":
		break
	else:
		print("Oops! Invalid Option")
		continue

print("Terminated Program")