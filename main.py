import WazeRouteCalculator
import logging



from_address = 'Budapest, Hungary'
to_address = 'Gyor, Hungary'
region = 'EU'
route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
route_time, route_distance = route.calc_route_info()
print("Time %.2f minutes, distance %.2f km." % (route_time, route_distance))