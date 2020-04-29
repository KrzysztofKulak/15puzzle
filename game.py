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

    def __len__(self):
        return len(self.state)

    def check_if_won(self):
        return bool(self)

    def move(self, item):
        item_position = self.state.index(item)
        if self.__is_legal_above_or_below(item_position) \
                or self.__is_legal_edge(item_position) \
                or self.__is_legal_middle(item_position):
            old_empty = self.empty_field
            self[item_position] = None
            self[old_empty] = item
        else:
            raise IllegalMoveError

    def __is_legal_above_or_below(self, item_position):
        return item_position % 4 == self.empty_field % 4 \
               and abs(item_position - self.empty_field) == 4

    def __is_legal_edge(self, item_position):
        return (
                (
                        self.empty_field % 4 == 0 and
                        item_position == self.empty_field + 1
                ) or
                (
                        self.empty_field % 4 == 3 and
                        item_position == self.empty_field - 1
                )
        )

    def __is_legal_middle(self, item_position):
        return (
                (
                        self.empty_field % 4 == 1 or
                        self.empty_field % 4 == 2
                ) and
                (
                        item_position == self.empty_field - 1 or
                        item_position == self.empty_field + 1
                )
        )


class IllegalMoveError(Exception):
    pass
