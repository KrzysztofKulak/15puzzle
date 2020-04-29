class Game:
    def __init__(self, initial=None):
        self.state = list()
        if type(initial) is list and len(initial) == 16:
            self.state = initial
        else:
            self.state = self.__get_default_state()
        self.desired_state = self.__get_default_state()

    @staticmethod
    def __get_default_state():
        default_state = list()
        for i in range(1, 16):
            default_state.append(i)
        default_state.append(None)
        return default_state

    def __getitem__(self, item):
        return self.state[item]

    def __str__(self):
        state_list = list(self.state)
        return (
            f"{state_list[:4]}\n"
            f"{state_list[4:8]}\n"
            f"{state_list[8:12]}\n"
            f"{state_list[12:]}\n"
        )

    def __repr__(self):
        return f"Game({self.state})"

    def __bool__(self):
        return self.state == self.desired_state

    def check_if_won(self):
        return bool(self)

