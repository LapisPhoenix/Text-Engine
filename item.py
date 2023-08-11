"""
For License please look at LICENSE
"""


from error import NotAnItem, AddedTooManyItems


class Stack:
    def __init__(self, stack_size: int = 64) -> None:
        """
        A Stack for an item, this should never be used for non items.
        :param stack_size: int
        """
        if not isinstance(stack_size, int):
            raise ValueError(f"Stack Size must be type int, not type {type(stack_size).__name__}.")
        
        self.stack_size = stack_size
        self.item_stack = []

    def push(self, item: "Item", amount) -> bool:
        """
        Add an item to the item stack
        :param item:
        :param amount:
        :return: True
        :raises: error.AddedTooManyItems
        """
        
        if not isinstance(item, Item):
            raise NotAnItem(f"{item} is not of the type Item. (Hint: {item} is type {type(item).__name__}).")
        
        if amount + len(self.item_stack) > self.stack_size:
            raise AddedTooManyItems(f"Tried to add {amount} items ({item.get_name()}) but stack size is {self.stack_size}. (Hint: {len(self.item_stack)} items was already in the stack.)")
        
        self.item_stack.extend([item] * amount)
        return True
    
    def get_stack_size(self) -> int:
        return self.stack_size
    
    def get_item_stack(self) -> list:
        return self.item_stack
    
    def __stack_size__(self) -> int:
        return self.get_stack_size()


class Item:
    def __init__(self, name: str, description: str = "", stack_size: int = 64) -> None:
        """
        Represents any customizable item.
        :param name:
        :param description:
        :param stack_size:
        """
        self.name = name
        self.description = description
        self.stack = Stack(stack_size)

    def get_name(self) -> str:
        """
        Gets the item's name
        :return: Item name
        """
        return self.name

    def get_description(self) -> str:
        """
        Gets the item's description, if there is one.
        :return: None | Item Description
        """
        return self.description
