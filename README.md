![banner](assets/banner.png)
![version](https://img.shields.io/badge/Version-1.0.0-blue) ![pure python](https://img.shields.io/badge/Pure%20Python-True-yellow)

# Text Engine

## Description
Text engine is an engine for creating text adventure games. It has utilities to help greatly improve efficiency and time. Its a pure python package, built for scalability and usability. It is designed for you to build apon the engine, creating whatever type of text adventure you want!

---

## Features
| Name | Description |
|------|-------------|
| Entity | A Basic living thing|
| Person | An extension of Entity, has a built in inventory system and dialog system |
| Item | A Basic item, you can stack them up till a customizable limit |
| Iteraction | Interact between two people, remove or give items between people |

---

## Example Usage
Example 1: Using the Item and Stack Classes
```py
from items import Item, Stack

# Create an iron sword item with a custom description
iron_sword = Item("Iron Sword", "A sturdy weapon made of iron.", stack_size=1)

# Create a stack of apples
apple = Item("Apple")
apple_stack = Stack(apple, stack_size=10)
apple_stack.push(5)

# Print the current stack size of the apple stack
print(f"Current stack size of apples: {len(apple_stack)}")
```

Example 2: Interacting with Characters and Inventory
```py
from interaction import Interaction
from character import Person
from items import Item

# Create a character named "Player" with a custom inventory size and description
player = Person("Player", "A skilled adventurer.", (255, 255, 255), health=100, armor=50, inventory_size=20)

# Create a health potion item
health_potion = Item("Health Potion", "Restores health when consumed.")
health_potion_stack = Stack(health_potion, stack_size=5)

# Give the player a health potion
Interaction.give_item(player, health_potion)

# Try to give the player another health potion (inventory is full)
try:
    Interaction.give_item(player, health_potion)
except FullInventory as e:
    print(e)

# Take a health potion from the player's inventory
Interaction.take_item(player, health_potion)

# Try to take more health potions than available (error)
try:
    Interaction.take_item(player, health_potion, amount=3)
except ItemNotInInventory as e:
    print(e)
```

Example 3: Using Text Output for Character Interaction
```py
from character import Person
from text import Text

# Create a character named "NPC" with a custom text color
npc = Person("NPC", "A friendly villager.", (0, 128, 0), health=80, armor=20)

# Create a text instance with custom color
text_handler = Text((255, 165, 0))

# Make the NPC say a message using colored text output
text_handler.say(npc.get_name(), "Hello, traveler! Welcome to our village.")

# Create a player character and make them say a message
player = Person("Player", "An adventurous soul.", (0, 0, 255), health=120, armor=60)
text_handler.say(player.get_name(), "Greetings! Thank you for your warm welcome.")
```

---

## Contributing
We welcome contributions to improve Text Engine. If you'd like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your contributions. 
2. Make your changes or additions in your branch. 
3. Clearly describe your changes in your commits and pull request. 
4. Ensure your code follows the existing style and conventions of the project.
5. Update any relevant documentation to reflect your changes. 
6. Open a pull request, providing a detailed description of your changes.


### Example of Changes
When contributing, please list your changes or additions in your pull request. Here's an example of how your pull request message could be structured:
```markdown
### Changes/Additions

- Added a new class `NewFeature` in `module.py`.
- Updated the `function_name` method to include additional parameters.
- Fixed a bug in `another_module.py` where values were not properly validated.
```

---

This project is licensed under the [__Apache V2 License__](LICENSE).
