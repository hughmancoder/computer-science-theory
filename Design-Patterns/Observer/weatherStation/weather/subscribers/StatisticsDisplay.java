package weather.subscribers;

import observers.*;
import weather.WeatherData;

public class StatisticsDisplay implements Observer, Subscriber {
	private float maxTemp = 0.0f;
	private float minTemp = 200;
	private float tempSum = 0.0f;
	private int numReadings;

	public StatisticsDisplay(WeatherData weatherData) {
		weatherData.registerObserver(this);
	}

	@Override
	public void update(float temp, float humidity, float pressure) {
		tempSum += temp;
		numReadings++;

		if (temp > maxTemp) {
			maxTemp = temp;
		}

		if (temp < minTemp) {
			minTemp = temp;
		}

		display();
	}

	public void display() {
		System.out.println("Avg/Max/Min temperature = " + (tempSum / numReadings)
				+ "/" + maxTemp + "/" + minTemp);
	}
}
