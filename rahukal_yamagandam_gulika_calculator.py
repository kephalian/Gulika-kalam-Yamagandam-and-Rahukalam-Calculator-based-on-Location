
import datetime
from suntime import Sun
from geopy.geocoders import Nominatim
import PySimpleGUI as sg
sg.theme("material 2")
# Define the time units for each weekday
rahukaal_units = {
    "Sunday": 8,
    "Monday": 2,
    "Tuesday": 7,
    "Wednesday": 5,
    "Thursday": 6,
    "Friday": 4,
    "Saturday": 3,
}


# Define the time units for each weekday
gulikakaal_units = {
    "Sunday": 7,
    "Monday": 6,
    "Tuesday": 5,
    "Wednesday": 4,
    "Thursday": 3,
    "Friday": 2,
    "Saturday": 1,
}
# Define the time units for each weekday
yamagandam_units = {
    "Sunday": 5,
    "Monday": 4,
    "Tuesday": 3,
    "Wednesday": 2,
    "Thursday": 1,
    "Friday": 7,
    "Saturday": 6,
}

# Function to calculate Gulikakaal
def calculate_yamagandam(day_of_week, sunrise_time, sunset_time):
    # Convert sunrise and sunset times to datetime objects
    sunrise = datetime.datetime.strptime(sunrise_time, "%H:%M")
    sunset = datetime.datetime.strptime(sunset_time, "%H:%M")

    # Calculate the total duration of daylight in minutes
    daylight_duration = (sunset - sunrise).total_seconds() / 60

    # Calculate the duration of each Rahukaal unit
    unit_duration = daylight_duration / 8

    # Calculate the Rahukaal start and end times
    start_time = sunrise + datetime.timedelta(minutes=(yamagandam_units[day_of_week] - 1) * unit_duration)
    end_time = start_time + datetime.timedelta(minutes=unit_duration)

    return start_time.strftime("%H:%M"), end_time.strftime("%H:%M")
    
    
# Function to calculate Gulikakaal
def calculate_gulikakaal(day_of_week, sunrise_time, sunset_time):
    # Convert sunrise and sunset times to datetime objects
    sunrise = datetime.datetime.strptime(sunrise_time, "%H:%M")
    sunset = datetime.datetime.strptime(sunset_time, "%H:%M")

    # Calculate the total duration of daylight in minutes
    daylight_duration = (sunset - sunrise).total_seconds() / 60

    # Calculate the duration of each Rahukaal unit
    unit_duration = daylight_duration / 8

    # Calculate the Rahukaal start and end times
    start_time = sunrise + datetime.timedelta(minutes=(gulikakaal_units[day_of_week] - 1) * unit_duration)
    end_time = start_time + datetime.timedelta(minutes=unit_duration)

    return start_time.strftime("%H:%M"), end_time.strftime("%H:%M")
    
# Function to calculate Rahukaal
def calculate_rahukaal(day_of_week, sunrise_time, sunset_time):
    # Convert sunrise and sunset times to datetime objects
    sunrise = datetime.datetime.strptime(sunrise_time, "%H:%M")
    sunset = datetime.datetime.strptime(sunset_time, "%H:%M")

    # Calculate the total duration of daylight in minutes
    daylight_duration = (sunset - sunrise).total_seconds() / 60

    # Calculate the duration of each Rahukaal unit
    unit_duration = daylight_duration / 8

    # Calculate the Rahukaal start and end times
    start_time = sunrise + datetime.timedelta(minutes=(rahukaal_units[day_of_week] - 1) * unit_duration)
    end_time = start_time + datetime.timedelta(minutes=unit_duration)

    return start_time.strftime("%H:%M"), end_time.strftime("%H:%M")

# Function to calculate sunrise and sunset times
def calculate_sunrise_sunset(place):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place)
    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)
    today = datetime.date.today()
    sunrise = sun.get_local_sunrise_time(today)
    sunset = sun.get_local_sunset_time(today)
    return sunrise.strftime('%H:%M'), sunset.strftime('%H:%M')


layout = [
  [sg.Text("Guliga, Yamagandam, Rahukal Calculator \nby Dr. Santhosh Kumar Rajamani",font=('Verdana', 9, 'bold'), background_color='yellow'),],
    [sg.Text("Enter a place:"), ],
    [sg.Input(default_text='pune', size=(20,1), key="place")],
    [sg.Button("Calculate Sunrise and Sunset"), ],[sg.Button("Calculate Rahukaal"), ],
    [sg.Button("Calculate Gulikakaal"),],
    [sg.Button("Calculate Yamagandam")],
# Define the layout of the GUI
#layout = [
#    [sg.Text("Enter a place:"), sg.InputText(key="place")],
#    [sg.Button("Calculate Sunrise and Sunset"), ],[sg.Button("Calculate Rahukaal"), ],
#    [sg.Button("Calculate Gulikakaal"), ],
#    [sg.Button("Calculate Yamagandam"), ],
#    [sg.Button("Exit")],
    [sg.Output(size=(40, 10))]
]

window = sg.Window("Sunrise and Sunset Calculator", layout)

# List of named places
named_places = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Calculate Sunrise and Sunset":
        place = values["place"]
        if place:
            sunrise, sunset = calculate_sunrise_sunset(place)
            print(f"Sunrise at {place}: {sunrise}")
            print(f"Sunset at {place}: {sunset}")
            #named_places.append(place)
            
    elif event == "Calculate Yamagandam":
        place = values["place"]
        if place:
            day_of_week = datetime.datetime.now().strftime("%A")
            sunrise, sunset = calculate_sunrise_sunset(place)
            yamagandam_start, yamagandam_end = calculate_yamagandam(day_of_week, sunrise, sunset)
            print(f"Yamagandam on {day_of_week} \n at {place}: {yamagandam_start} - {yamagandam_end}")
                 
    elif event == "Calculate Gulikakaal":
        place = values["place"]
        if place:
            day_of_week = datetime.datetime.now().strftime("%A")
            sunrise, sunset = calculate_sunrise_sunset(place)
            gulikakaal_start, gulikakaal_end = calculate_gulikakaal(day_of_week, sunrise, sunset)
            print(f"Gulikakal on {day_of_week} \n at {place}: {gulikakaal_start} - {gulikakaal_end}")
            
    elif event == "Calculate Rahukaal":
        place = values["place"]
        if place:
            day_of_week = datetime.datetime.now().strftime("%A")
            sunrise, sunset = calculate_sunrise_sunset(place)
            rahukaal_start, rahukaal_end = calculate_rahukaal(day_of_week, sunrise, sunset)
            print(f"Rahukaal on {day_of_week} \n at {place}: {rahukaal_start} - {rahukaal_end}")
            
    #elif event == "Show Places":
#        if named_places:
#            sg.popup_scrolled('\n'.join(named_places), title='Named Places')
#        else:
            #sg.popup('No named places yet.')

window.close()
