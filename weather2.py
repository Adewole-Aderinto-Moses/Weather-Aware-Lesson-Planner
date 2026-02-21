import urllib.request
import json
from rich.console import Console

console = Console()

#getting my weather api key from my_weather_api_key
with open("my_weather_api_key.json", "r") as f:
	my_api_key = json.load(f)

key = my_api_key[0]
def get_weather(city_name):
    console.print(f"[italic yellow]Connecting to weather satellites for {city_name}...[/italic yellow]")
    api_key = key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Using the built-in library instead of 'requests'
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].lower()
            
            console.print(f"\n[bold yellow]Current Weather in {city_name}:[/bold yellow]")
            console.print(f"Temperature: {temp}°C | Condition: {weather_desc}")
            
            # --- TEACHER'S LOGIC ---
            if "rain" in weather_desc or "drizzle" in weather_desc:
                console.print("\n[bold cyan]💡 Lesson Plan:[/bold cyan] Rainy day! Indoor Tech Lesson.")
            else:
                console.print("\n[bold green]💡 Lesson Plan:[/bold green] Clear skies! Outdoor Math Logic.\n")
                
    except Exception as e:
        console.print(f"[red]Error fetching weather: {e}[/red]")

while True:
	console.print(f"{' '*3}Clefnet Digital Solution Tutorial 2\n [yellow bold]Automated Weather & Lesson Plan Episode 1[bold yellow]\n ")
	get_city_name = input("Please Enter a Your City: ").capitalize()
	get_weather(get_city_name)
