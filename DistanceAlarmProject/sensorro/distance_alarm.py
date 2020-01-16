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

    
    return;


def playMp3Audio (name = "abc.mp3",count =1):
    print ("playMp3Audio: ", name)
    print ("Times ", count)
    # real function defined
    data = open(name, 'rb').read()

    song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
    play(song)

    return;


TRIG = port.PA21
ECHO = port.PC3

gpio.init()

print "Distance Measurement In Progress"

gpio.setcfg(TRIG, gpio.OUTPUT)
gpio.setcfg(ECHO, gpio.INPUT)

gpio.output(TRIG, 0)

print "Waiting For Sensor To Settle"

time.sleep(2)
gpio.output(TRIG, 1)
time.sleep(0.00001)
gpio.output(TRIG, 0)

while gpio.input(ECHO) == 0:
    pulse_start = time.time()

while gpio.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance: " + str(distance) + "cm")

if( distance < 1000 )
    playWaveAudio("abc.wav",2)    


if( distance > 1000 )
    playMp3Audio("abc.mp3",2)    
