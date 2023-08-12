class AddedTooManyItems(Exception):
    """
    Raised when attempting to add too many items to a container.
    """
    pass


class NotAnItem(Exception):
    """
    Raised when an operation is performed on a non-item object.
    """
    pass


class FullInventory(Exception):
    """
    Raised when attempting to add an item to a person's inventory, but the inventory is already full.
    """
    pass


class ItemNotInInventory(Exception):
    """
    Raised when trying to remove an item from a person's inventory, but the item doesn't exist in the inventory.
    """
    pass
