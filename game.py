class Game:
    def __init__(self, initial_state=None):
        if not initial_state:
            self.state = self.__get_default_state()
        elif type(initial_state) is list and len(initial_state) == 16:
            self.state = initial_state
        else:
            raise ValueError("Game state has to be a list with 16 values.")
        self.desired_state = self.__get_default_state()

    @staticmethod
    def __get_default_state():
        default_state = list()
        for i in range(1, 16):
            default_state.append(i)
        default_state.append(None)
        return default_state

    @property
    def empty_field(self):
        return self.state.index(None)

    def __getitem__(self, item):
        return self.state[item]

    def __setitem__(self, key, value):
        self.state[key] = value

    def __str__(self):
        state_list = list(self.state)
        return (
            f"{state_list[:4]}\n"
            f"{state_list[4:8]}\n"
            f"{state_list[8:12]}\n"
            f"{state_list[12:]}"
        )

    def __repr__(self):
        return f"Game({self.state})"

    def __bool__(self):
        return self.state == self.desired_state

    def check_if_won(self):
        return bool(self)

    def move(self, item):
        item_position = self.state.index(item)
        if item_position % 4 == self.empty_field % 4 \
                or (self.empty_field % 4 == 0 and item_position == self.empty_field + 1) \
                or (self.empty_field % 4 == 3 and item_position == self.empty_field - 1):
            old_empty = self.empty_field
            self[item_position] = None
            self[old_empty] = item
        else:
            raise IllegalMoveError


class IllegalMoveError(Exception):
    def __init__(self):
        super(Exception, "Selected field's not adjacent to the empty field.")
