import WazeRouteCalculator
from csv import writer
import datetime
import pytz 


# github: https://github.com/jd2012/Waze-Traffic-Calculator

from_address = ["Galesburg, IL", "Bloomington, IL", "Lincoln, IL", "Peoria, IL", "Lincoln, IL", "El Paso, IL", "Pontiac, IL", "40.6270229, -89.5019788"]
to_address = ["Peoria, IL", "Peoria, IL", "Peoria, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "40.7355303, -89.6706033"]
region = 'US'
header_row = ["From", "To", "Travel Time"]
route_time = []


def pick_format():
  global fp
  print("Choose the format to print to the console:\n\t(1) Times inline with context\n\t(2) Comma seperated times and context\n\t(3) Just times\n\t(4) Write to CSV file")
  fp = input("Choose format [1,2,3,4]: ")
  check_format()

def check_format():
  if fp in {"1", "2", "3", "4"}:
    print_times()
  else:
    print('\a')
    print("Error: Invalid Format")
    pick_format()

def current_time():
  utc_now = pytz.utc.localize(datetime.datetime.utcnow())
  time_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  print("Traffic at "+time_now.strftime("%I:%M %p %Z")+"\n")

def get_times():
  current_time()
  for i in range(8):
    route = WazeRouteCalculator.WazeRouteCalculator(from_address[i], to_address[i], region)
    route_time_item, route_distance = route.calc_route_info()
    route_time.append(route_time_item)
    print("%.2f" % (route_time[i]))
  diff_format()

def diff_format():
  df = input("\nPress enter to get traffic times again. Type 1 to print the results in a different format: ")
  if df == "1":
    pick_format()
  elif df == "0":
    print("\n\nExiting...\n")
    return
  else:
    print("\n")
    get_times() 

def print_times():
  if fp in {"1", "2", "3"}:
    current_time()
    for i in range(8):
      if fp == "1":
        print("From %s to %s:\t %.2f minutes" % (from_address[i], to_address[i], route_time[i]))
      elif fp == "2":
        print("%s,%s,%.2f" % (from_address[i], to_address[i], route_time[i]))
      elif fp == "3":
        print("%.2f" % (route_time[i]))
  elif fp == "4":
      write_times()
  else:
    print("Error: Please try again")
    return
  diff_format()

def write_times():
  with open('traffictimes.csv', 'w', newline='') as file:
    w = writer(file)
    w.writerow(header_row)
    formatted_route_time = "{:.2f}"
    for i in range(8):
      w.writerow((from_address[i], to_address[i], formatted_route_time.format(route_time[i])))
  print("\nTimes written to traffictimes.csv\n")

get_times()
