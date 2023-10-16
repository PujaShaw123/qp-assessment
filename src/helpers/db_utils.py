"""Script to provide database specific functions"""


def to_array(rows):
    """Function to convert tuples to list of dictionary."""
    return [r._asdict() for r in rows]
