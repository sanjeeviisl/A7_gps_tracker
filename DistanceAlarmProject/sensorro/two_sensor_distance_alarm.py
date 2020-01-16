#!/usr/bin/env python
from pyA20.gpio import gpio
from pyA20.gpio import port
from pydub import AudioSegment
from pydub.playback import play
import io
import time
import pyaudio
import wave
import sys


def playWaveAudio (name = "abc.wav",count =1):
    print ("playWaveAudio: ", name)
    print ("Times ", count)
    # real function defined
    CHUNK = 1024

    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute

    while True:

        
        wf = wave.open(name, 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
        

        played = datetime.now()
        playedHour = played.hour
        playedMin = played.minute

        playedTime = playedMin - currentMin
        if(playedTime > count) break
    
    
    return;


def playMp3Audio (name = "abc.mp3",count =1):
    print ("playMp3Audio: ", name)
    print ("Times ", count)
    # real function defined

    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute

    while True:

        data = open(name, 'rb').read()

        song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
        play(song)

        played = datetime.now()
        playedHour = played.hour
        playedMin = played.minute

        playedTime = playedMin - currentMin
        if(playedTime > count) break
    
    return;


print "Distance Measurement In Progress"

gpio.init()

TRIG1 = port.PA21
ECHO1 = port.PC3

TRIG2 = port.PA19
ECHO2 = port.PC2

gpio.setcfg(TRIG1, gpio.OUTPUT)
gpio.setcfg(ECHO1, gpio.INPUT)

gpio.setcfg(TRIG2, gpio.OUTPUT)
gpio.setcfg(ECHO2, gpio.INPUT)

gpio.output(TRIG1, 0)
gpio.output(TRIG2, 0)

print "Waiting for Sensor1 To Settle"

gpio.output(TRIG1, 0)
time.sleep(1)
gpio.output(TRIG1, 1)
time.sleep(0.00001)
gpio.output(TRIG1, 0)

while gpio.input(ECHO1) == 0:
    pulse_start = time.time()

while gpio.input(ECHO1) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance1 = pulse_duration * 17150

distance1 = round(distance, 2)

print("Distance1: " + str(distance) + "cm")


print "Waiting for Sensor2 To Settle"
gpio.output(TRIG2, 0)
time.sleep(1)
gpio.output(TRIG2, 1)
time.sleep(0.00001)
gpio.output(TRIG2, 0)

while gpio.input(ECHO2) == 0:
    pulse_start = time.time()

while gpio.input(ECHO2) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance2 = pulse_duration * 17150

distance2 = round(distance, 2)

print("Distance2: " + str(distance) + "cm")
