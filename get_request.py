# bringing in the module we need to reach out to a webpage
import requests

# grabbing the webpage we desire. In my case, I have been really into the game called TemTem
webpage_response = requests.get('https://crema.gg/games/temtem/')

# showing what the status code is. Tested and shows a '200'
print(webpage_response.status_code)
