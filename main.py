import WazeRouteCalculator
from csv import writer
from datetime import datetime

from_address = ["Galesburg, IL", "Bloomington, IL", "Lincoln, IL", "Peoria, IL", "Lincoln, IL", "El Paso, IL", "Pontiac, IL", "40.6270229, -89.5019788"]
to_address = ["Peoria, IL", "Peoria, IL", "Peoria, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "40.7355303, -89.6706033"]
region = 'US'

with open('traffictimes.csv', 'w', newline='') as file:
  w = writer(file)
  for i in range(8):
    route = WazeRouteCalculator.WazeRouteCalculator(from_address[i], to_address[i], region)
    route_time, route_distance = route.calc_route_info()
    print("From %s to %s:\t %.2f minutes" % (from_address[i], to_address[i], route_time))
    formatted_route_time = "{:.2f}"
    w.writerow((from_address[i], to_address[i], formatted_route_time.format(route_time)))
