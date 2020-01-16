# importing the requests library 
import requests 

def uploadImage(image_file_name) :
    url = 'http://iisl.co.in/system/VigilanceApp/server_scripts/uploadImage.php'
    files = {'image': open(image_file_name, 'rb')}
    r = requests.post(url, files=files)
    # extracting response text
    response = r.text
    print("Response:%s"%response)

def getAPIKey (company ) :

    # api-endpoint 
    URL = "http://iisl.co.in/system/VigilanceApp/server_scripts/fcm/getAPIKey.php"

    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'company_name':company} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 

    # extracting data in json format 
    data = r.json() 


    # extracting latitude, longitude and formatted address 
    # of the first matching location 
    api_key = data[0]['api_key']
    company_  = data[0]['company_name']
    

    # printing the output 
    print("\n COMAPNY:   %s  "   %(company_))
    print(" API_KEY:   %s  \n"   %(api_key))
    return api_key


def sendNotification(API_KEY, manager_id, project, location, glove, goggle, vest, boot, helmet, image_path) :

    # defining the api-endpoint 
    API_ENDPOINT = "http://iisl.co.in/system/VigilanceApp/server_scripts/fcm/sendMessage_ai_safety.php"

    uploadImage(image_path)
 
    # data to be sent to api 
    data = {'api_dev_key':API_KEY, 
            'manager_id': manager_id, 
            'project': project, 
            'location': location, 
            'glove': glove, 
            'goggle': goggle, 
            'vest': vest, 
            'boot': boot, 
            'helmet': helmet, 
            'image_path': image_path} 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    response = r.text 
    print("Response:%s"%response) 

