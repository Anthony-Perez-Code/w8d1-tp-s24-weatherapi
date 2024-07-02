# w8d1-tp-s24-weatherapi

An API to retrieve the current weather conditions for location based on zip code.

# WELCOME TO THE SIMPLEST WEATHER API

This API takes the input of the user and returns back basic weather information about that area, including the temperature in Fahrenheit, the current condition (sunny, cloudy, etc.), the humidity level, the "feels like" condition, and wind speeds.

# USING THIS API

To use this API, simply send a GET request to the following route:

http://127.0.0.1:5000/weather/<area>

<area> is the location for which you seek the weather. You may enter an area based on city name or zip code.

# ERROR

If there is not information for the area sought, a meesage will be passed to inform the user.

# EXAMPLES

1. http://127.0.0.1:5000/weather/brooklyn
   Returns the weather for Brooklyn, NY.

2. http://127.0.0.1:5000/weather/32013
   Returns the weather for Day, Florida.

3. http://127.0.0.1:5000/weather/london
   Returns the weather for London, City of London, Greater London.
