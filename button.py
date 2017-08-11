import subprocess
import socket
from gpiozero import Button, LED
from signal import pause

#############################################################################################
# Sends 'message' to port 55355 for RetroArch's network commands

def retroarch_command():
    print "reset...\n"
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.sendto("RESET", ("127.0.0.1", 55355))


#############################################################################################
# Safely shuts-down the Raspberry Pi

def shutdown():
    print "shutdown...\n"
    subprocess.call("sudo shutdown -h now", shell=True)


#############################################################################################


led = LED(14)
resetbtn = Button(2)
offbtn = Button(15)

while True:
	led.on()
	offbtn.when_pressed = shutdown
	resetbtn.when_pressed = retroarch_command

	pause()
	