import i2c_lcd as lcd
import time
import psycopg2

def select_last():
    connection = psycopg2.connect(user="piotr",
            password="windows7",
            host="127.0.0.1",
            port="5432",
            database="pgs")

    cursor = connection.cursor()
    query = "SELECT number, date FROM data ORDER BY date DESC LIMIT 1"
    cursor.execute(query)
    anwser = cursor.fetchone()
    return anwser

def main():
    while True:
        number = select_last()
        lcd.clear()
        lcd.lcd_string("Wolne miejsca:", lcd.LCD_LINE_1)
        lcd.lcd_string(str(number[0]), lcd.LCD_LINE_2)
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.lcd_byte(0x01, lcd.LCD_CMD)
