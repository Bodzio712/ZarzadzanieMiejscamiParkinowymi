#!/bin/bash

echo "Uruchamianie pomiaru..."
sudo python3 Pomiar/pomiar.py &
echo "Uruchamianie lcd..."
sudo python3 LCD/lcd.py &
echo "Uruchamianie serwera..."
uwsgi --http 0.0.0.0:5000 --wsgi-file Serwer/wsgi.py &

while true
do
	sleep 1
done

function ctrc()
{
	echo 'Zabijanie pomiaru..'
	sudo pkill -2 -f Pomiar/pomiar.py
	echo 'Zabijanie lcd...'
	sudo pkill -2 -f LCD/lcd.py
	echo 'Zabijanie uwsgi...'
	sudo pkill -2 -f uwsgi
	
	echo 'Zabijanie Pythona...'
	sudo pkill -2 -f python3
	echo 'Zabijanie uwsgi(SIGKILL)...'
	sudo pkill -9 -f uwsgi
}

trap ctrc SIGINT
