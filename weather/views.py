from django.shortcuts import render,redirect
import requests

def weather(request):
	"""Weather api view;user request city weather then api provider response with weather conditions data for this city"""
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=917fe0498a0cf04f95e2814b27d764c8'
	city_name = request.GET.get('q', None)
	weather_data =[]
	if city_name:
		r = requests.get(url.format(city_name)).json()
		try:
			city_weather = {
	            'city' : city_name,
	            'temperature' : r['main']['temp'],
	            'description' : r['weather'][0]['description'],
	            'icon' : r['weather'][0]['icon'],
	        }
		
			weather_data.append(city_weather)
		except KeyError:
			messages.error(request,f"City Not Found,Please Enter Valid City Name")
	
	print(weather_data)
	context={'weather_data':weather_data}
	return render(request,'weather.html', context)

