package weather;

import weather.subscribers.CurrentConditionsDisplay;
import weather.subscribers.ForecastDisplay;
import weather.subscribers.StatisticsDisplay;

public class WeatherStation {

	private WeatherData weatherData;
	private CurrentConditionsDisplay currentConditionsDisplay;
	private StatisticsDisplay statisticsDisplay;
	private ForecastDisplay forecastDisplay;

	public WeatherStation() {
		weatherData = new WeatherData();

		// Create the observers (displays)
		currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);
		statisticsDisplay = new StatisticsDisplay(weatherData);
		forecastDisplay = new ForecastDisplay(weatherData);

	}

	public void simulateWeatherChanges() {
		// Simulate changes in weather data
		weatherData.setMeasurements(75, 65, 30.4f);
		weatherData.setMeasurements(80, 70, 29.2f);
		weatherData.setMeasurements(78, 68, 29.5f);

		// Remove an observer
		weatherData.removeObserver(statisticsDisplay);

		// Simulate more changes
		weatherData.setMeasurements(82, 72, 30.3f);

		currentConditionsDisplay.display();

		// Add the observer back
		weatherData.registerObserver(statisticsDisplay);

		// Simulate one final change
		weatherData.setMeasurements(76, 66, 29.9f);

		forecastDisplay.display();

	}
}
