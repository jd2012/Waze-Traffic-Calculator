# Waze-Traffic-Calculator
#### The one-stop-shop for all your HOI traffic time needs

## About

Built using:
- Python 3
- [My Brain](https://github.com/jd2012)
- Python Package [Waze Route Caclulator](https://github.com/kovacsbalu/WazeRouteCalculator)

...but mostly my brain.

---

##### Built for the best and most accurate meteorologist in world. Check out her work at [Heart of Illinois ABC](https://www.hoiabc.com/weather)

---

## What It Do

Using the WazeRouteCalculator Python Package, the program request the travel time betweeen the locations bellow through the Waze API and and can return the results in various formats.  

| From                                           | To                                             |
| ---------------------------------------------- | ---------------------------------------------- |
| Galesburg, IL                                  | Peoria, IL                                     |
| Bloomington, IL                                | Peoria, IL                                     |
| Lincoln, IL                                    | Peoria, IL                                     |
| Peoria, IL                                     | Bloomington, IL                                |
| Lincoln, IL                                    | Bloomington, IL                                |
| Lincoln, IL                                    | Bloomington, IL                                |
| Pontiac, IL                                    | Bloomington, IL                                |
| 40.6270229, -89.5019788                        | 40.7355303, -89.6706033                        |

It can output the results in the following formats
| Format                                         | Example Output                                           |
| ---------------------------------------------- | -------------------------------------------------------- |
| Times inline with context                      | `From Galesburg, IL to Peoria, IL:        45.35 minutes` |          
| Comma seperated times and context              | `Galesburg, IL,Peoria, IL,45.35`                         |         
| Just times                                     | `45.35`                                                  |      
| Write to CSV file                              | `Times written to traffictimes.csv` found on [Repl.it](https://repl.it/@jd20121/Waze-Traffic-Calculator-1#traffictimes.csv) |        

## Why It Cool

- I built it
- ~~It works~~ sorta

