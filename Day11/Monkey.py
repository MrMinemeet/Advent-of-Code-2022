class Monkey:
    # Items = Lists worry level for each item the monkey has. IN the order the monkey well check them
    # Operation = Changes worry level as the monkey inspects it
    # test = Tests where the monkey throws the item next (condition, if_true, if_false)
    def __init__(self, name: str, items=None, operation="", test: tuple = (0, 0, 0)):
        self.name = name
        self.items = items or []
        self.operation = operation
        self.test = test

    def __repr__(self) -> str:
        return f"Monkey ({self.items}, {self.operation}, {self.test})"

    def __str__(self) -> str:
        return f"Monkey {self.name}: {self.items}"
