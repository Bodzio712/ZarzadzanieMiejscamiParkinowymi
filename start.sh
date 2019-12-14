#!/bin/bash

echo "Uruchamianie pomiaru..."
sudo python3 Pomiar/pomiar.py &
echo "Uruchamianie lcd..."
sudo python3 LCD/lcd.py &

sleep 10
echo 'Zabijanie procesów'
sudo pkill -2 -f Pomiar/pomiar.py
sudo pkill -2 -f LCD/lcd.py

sleep 2
echo 'Zabijanie Pythona'
sudo pkill -2 -f python3
