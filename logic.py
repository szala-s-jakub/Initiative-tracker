from random import randint


class entity:
    def __init__(self, name: str, max_hp, initiative_bonus, initiative=0):
        self.name = name
        self.hp = max_hp
        self.hp = max_hp
        self.max_hp = max_hp
        self.initiative_bonus = initiative_bonus
        self.initiative = initiative

    def __str__(self):
        return (
            self.name
            + " "
            + str(self.hp)
            + "/"
            + str(self.max_hp)
            + " "
            + str(self.initiative)
        )

    def roll_initiative(self):
        rzut = randint(1, 20)
        self.initiative = self.initiative_bonus + rzut

    def change_hp(self, new_hp):
        self.hp = new_hp

    def _clone(self):
        return self.name, self.hp, self.max_hp, self.initiative_bonus, self.initiative


class order:
    def __init__(self, entities=None):
        if entities is None:
            self.__entities = []
        else:
            self.__entities = entities

    def __getitem__(self, index):
        if index < 0 or index >= len(self.__entities):
            raise IndexError("Index out of range")
        return self.__entities[index]

    def __len__(self):
        return len(self.__entities)

    def __iter__(
        self,
    ):
        return iter(self.__entities)

    def append_entity(self, new_entity: entity):
        self.__entities.append(new_entity)

    def remove_at_index(self, index):
        if index < 0 or index >= len(self.__entities):
            raise IndexError("Index out of range")
        del self.__entities[index]

    def roll_i_for_all(self):
        for entity in self.__entities:
            entity.roll_initiative()

    def display_order(self):
        print("Nr.", "Nazwa", "PW", "Inicjatywa")
        for i in range(len(self.__entities)):
            print(i + 1, ". ", str(self.__entities[i]), sep="")
        print()


if __name__ == "__main__":
    kobold = entity("Kobold", 24, -2)
    print(str(kobold))
    kobold.roll_initiative()
    test = order()
    test.append_entity(kobold)
    test.append_entity(entity("Istota", 12, 4))
    test.display_order()
    test.roll_i_for_all()
    test.display_order()
