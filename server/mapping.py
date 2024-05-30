weather_descriptions = {
    0: "clear",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "freezing fog",
    51: "light drizzle",
    53: "moderate drizzle",
    55: "heavy drizzle",
    56: "light freezing drizzle",
    57: "heavy freezing drizzle",
    61: "slight rain",
    63: "moderate rain",
    65: "heavy rain",
    66: "light freezing rain",
    67: "heavy freezing rain",
    71: "light snow",
    73: "moderate snow",
    75: "heavy snow",
    77: "icefall",
    80: "slight rain showers",
    81: "moderate rain showers",
    82: "heavy rain showers",
    85: "slight snow showers",
    86: "heavy snow showers",
    95: "thunderstorm",
}

weather_emojis = {
    0: "☀️",
    1: "🌤️",
    2: "⛅",
    3: "☁️",
    45: "🌫️",
    48: "❄️🌫️",
    51: "🌦️",
    53: "🌦️🌦️",
    55: "🌦️🌦️🌦️",
    56: "❄️🌦️",
    57: "❄️🌦️🌦️",
    61: "🌧️",
    63: "🌧️🌧️",
    65: "🌧️🌧️🌧️",
    66: "❄️🌧️",
    67: "❄️🌧️🌧️",
    71: "🌨️",
    73: "🌨️🌨️",
    75: "🌨️🌨️🌨️",
    77: "❄️❄️❄️",
    80: "☔",
    81: "🌧️☔",
    82: "🌧️🌧️☔",
    85: "🌨️☔",
    86: "🌨️🌨️☔",
    95: "🌩️",
}

def map_degree_to_direction(degree):
    if degree <= 15:
        return 'N'
    elif degree <= 35:
        return 'N/NE'
    elif degree <= 55:
        return 'NE'
    elif degree <= 75:
        return 'E/NE'
    elif degree <= 105:
        return 'E'
    elif degree <= 125:
        return 'E/SE'
    elif degree <= 145:
        return 'SE'
    elif degree <= 165:
        return 'S/SE'
    elif degree <= 195:
        return 'S'
    elif degree <= 215:
        return 'S/SW'
    elif degree <= 235:
        return 'SW'
    elif degree <= 255:
        return 'W/SW'
    elif degree <= 285:
        return 'W'
    elif degree <= 305:
        return 'W/NW'
    elif degree <= 325:
        return 'NW'
    elif degree <= 345:
        return 'N/NW'
    else:
        return 'N'
    
def map_moon_icon_and_phase(moon_lit,waxing): 
    # moon_lit = % of moon surface illuminated; waxing = boolean
    if moon_lit <= 3:
        moon_phase = "New Moon"
        moon_icon = "🌑"
    elif moon_lit <= 47:
        if waxing:
            moon_phase = "Waxing Crescent"
            moon_icon = "🌒"
        else:
            moon_phase = "Waning Crescent"
            moon_icon = "🌘"
    elif moon_lit <= 53:
        if waxing:
            moon_phase = "First Quarter"
            moon_icon = "🌓"
        else:
            moon_phase = "Last Quarter"
            moon_icon = "🌗"
    elif moon_lit <= 97:
        if waxing:
            moon_phase = "Waxing Gibbous"
            moon_icon = "🌔"
        else:
            moon_phase = "Waning Gibbous"
            moon_icon = "🌖"
    else:
        moon_phase = "Full Moon"
        moon_icon = "🌕"
    
    return {
        "moon_phase": moon_phase,
        "moon_icon": moon_icon,
    }