from random import choice

class Game:
	def user_play(self):
		self.user_action = input("Enter a choice (rock, paper, scissors): ")
		return self.user_action

	def computer_play(self):
		self.computer_action = choice(['rock', 'scissors', 'paper'])
		return self.computer_action
	
	def chose(self):
		return print(f"You chose {self.user_action}, computer chose {self.computer_action}.\n")

	def result(self):
		if self.user_action == self.computer_action:
			print("Its a tie!")
		elif self.user_action == 'rock':
			if self.computer_action == 'scissors':
				print('Rock smashes scissors. You win!')
			else:
				print('Paper covers rock. You lose!')
		elif self.user_action == 'paper':
			if self.computer_action == 'rock': 		
				print('Paper covers rock. You win!')
			else:
				print('Scissors cuts paper. You lose!')
		elif self.user_action == 'scissors':
			if self.computer_action == 'paper':
				print('Scissors cuts paper. You win!')
			else:
				print('Rock smashes scissors. You lose!')

p = Game()
p.user_play()
p.computer_play()
p.chose()
p.result()
