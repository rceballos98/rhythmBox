import copy
import math

def _get_pulse(list_):
	result = []
	for element in list_:
		if (isinstance(element, list)):
			result += _get_pulse(element)
		else:
			result.append(element)
	return result

def _generate_rhythm_from_template(rhythm_template):
	base_rhythms = [
	[0],
	[1],
	[1,0],
	[1,0,0],
	[1,0,0,0],
	[0,0,0,0]
	]
	rhythms = []
	for rhythm in rhythm_template:
		actual_rhythm = []
		current_rhythm = _get_pulse(rhythm)
		for pulse in current_rhythm:
			actual_rhythm += base_rhythms[pulse]
		rhythms.append(actual_rhythm)
	return rhythms


def rotate_rhythm(rhythm, rotations):
	front = rhythm[rotations:]
	back = rhythm[:rotations]
	rhythm = front + back
	return rhythm

def reflect_rhythm(rhythm):
	length = len(rhythm)
	for i in xrange(length):
		rhythm.append(rhythm.pop[length-i])
	return rhythm

def clapping_music_algorithm(base, repetitions, number_of_rhythms):
	rhythms = []
	rhythms.append(base)
	for i in xrange(number_of_rhythms - 1):
		current_rhythm = []
		for rotations in xrange(len(base)):
			rotated_rhythm = rotate_rhythm(base,rotations)
			for rep in xrange(repetitions*(i+1)):
				for beat in rotated_rhythm:
						current_rhythm.append(beat)
		rhythms.append(current_rhythm)
	return rhythms

def eudclidean_algorithm(onsets,pulses):
	interval_a = pulses/onsets
	num_int_a = pulses%onsets
	interval_b = interval_a - 1
	num_int_b = onsets - num_int_a

	if num_int_a < num_int_b:
		num_int_b,num_int_a = num_int_a,num_int_b
		interval_a, interval_b = interval_b, interval_a

	ratio  = int(num_int_a/num_int_b)
	rhythm = []
	interval_count = 0
	for n in xrange(onsets):
		rhythm.append(1)
		if interval_count >= ratio:
			interval_count = 0
			for i in xrange(interval_b):
				rhythm.append(0)
		else:
			interval_count += 1
			for i in xrange(interval_a):
				rhythm.append(0)
	return rhythm

def complement(rhythm):
	complement = []
	for pulse in rhythm:
		if pulse == 1:
			complement.append(0)
		else:
			complement.append(1)
	return complement

def alternating_algorithm(rhythm):
	right = [] 
	left = []
	alternate = 1
	for pulse in rhythm:
		if pulse == 1:
			if alternate == 1:
				right.append(0)
				left.append(1)
			else:
				right.append(1)
				left.append(0)
			alternate = alternate*(-1)
		else:
			right.append(0)
			left.append(0)
	left_copy = copy.deepcopy(left)
	for pulse in right:
		left.append(pulse)
	for pulse in left_copy:
		right.append(pulse)
	return [right,left]

def reflecting_interlocking(rhythm):
	onsets = 0
	silences = 0
	for pulse in rhythm:
		if pulse == 1:
			onsets +=1
		if pulse == 0:
			silences += 1
	if silences != onsets:
		raise ValueError('Rhythm given does not \
have the same number of silences as onsets')
	else:
		return complement(rhythm)

def generate_score(templates):
	score = _generate_rhythm_from_template(templates)
	return score
