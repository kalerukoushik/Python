
import jarvis
from google_images_download import google_images_download 

# Driver Code 
def main(query):
    response = google_images_download.googleimagesdownload() 
    jarvis.speak("How many images of "+query +"do you want me to download")
    noOfImgs = int(jarvis.takeCommand())

    arguments = {"keywords": query, "format": "jpg", "limit":noOfImgs, "print_urls":False, "size": "medium", "aspect_ratio": "panoramic"}
    try: 
        response.download(arguments) 
        
    except FileNotFoundError: 
        arguments = {"keywords": query, "format": "jpg", "limit":noOfImgs, "print_urls":False, "size": "medium"} 
                        
        try:
            response.download(arguments) 
        except: 
            pass

    jarvis.speak("I have downloaded the images of "+query+ "and stored it in the download folder, take a look of it")
