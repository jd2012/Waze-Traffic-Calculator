import WazeRouteCalculator
from csv import writer 

# github: https://github.com/jd2012/Waze-Traffic-Calculator

from_address = ["Galesburg, IL", "Bloomington, IL", "Lincoln, IL", "Peoria, IL", "Lincoln, IL", "El Paso, IL", "Pontiac, IL", "40.6270229, -89.5019788"]
to_address = ["Peoria, IL", "Peoria, IL", "Peoria, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "40.7355303, -89.6706033"]
region = 'US'
header_row = ["From", "To", "Travel Time"]


def pick_format():
  global fp
  fp = input("Choose format [1,2,3]: ")
  check_format()


def check_format():
  if fp in {"1", "2", "3"}:
    write_times()
  else:
    print('\a')
    print("Error: Invalid Format")
    pick_format()

def write_times():
  with open('traffictimes.csv', 'w', newline='') as file:
    w = writer(file)
    w.writerow(header_row)
    for i in range(8):
      route = WazeRouteCalculator.WazeRouteCalculator(from_address[i], to_address[i], region)
      route_time, route_distance = route.calc_route_info()
      if fp == 1:
        print("From %s to %s:\t %.2f minutes" % (from_address[i], to_address[i], route_time))
      elif fp == 2:
        print("%s,%s,%.2f" % (from_address[i], to_address[i], route_time))
      elif fp == 3:
        print("%.2f" % (route_time))
      else:
        print("Error: Please try again")
      

      formatted_route_time = "{:.2f}"
      w.writerow((from_address[i], to_address[i], formatted_route_time.format(route_time)))

print("Choose the format to print to the console:\n\t(1) Times inline with context\n\t(2) Comma seperated times and context \n\t(3) Just times")
pick_format()
