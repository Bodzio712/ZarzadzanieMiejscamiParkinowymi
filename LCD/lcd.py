import i2c_lcd as lcd
import time
import psycopg2

def select_last():
    connection = psycopg2.connect(user="piotr",
            password="windows7",

def main():
    while True:

        lcd.clear()
        lcd.lcd_string("Liczba wolnych miejsc:", lcd.LCD_LINE_1)
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.lcd_byte(0x01, lcd.LCD_CMD)
