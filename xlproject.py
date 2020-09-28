import WazeRouteCalculator
import xlwings as xw
import pyautogui as pag

# github: https://github.com/jd2012/Waze-Traffic-Calculator

wb = xw.Book.caller()
sht = wb.sheets[0]

from_address = ["Galesburg, IL", "Bloomington, IL", "Lincoln, IL", "Peoria, IL", "Lincoln, IL", "El Paso, IL", "Pontiac, IL", "40.6270229, -89.5019788"]
to_address = ["Peoria, IL", "Peoria, IL", "Peoria, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "Bloomington, IL", "40.7355303, -89.6706033"]
route_time = []
region = 'US'


def getTraffic():
    route_time = []
    for i in range(8):
        route = WazeRouteCalculator.WazeRouteCalculator(from_address[i], to_address[i], region)
        route_time.append(route.calc_route_info()[0])
    xw.Range('C2').options(transpose=True).value = route_time

def resetDocument():
    sht['A1'].value = "From"
    sht['B1'].value = "To"
    sht['C1'].value = "Time"
    xw.Range('A2').options(transpose=True).value = from_address
    xw.Range('B2').options(transpose=True).value = to_address

def main():
    A1_blank = sht['A1'].value
    if A1_blank == "":
        confirm_reset = pag.confirm(text='It appaers that the document is not setup correctly. Would you like to reset the document?', title='Possible Error', buttons=['Fine, reset the document', 'Nah, I\'m gonna continue and then tell Joseph his program broke later', 'Cancel, cuz I don\'t want to hit the other buttons'])
        if confirm_reset == 'Fine, reset the document':
            resetDocument()
        elif confirm_reset == 'Nah, I\'m gonna continue and then tell Joseph his program broke later':
            getTraffic()
        elif confirm_reset == 'Cancel, cuz I don\'t want to hit the other buttons':
            return
        else:
            pag.alert(text='An error has occured. Exiting the program.', title='ERROR', button='OK')
            return
    else:
        getTraffic()

if __name__ == "__main__":
    xw.Book("xlproject.xlsm").set_mock_caller()
    main()
