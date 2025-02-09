import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if city:
        api_key = "your_api_key_here"  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            result_label.config(text=f"Weather: {weather}\nTemperature: {temperature}°C")
        else:
            messagebox.showerror("Error", "City not found")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()