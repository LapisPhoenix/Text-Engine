import time
import random
import sys


class Text:
	def __init__(self, text_color: tuple[int, int, int]):
		"""
		A utility class for displaying text with custom colors.
		:param text_color: RGB color tuple (0-255) for the text.
		"""
		r, g, b = text_color
		if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
			raise ValueError("Color components should be integers.")
		
		if not 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
			raise ValueError("Color components should be in the range 0-255.")
		
		self.text_color = text_color
		self.r, self.g, self.b = self.text_color
	
	def print_colored_text(self, text, end: str = '\n'):
		"""
		Print a single-colored message.
		:param text: The text to be printed to the screen
		:param end: What is to print at the end of the text, defaults to a newline character.
		:return:
		"""
		print(f'\033[38;2;{self.r};{self.g};{self.b}m{text}\033[0m', end=end)
	
	def _human_say(self, text):
		"""
		Simulate human-like typing and printing of text.
		:param text: The text to be printed.
		"""
		for char in text:
			time.sleep(random.choice([
				0.3, 0.11, 0.08, 0.07, 0.07,
				0.07, 0.06, 0.06, 0.05, 0.01
			]))
			sys.stdout.write(char)
			sys.stdout.flush()
		print()
	
	def say(self, person, text):
		"""
		Display colored text as if spoken by a person.
		:param person: The name or identifier of the person speaking.
		:param text: The text to be spoken.
		"""
		print(f"[\033[38;2;{self.r};{self.g};{self.b}m{person}\033[0m]: ", end='')
		self._human_say(text)
