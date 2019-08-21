#!/usr/bin/env python
from pyA20.gpio import gpio
from pyA20.gpio import port
from datetime import datetime, date
import io
import time
import wave
import sys
import gps
import requests 

### to be included
####!/bin/bash 
####sudo gpsd /dev/ttyS2 -F /var/run/gpsd.sock

  
# defining the api-endpoint  
START_API_ENDPOINT = "http://iisl.co.in/system/VehicleTracker/gps_control_panel/gps_mapview/adddevicelocation.php"
  
# your API key here 
DEVICE_KEY = "9873441502"
  
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
data = {'device_id': DEVICE_KEY }

try:
    # sending post request and saving response as response object
    r = requests.post(url =START_API_ENDPOINT, data = data)
    # extracting response text
    response  = r.text
    print("Response from server :%s"%response)

except Exception as e:
    print("Error %s" % str(e))

while True:
    time.sleep(5) 
    try:
        report = session.next()
        # Wait for a 'TPV' report and display current time
        if report['class'] == 'TPV':
            if hasattr(report, 'time') and hasattr(report, 'lat') and hasattr(report, 'lon'):
                print report.time
                print "Latitude: "+str(report.lat)+", Longitude: "+str(report.lon)
                # GET GPS DATA
                gpsData['device_id'] = DEVICE_KEY
                gpsData['latitude'] = report.latitude
                gpsData['longitude'] = report.longitude
                gpsData['utcdate_stamp'] = gpsd.utc
                gpsData['utctime_stamp'] = report.time
                gpsData['alt'] = report.altitude
                gpsData['eps'] = report.eps
                gpsData['epx'] = report.epx
                gpsData['epv'] = report.epv
                gpsData['ept'] = report.ept
                gpsData['speed'] = report.speed
                gpsData['climb'] = report.climb
                gpsData['track'] = report.track
                gpsData['mode'] = report.mode
                gpsData['sats'] = report.sats
                gpsData['direction'] =  ""
                gpsData['gps_data'] =  ""
                gpsData['device_status'] =  ""
                gpsData['engine_status'] = ""
                gpsData['vehicle_status'] = ""
            
                trigger = float(gpsData['latitude'])
                
                if math.isnan(trigger):
                   data = {'device_id': gpsData['device_id'],'longitude': gpsData['longitude'],'latitude': gpsData['latitude'],\
                   'utcdate_stamp': gpsData['utcdate_stamp'],'utctime_stamp': gpsData['utctime_stamp'],'speed': gpsData['speed'],\
                   'direction': gpsData['direction'],'gps_data': gpsData['gps_data'],'device_status': gpsData['device_status'],\
                   'engine_status': gpsData['engine_status'],'vehicle_status': gpsData['vehicle_status']}
                else :
                   data = {'device_id': gpsData['id'],'longitude': gpsData['longitude'],'latitude': gpsData['latitude'],\
                   'utcdate_stamp': gpsData['utcdate_stamp'],'utctime_stamp': gpsData['utctime_stamp'],'speed': gpsData['speed'],\
                   'direction': gpsData['direction'],'gps_data': gpsData['gps_data'],'device_status': gpsData['device_status'],\
                   'engine_status': gpsData['engine_status'],'vehicle_status': gpsData['vehicle_status']}
                    
                try:	
                  
                   # sending post request and saving response as response object 
                   r = requests.post(url = API_ENDPOINT, data = data) 
                    # extracting response text  
                   pastebin_url = r.text 
                   print("The pastebin URL is:%s"%pastebin_url) 

                except Exception as e:
                   print("Error %s" % str(e))

    except Exception as e:
      print("Error %s" % str(e))

