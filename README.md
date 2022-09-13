# Vacation-Weather-Dashboard

## Dashboard

[Click here to view the live Dashboard!](https://matin-n-vacation-weather-dashboard-streamlit-app-k4h6j7.streamlitapp.com/)

## Project Overview

A interactive dashboard to visualize weather conditions and possible cities for taking a vacation.

## Data

The app uses parsed historical data from [World Weather Analysis](https://github.com/matin-n/World-Weather-Analysis). The weather data is for December 2, 2021. The data was obtained from [OpenWeatherMap API](https://openweathermap.org/api), and the city locations were obtained from the [MaxMind World Cities Database](http://www.maxmind.com/en/free-world-cities-database) using the [CitiPy](https://github.com/wingchen/citipy) library. View the original [World Weather Analysis](https://github.com/matin-n/World-Weather-Analysis) repository for more information on how the data was collected and parsed.

## Resources

- Data Source: [`cities.csv`](cities.csv)
- Libraries: [`Pandas`](https://pandas.pydata.org/), [`Plotly`](https://plotly.com/graphing-libraries/), [`Streamlit`](https://streamlit.io/), [`StatsModels`](https://www.statsmodels.org/stable/index.html)
- Additional: [Mapbox](https://www.mapbox.com/), [OpenWeatherMap](https://openweathermap.org/api)
- Source Code: [`streamlit_app.py`](streamlit_app.py)
