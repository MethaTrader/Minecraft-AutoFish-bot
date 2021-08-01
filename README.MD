[![Python 2.7|3.6](https://img.shields.io/badge/Python-2.7%7C3.6-blue.svg)](https://www.python.org/) [![Open CV 4.5.3](https://img.shields.io/badge/OpenCV-4.5.3-brightgreen)](https://pypi.org/project/opencv-python/)

![Screenshot](https://i.piccy.info/i9/c466461aee534d39743c4f83d5699cb5/1627851597/93807/1437490/18198image.jpg)


## Hello everyone, this is my second attempt at making a bot for games. This time, automatic fishing in the minecraft game. Go!
#

*The bot is simple and unstable, it can sometimes work incorrectly.*

### How does the bot work?
First, we are looking for a float, more precisely red in the range from <span style="color:rgb(90, 19, 29)">rgb(90, 19, 29)</span> to <span style="color:rgb(230, 50, 50)">rgb(230, 50, 50)</span>. 
If the float is found, then everything is fine, we do nothing.
If the float disappears from the screen *(under water)*, the bot will press the right mouse button after 1 second until the float appears again.

### **Problems that may arise:**
1) If a red color gets into the frame, the bot will react to it.
2) If they start to beat us in the game or we turn away from the float
3) If the brightness in the game is too low


Thank you all, have fun playing!