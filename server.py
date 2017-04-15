#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:11:25 2017

@author: einarbui
"""

#import os
import time
from flask import Flask, request, send_file
from deepdream import *


app = Flask(__name__)

#Not really using this    
@app.route('/uploadPIL', methods=['POST'])
def uploadPIL():
    print(request.form['image'])
    return 'thanks for PIL'
    
@app.route('/uploadJPG', methods=['POST'])
def uploadJPG():
    incoming = request.files['file']
    incoming.save('temp.jpg')

    img = PIL.Image.open('temp.jpg')
    parameters = request.form.to_dict()
    imgout = transform(img, **parameters)
    imgout.save('output.jpg')
    # time.sleep(0.5)
    return send_file(open('output.jpg', 'rb'), mimetype='image/jpg')

@app.route('/uploadtest', methods=['POST'])
def uploadtest():
    print(request.files)
    print(request.form.to_dict())
    return 'thanks'
    
app.run(host= '0.0.0.0')  

    
#For later

#def serve_pil_image(pil_img):
#    img_io = StringIO()
#    pil_img.save(img_io, 'JPEG', quality=70)
#    img_io.seek(0)
#    return send_file(img_io, mimetype='image/jpeg')
#    
#@app.route('/some/route/')
#def serve_img():
#    img = Image.new('RGB', ...)
#    return serve_pil_image(img)