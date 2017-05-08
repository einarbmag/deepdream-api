# deepdream-api
Flask app that transforms jpg images using Google's Deepdream. Available as a Docker image, [einarbmag/deepdream-api](https://hub.docker.com/r/einarbmag/deepdream-api/)

This is a Flask app that consists of an endpoint at 0.0.0.0:5000/uploadJPG which receives a jpeg along with a few parameters, 
transforms the image using Google's Deepdream, and returns it. This is a CPU-only version. Here is a code snippet showing how one 
would interact with the server using Python:

```
import requests

#Send and get JPEG back
"""
Parameters:
    maxwidth: positive integer (=512)
    iter_n:positive integer (=10)
    octave_n: positive integer (=4)
    octave_scale: float, usually between 1 and 2 I think (=1.4)
    end: string, layer that gets displayed (='inception_4c/output')
"""
fileJPG = open('einar.jpg', 'rb')
res = requests.post('http://0.0.0.0:5000/uploadJPG', 
                    files={'file':fileJPG}, 
                    data={'iter_n':10, 'octave_n':4}, 
                    timeout=100.0
                    )
                    
with open('final.jpg', 'wb') as f:
    for chunk in res.iter_content(1024):
        f.write(chunk)
```
