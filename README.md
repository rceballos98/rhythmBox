rhythmBox
=========

Python script to control arduino running firmata. It allows users to play any rhythm on the arduino which is connected to four solenoids.

=========

Run firmata on Arudino
Install pyfirmata library for python 2.7

Use rhythmUserInterface to pull from the other three modules that provide
common rhythm templates and common algorythm's used to generate rhythms. 

========

Example Video of a 4 person syncopated clave rhythm (+.+.+..+.+..):
https://goo.gl/photos/6Z5ck3KXUv2vJ4QX6

In the video all solenoids start with the same rhythm.
Then each solenoid will skip a beat (momentarily shorten the rhythm by one beat) with the frequencies listed below:
Solenoid A: every 4 
Solenoid B: every 8
Solenoid C: every 16
Solenoid D: Never skips a beat

As the video shows, this very simple algorithm can generate some really intrecate sounding rhythms!
