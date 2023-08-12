from error import FullInventory, ItemNotInInventory
from item import Item
from character import Person


class Interaction:
    @staticmethod
    def give_item(person: Person, item: Item):
        """
        Give an item to a person's inventory, managing item stacks if necessary.
        :param person: The person receiving the item.
        :param item: The item to be given.
        :raises FullInventory: If the person's inventory is full.
        """
        if len(person.inventory_stack) + 1 > person.inventory_size:
            raise FullInventory("You tried to add an item to the inventory, but the inventory is full!")

        for itm in person.inventory_stack:
            if itm == item and len(itm.stack) < itm.stack.get_stack_size():
                # Item stack is not full
                itm.stack.push(1)
                break
        else:
            person.inventory_stack.append(item)

    @staticmethod
    def take_item(person: Person, item: Item, amount: int = 1):
        """
        Take an item from a person's inventory.
        :param person: The person from whose inventory the item is taken.
        :param item: The item to be taken.
        :param amount: The amount of the item to take (default is 1).
        :raises ItemNotInInventory: If the item is not in the person's inventory.
        """
        if item not in person.inventory_stack:
            raise ItemNotInInventory(f"{item.get_name()} is not in {person.get_name()}'s inventory.")

        for i, itm in enumerate(person.inventory_stack):
            if itm == item:
                if len(itm.stack.get_item_stack()) >= amount:
                    return itm.stack.pop(amount)
        else:
            raise ItemNotInInventory(f"{amount} {item.get_name()} not found in {person.get_name()}'s inventory.")
