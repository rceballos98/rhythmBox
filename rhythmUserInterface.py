import rhythmGenerator as gen
import arduinoRhythmPlayer as player
import templates as tmp
#solenoid colors
#1-yellow-cookie
#2-blue-plastic
#3-green-box
#4-orange-glass

#set speed
speed = 0.12

#Initiate arduino board
player.set_board('/dev/ttyACM0')

#CHOOSE RHYTHM FROM TEMPLATES
template = tmp.clave_son_template
template = tmp.template_amen_break
template = tmp.amr_diab_clapping_music

#TRASNFORM RHYTHM TO ARDUINO READABLE
score = gen.generate_score(template)
longest = 0
for rhythm in score:
	print rhythm
	length = len(rhythm)
	print length
	if length > longest:
		longest = length
print 'Duration: ' + str(longest*speed)

#PLAY THE RHYTHM
player.play_solenoids(score,speed)