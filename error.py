class AddedTooManyItems(Exception):
    """
    Custom exception raised when attempting to add too many items to a container.
    """
    pass


class NotAnItem(Exception):
    """
    Custom exception raised when an operation is performed on a non-item object.
    """
    pass
