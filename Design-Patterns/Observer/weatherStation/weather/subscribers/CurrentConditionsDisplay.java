package weather.subscribers;

import observers.*;
import weather.WeatherData;

public class CurrentConditionsDisplay implements Observer, Subscriber {
	private WeatherData weatherData;
	private float temperature;
	private float humidity;

	public CurrentConditionsDisplay(WeatherData weatherData) {
		this.weatherData = weatherData;
		weatherData.registerObserver(this);
	}

	public void update(float temp, float humidity, float pressure) {
		this.temperature = temp;
		this.humidity = humidity;
		display();
	}

	public void display() {
		System.out.println("Current conditions: " + temperature
				+ "F degrees and " + humidity + "% humidity");
	}

	// Method to unregister from WeatherData
	public void unregister() {
		weatherData.removeObserver(this);
	}
}