import rhythmGenerator as gen

#solenoid colors
#1-yellow-cookie
#2-blue-plastic
#3-green-box
#4-orange-glass

# Good rhythms
clave_son =  [1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0]
bossa_nova = [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]
gahu =       [1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0]
shiko = 	 [1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0]
son = 	 	 [1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0]
soukous = 	 [1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0]
rumba = 	 [1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0]
fume_fume =  [1,0,1,0,1,0,0,1,0,1,0,0]
bass_hound = [1,0,1,0,0,1,0,0]
amr_diab =   [1,0,0,1,0,0,1,0]
jules1 = 	 [1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1]
jules2 =     [1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0]
clapping_music_base = [1,1,1,0,1,1,0,1,0,1,1,0]
spaced =       [1,0,0,1,0,1,0,0]
aka_pygmies1 = [1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0]
aka_pygmies2 = [1,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0]
kanda_bongo = [1,0,0,1,0,0,1,0]
bolero = [1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1]


#templates

amen_break = [
#snare drum 1
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
#bass drum
[1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
#high hat
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
#snare drum 2
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0]
]

paradiddle = [
[1,0,1,1,0,1,0,1],
[0,1,0,0,1,0,1,1]
]

double_paradiddle = [
[1,0,1,0,1,1,0,1,0,1,0,0],
[0,1,0,1,0,0,1,0,1,0,1,1]
]

triple_paradiddle = [
[1,0,1,0,1,0,1,1,0,1,0,1,0,0],
[0,1,0,1,0,1,0,0,1,0,1,0,1,1]
]

gnawa = [
[1,0,1,0,0,1,0,0],
[0,1,0,0,1,0,1,0]
]

template1 = [
[4,4,4,4,3,3,3,2,2,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,3,3,3,3,3,3,3,3,3,3,3],
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,3,3,3,3,3,3,3,3,3,3,3],
[5,5,5,1,1,1,5,5,5,1,1,1,5,5,5,1,1,1,5,5,5,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1]
]

template2 = [
[2],
[3],
[1,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0],
[5,5,5,1,1,1,1]
]

template_paradiddle = [
paradiddle[0],
paradiddle[1],
[0],
[0]
]

template_amen_break = [
[5,5,5,5,5,5,5,5,5,5,amen_break[1],amen_break[1],amen_break[1],5,5],
[amen_break[0]],
[5,5,5,5,5,5,5,5,amen_break[3],amen_break[3],amen_break[3],5,5,5,5],
[5,5,5,5,5,5,amen_break[2],amen_break[2],amen_break[2],5,5,5,5,5,5]
]

alternating_clave_son = gen.alternating_algorithm([1,0,1,1,1,0,1,0])
complement_clave_son = gen.complement(clave_son)

clave_son_template = [
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,complement_clave_son,complement_clave_son,complement_clave_son,complement_clave_son,alternating_clave_son[0],alternating_clave_son[0],alternating_clave_son[0],alternating_clave_son[0]],
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son,clave_son],
[clave_son],
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,alternating_clave_son[0],alternating_clave_son[0],alternating_clave_son[0],alternating_clave_son[0]]
]

amr_diab_clapping_music = gen.clapping_music_algorithm(amr_diab,4,4)

aka_pygmies_template = [
aka_pygmies2,
[0],
aka_pygmies1,
aka_pygmies1
]

empty = [[0],[0],[0],[0]]

alternating_clave_son_double = []
alternating_clave_son = gen.alternating_algorithm([1,0,1,1,1,0,1,0])
for rhythm in alternating_clave_son:
	for pulse in rhythm:
		alternating_clave_son_double.append(pulse)
alternating_clave_son = alternating_clave_son_double

base1 = [1,0,1,1,0,1,0,0]
base2 = gen.alternating_algorithm(base1)
template4 = gen.clapping_music_algorithm(base1,4,4)
template3 = gen.clapping_music_algorithm(clave_son,2,4)
template5 = gen.clapping_music_algorithm(bossa_nova,4,4)