from pyfirmata import Arduino, util
import time

import sys

try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character. 
        Nothing is echoed to the console. This call will block if a keypress 
        is not already available, but will not wait for Enter to be pressed. 

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

board = Arduino('/dev/ttyACM0')


pins = [6,7,8,9]

key = 0
print('\nDrum!!! (press q to exit)\n')

while key != 'q':
	key = getch()
	if key == 'i':
		board.digital[8].write(1)
		time.sleep(0.01)
		board.digital[8].write(0)

	if key == 'j':
		board.digital[6].write(1)
		time.sleep(0.01)
		board.digital[6].write(0)

	if key == ' ':
		board.digital[7].write(1)
		time.sleep(0.01)
		board.digital[7].write(0)

	if key == 'a':
		board.digital[9].write(1)
		time.sleep(0.01)
		board.digital[9].write(0)

