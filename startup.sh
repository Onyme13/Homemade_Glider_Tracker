#!/bin/bash

sleep 2

cd Homemade_Glider_Tracker

sleep 1

sudo python ./server.py &

sleep 2

sudo python ./GUI_tkinter.py


