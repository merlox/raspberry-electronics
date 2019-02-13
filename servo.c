#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define OFFSET_MS 3 // The unit of pulses is 0.1 miliseconds
#define SERVO_MIN_MS 5+OFFSET_MS
#define SERVO_MAX_MS 25+OFFSET_MS
#define servoPin 29

long mapRanges(long value, long fromMin, long fromMax, long toMin, long toMax) {
	return (toMax - toMin) * (value - fromMin) / (fromMax - fromMin) + toMin;
}

void servoInitialize(int pin) {
	softPwmCreate(pin, 0, 200);
}

// To rotate the servo from 0 to 180 degrees
void servoWrite(int pin, int angle) {
	if(angle > 180) angle = 180;
	if(angle < 0) angle = 0;
	softPwmWrite(pin, mapRanges(angle, 0, 180, SERVO_MIN_MS, SERVO_MAX_MS));
}

// To rotate the servo from 0 ms to 25 ms
void servoWriteMs(int pin, int ms) {
	if(ms > SERVO_MAX_MS) ms = SERVO_MAX_MS;
	if(ms < SERVO_MIN_MS) ms = SERVO_MIN_MS;
	softPwmWrite(pin, ms);
}

int main(void) {
	int i;
	if(wiringPiSetup() == -1) {
		printf("Setup wiringPi failed");
		return 1;
	}
	printf("Starting...\n");
	servoInitialize(servoPin);
	while(1) {
		// Rotate from 0 to 180 degrees
		for(i = SERVO_MIN_MS; i < SERVO_MAX_MS; i++) {
			servoWriteMs(servoPin, i);
			delay(10);
		}
		delay(500);
		for(i = SERVO_MAX_MS; i > SERVO_MIN_MS; i--) {
			servoWriteMs(servoPin, i);
			delay(10);
		}
		delay(500);
	}
	
	return 0;
}
