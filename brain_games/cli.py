import prompt

def run():
	name = prompt.string('May I have your name? ')
	return ('Hello, ' + name + '!')
