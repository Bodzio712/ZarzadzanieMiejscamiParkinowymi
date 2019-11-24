#Libraries
import RPi.GPIO as GPIO
import time
import psycopg2

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER1 = 23
GPIO_ECHO1 = 18

GPIO_TRIGGER2 = 25
GPIO_ECHO2 = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

def distance(GPIO_TRIGGER, GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()


    # time difference
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
            dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)
            free = 0;
            if dist1 > 100:
                free=free+1
            if dist2 > 100:
                free=free+1

            print("Wolne miejsca = %", free)

            connection = psycopg2.connect(user="piotr",
                                        password="windows7",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pgs")
            cursor=connection.cursor()
            query = """INSERT INTO data (number) VALUES (%s)"""
            cursor.execute(query, (free, ))
            connection.commit()

            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
