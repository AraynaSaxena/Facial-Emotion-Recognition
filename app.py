from flask import Flask, render_template, Response, request, url_for, redirect, flash,redirect,session
# from werkzeug import secure_filename
from camera import Video
import json
import cv2
from deepface import DeepFace
import os
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')





@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)
