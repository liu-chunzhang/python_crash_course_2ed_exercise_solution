class Restaurant:

	def __init__(self, restaurant_name, cuisine_name):
		self.restaurant_name = restaurant_name
		self.cuisine_name = cuisine_name
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The name of this restaurant is {self.restaurant_name}.")
		print(f"The cuisine type of this restaurant is {self.cuisine_name}.")

	def open_restaurant(self):
		print("The restaurant is open.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment_number_served):
		self.number_served += increment_number_served