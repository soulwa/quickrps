import random

ROCK = 0
SCISSORS = 1
PAPER = 2

USER_WIN = 0
CPU_WIN = 1
TIE = 2

rps_order = [0, 1, 2, 0]
rps_enum_to_str = ['rock', 'scissors', 'paper']

def quick_rps(user_in, cpu_in):
	if cpu_in == user_in:
		return TIE
	if cpu_in == rps_order[user_in + 1]:
		return USER_WIN
	return CPU_WIN
