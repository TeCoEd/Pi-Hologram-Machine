#Based on a program code from @bigles
from gpiozero import Button
from subprocess import check_call
from signal import pause
from random import choice
from time import sleep
import glob
import subprocess
import keyboard #(pip3 install keyboard)

sleep(5)
shutdown_btn = Button(17, hold_time=2)

def play_video():
    keyboard.press_and_release('q') #stop the video player so that the next one can be displayed
    sleep(1)
    videos = []
    for file in glob.glob("/home/pi/Hologram/*.mp4"):
        videos.append(file)
    print(videos)
    chosen = choice(videos)
    print(chosen)
    subprocess.Popen(['omxplayer',(chosen)])
        
def pause_video():
    keyboard.press_and_release('space')
    
def shutdown():
    check_call(['sudo', 'poweroff'])
    
randomiser = Button(2) #select video
pause_button = Button(3) #pause
video_shutdown = Button(4) #shutdown

try:
    print("Press THE BUTTON")
    randomiser.when_pressed = play_video
    pause_button.when_pressed = pause_video
    shutdown_btn.when_held = shutdown
    pause()
except KeyboardInterrupt:
    print("\nEXIT")
