class Flight:
	#flight_list=[]
	def __init__(self,name,max_seats):
		#flight_list=[]	
		self.name=name
		self.max_seats=max_seats
		self.seatsamt=0
		self.bookedseats=[]
		self.adminPIN=0
		self.vehicle_name="Flight"
		self.booked=False
		#flight_list.append(self.name)	

	def get_name(self):
		return self.name
	def change_name(self,name):
		self.name=name
	def get_maxSeats(self): 
		return self.max_seats
	def set_maxSeats(self,seats):
		self.max_seats=seats
