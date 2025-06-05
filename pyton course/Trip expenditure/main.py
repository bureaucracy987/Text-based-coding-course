def hotel_cost(days):
  return 140*days
def plane_ride_cost(city):
  if "Charlotte"==city:
    return 183
  if "Tampa"==city:
    return 220
  if "Pittsburg"==city:
    return 299
  if "Los Angeles"==city:
    return 320
def rental_car_cost(days):
  if days>=7:
    return 40*days-50
  elif days>=3:
    return 40*days-20
  else:
    return 40*days
def trip_cost(days,city,spending_money):
  return rental_car_cost(days)+plane_ride_cost(city)+hotel_cost(days)+spending_money
print("Total cost of the trip",trip_cost(7,"Los Angeles",500))
print("Total cost of the trip",trip_cost(6,"Tampa",500))

  