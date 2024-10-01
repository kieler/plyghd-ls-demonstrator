from enum import Enum


class SynthesisOptionType(Enum):
    # Options of this type are just set or not set.
        CHECK = 0
        # Options of this type provide a set of possible disjoint values.
        CHOICE = 1
        # Options of this type provide a range of possible continuous values.
        RANGE = 2
        # Options of this type provide any String as its possible values.
        TEXT = 3
        # Pseudo option representing a separator.
        SEPARATOR = 4
        # Pseudo option representing a container for other options.
        CATEGORY = 5


class SynthesisOption:
    def __init__(self, id, theName, theType, theInitialValue):
        self.id = id
        self.name = theName
        self.type = theType
        self.initialValue = theInitialValue