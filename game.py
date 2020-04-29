class Game:
    def __init__(self, initial=None):
        self.state = list()
        if type(initial) is list and len(initial) == 16:
            self.state = initial
        else:
            self.__set_default_state()

    def __set_default_state(self):
        for i in range(1, 16):
            self.state.append(i)
        self.state.append(None)

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

