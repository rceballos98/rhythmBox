from pyfirmata import Arduino, util
import time

currentTime = 0
previousTime = 0
set_solenoids = False
pointers = [0,0,0,0]
#default
pins = [6,7,8,9]
number_of_solenoids = len(pins)
board = Arduino('/dev/ttyACM0')

def set_board(port):
	board = Arduino(port) #ACM0 .usbserial-A6008rIF

def set_pins(pin1,pin2,pin3,pin4):
	pins[0] = pin1
	pins[1] = pin2
	pins[2] = pin3
	pins[3] = pin4

def _set_pointers(solenoids, previousTime, pulse_length):

	currentTime = time.time()
	
	for i in xrange(number_of_solenoids):
		if (currentTime - previousTime > pulse_length):
			if solenoids[i]["pointer"]+2 > len(solenoids[i]["rhythm"]):
				solenoids[i]["pointer"] = 0
				#print i+1
			else:
				solenoids[i]["pointer"] += 1;
		#print solenoids[i]["pointer"]
	previousTime = currentTime

	return solenoids

def load_solenoids(rhythms):
	solenoids = []
	for i in xrange(number_of_solenoids):
		solenoids.append({"rhythm":rhythms[i],"pointer":pointers[i],"pin":pins[i]})
	set_solenoids = True
	return solenoids

def play_solenoids(rhythms, pulse_length):
		solenoids = load_solenoids(rhythms)

		while True:	
			previousTime = currentTime

			#turns off solenoids for consecutive beats
			for pin in pins:
				board.digital[pin].write(0)
			
			#length of solenoid pause
			time.sleep(pulse_length/3)

			for i in xrange(number_of_solenoids):
				#writes either a 0 or a 1 to corresponding solenoid pin by reading the rhythm inside each 
				#solenoid dictionary at the pointer specified
				board.digital[solenoids[i]["pin"]].write(solenoids[i]["rhythm"][solenoids[i]["pointer"]])
				#print solenoids[i]["pointer"] (for debugging)

			#lenght of solenoid signal
			time.sleep(2*pulse_length/3)

			#set pointers
			solenoids = _set_pointers(solenoids,previousTime,pulse_length)



