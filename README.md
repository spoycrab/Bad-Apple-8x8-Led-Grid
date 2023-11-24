<p align="center">
  <img src="https://docs.arduino.cc/static/bc75e08267cb638bb4dcae684a7038e0/a6d36/8x8-LED-Matrix.png" width="450 align="center">
</p>
    
# Bad Apple on a 8x8 Led Grid
Project inspiration [Playlist](https://www.youtube.com/watch?v=cuMkI6cDKMs&list=PLajlU5EKJVdonUGTEc7B-0YqElDlz9Sf9).

This is an Arduino project to run the music video bad apple on a 8x8 Led Grid

First i've used ffmpeg to transform every frame of the video into a 8x8 png image, then ran a python code to transform every image into a Hex array, after that i've pasted that array into the arduino (IMAGES[ ] array) and compiled it.

You can adapt the code to run on a larger Display.
