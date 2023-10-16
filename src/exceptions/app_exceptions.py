""" Exceptions """
class ValidationError(Exception):
    """Validation Error"""
    def __init__(self, message):
        super().__init__()
        self.message = message