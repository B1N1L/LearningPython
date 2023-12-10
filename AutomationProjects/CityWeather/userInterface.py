from main import weatherData 
import PySimpleGUI as sg 

output=""
layout = [
        sg.Text("Welcome to the City Weather UI", size=(30,3), text_color = 'black', font = ('Arial', 18))
    ],[
        sg.Text("Enter the city name"),
        sg.In(size=(25, 1), enable_events=True, key="-CITY-")
    ],[
        sg.Button("Submit")
    ],[
        sg.Text(size=(25,1), key="-WEATHER-", font = ('Times New Roman', 14))
        ]

window = sg.Window(title="Weather UI", layout=[layout], margins=(200, 100), background_color = '#808080')

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        output = weatherData(values["-CITY-"])
        window["-WEATHER-"].update(f"Weather Update: {output}")