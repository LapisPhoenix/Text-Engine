from text import Text


class Entity:
	def __init__(self, species: str, health: int, armor: int, description: str):
		"""
		Represents a game entity with health, armor, and other attributes.
		:param species: The species or type of the entity.
		:param health: The health points of the entity.
		:param armor: The armor points of the entity.
		:param description: A description of the entity.
		"""
		if not isinstance(health, int):
			raise ValueError(f"Entity Health must be type int, not type {type(health).__name__}")
		if not isinstance(armor, int):
			raise ValueError(f"Entity Armor must be type int, not type {type(armor).__name__}")
		if not isinstance(description, str):
			raise ValueError(f"Value must be type str, not {type(description).__name__}.")
		self.species = species
		self.health = health
		self.armor = armor
		self.description = description
		self.is_dead = False
	
	def get_description(self) -> str:
		"""
		Get the description of the entity.
		:return: The description of the entity.
		"""
		return self.description
	
	def get_health(self) -> int:
		"""
		Get the health points of the entity.
		:return: The health points of the entity.
		"""
		return self.health
	
	def get_species(self) -> str:
		"""
		Get the species or type of the entity.
		:return: The species or type of the entity.
		"""
		return self.species
	
	def get_is_dead(self) -> int:
		"""
		Get whether the entity is dead.
		:return: True if the entity is dead, False otherwise.
		"""
		return self.is_dead
	
	def get_armor(self) -> int:
		"""
		Get the armor points of the entity.
		:return: The armor points of the entity.
		"""
		return self.armor
	
	def set_is_dead(self, value: bool):
		"""
		Set whether the entity is dead.
		:param value: True if the entity is dead, False otherwise.
		:return: None
		"""
		if not isinstance(value, bool):
			raise ValueError(f"Value must be either True or False, not {value}.")
		self.is_dead = value
	
	def set_description(self, description: str):
		"""
		Set the description of the entity.
		:param description: The new description for the entity.
		:return: None
		"""
		if not isinstance(description, str):
			raise ValueError(f"Value must be type str, not {type(description).__name__}.")
		self.description = description
	
	def set_health(self, health: int):
		"""
		Set the health points of the entity.
		:param health: The new health points for the entity.
		:return: None
		"""
		if not isinstance(health, int):
			raise ValueError(f"Value must be type int, not {type(health).__name__}.")
		self.health = health
	
	def set_species(self, species: str):
		"""
		Set the species or type of the entity.
		:param species: The new species or type for the entity.
		:return: None
		"""
		self.species = species
	
	def set_armor(self, value: int):
		"""
		Set the armor points of the entity.
		:param value: The new armor points for the entity.
		:return: None
		"""
		if not isinstance(value, int):
			raise ValueError(f"Value must be type int, not {type(value).__name__}")
		self.armor = value


class Person(Entity):
	def __init__(self, name: str, description: str, text_color: tuple[int, int, int], health: int, armor: int, inventory_size: int = 16):
		"""
		Represents a human-like game character with additional text features.
		:param name: The name of the person.
		:param health: The health points of the person.
		:param armor: The armor points of the person.
		:param description: A description of the person.
		:param text_color: The RGB color tuple for text output.
		"""
		super().__init__("Human", health, armor, description)
		self.name = name
		self.text_handler = Text(text_color)
		self.inventory_size = inventory_size
		self.inventory_stack = []   # List of all the items currently in the inventory
	
	def say(self, message: str):
		"""
		Make the person say a message using text output.
		:param message: The message the person wants to say.
		:return: None
		"""
		self.text_handler.say(self.name, message)
	
	def get_name(self) -> str:
		"""
		Get the name of the person.
		:return: The name of the person.
		"""
		return self.name
	
	def set_name(self, name: str):
		"""
		Set the name of the person.
		:param name: The new name for the person.
		:return: None
		"""
		if not isinstance(name, str):
			raise ValueError(f"Person name must be type str, not type {type(name).__name__}")
		self.name = name