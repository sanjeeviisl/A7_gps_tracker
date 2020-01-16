import arctusapi

from arctusapi import getAPIKey 
from arctusapi import sendNotification 
#from arctusapi import uploadFile 

api_key = getAPIKey ('arctus')
sendNotification(api_key, "+918171943905","project2", "location2", 4, 5, 6, 7, 4, "test.jpg")
#image_file_name = "test.jpg"
#uploadFile(image_file_name)


