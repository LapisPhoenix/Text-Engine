from error import AddedTooManyItems


class Stack:
    def __init__(self, stack_for: "Item", stack_size: int = 64) -> None:
        """
        Represents a stack of items with a maximum size.
        :param stack_for: The type of item this stack holds.
        :param stack_size: The maximum size of the stack.
        """
        if not isinstance(stack_size, int):
            raise ValueError(f"Stack Size must be type int, not type {type(stack_size).__name__}.")
        if not isinstance(stack_for, Item):
            raise ValueError(f"Stack for must be type Item, not type {type(stack_for).__name__}.")

        self.stack_size = stack_size
        self.stack_for = stack_for
        self.item_stack = []

    def push(self, amount: int) -> None:
        """
        Add items to the stack.
        :param amount: The amount of items to add.
        :raises AddedTooManyItems: If adding items exceeds the stack size.
        """
        if amount + len(self.item_stack) > self.stack_size:
            raise AddedTooManyItems(f"Tried to add {amount} items ({self.stack_for.get_name()}), "
                                    f"but stack size is {self.stack_size}.")

        self.item_stack.extend([self.stack_for] * amount)

    def pop(self, amount: int) -> None:
        """
        Remove items from the stack.
        :param amount: The amount of items to remove.
        """
        if len(self.item_stack) >= amount:
            self.item_stack = self.item_stack[:-amount]

    def __len__(self) -> int:
        return len(self.item_stack)

    def get_stack_size(self) -> int:
        """
        Get the stack size limit.
        :return: The stack size limit.
        """
        return self.stack_size

    def get_item_stack(self) -> list:
        """
        Get the current stack of items.
        :return: The current stack of items.
        """
        return self.item_stack

    def __stack_size__(self) -> int:
        """
        Get the current stack size limit.
        :return: The current stack size limit.
        """
        return self.get_stack_size()


class Item:
    def __init__(self, name: str, description: str = "", stack_size: int = 64) -> None:
        """
        Represents any customizable item.
        :param name: The name of the item.
        :param description: The description of the item (optional).
        :param stack_size: The maximum stack size of the item (default is 64).
        """
        self.name = name
        self.description = description
        self.stack = Stack(self, stack_size)
        self.add_to_stack()

    def add_to_stack(self):
        """
        Add the item to its stack.
        """
        self.stack.item_stack.append(self)

    def remove_from_stack(self):
        """
        Remove the item from its stack.
        """
        self.stack.item_stack.remove(self)

    def get_name(self) -> str:
        """
        Get the item's name.
        :return: The item's name.
        """
        return self.name

    def get_description(self) -> str:
        """
        Get the item's description, if there is one.
        :return: The item's description.
        """
        return self.description

    def set_description(self, description: str):
        """
        Set the description of the item.
        :param description: The new description for the item.
        """
        self.description = description

    def set_name(self, name: str):
        """
        Set the item's name.
        :param name: The new name for the item.
        """
        self.name = name