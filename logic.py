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
            self.entities = []
        else:
            self.entities = entities

    def __getitem__(self, index):
        if index < 0 or index >= len(self.entities):
            raise IndexError("Index out of range")
        return self.entities[index]

    def __len__(self):
        return len(self.entities)

    def _append(self, new_entity: entity):
        self.entities.append(new_entity)

    def _roll_i_for_all(self):
        for entity in self.entities:
            entity.roll_initiative()

    def _display_order(self):
        print("Nr.", "Nazwa", "PW", "Inicjatywa")
        for i in range(len(self.entities)):
            print(i + 1, ". ", str(self.entities[i]), sep="")
        print()


if __name__ == "__main__":
    kobold = entity("Kobold", 24, -2)
    print(str(kobold))
    kobold.roll_initiative()
    test = order()
    test._append(kobold)
    test._append(entity("Istota", 12, 4))
    test._display_order()
    test._roll_i_for_all()
    test._display_order()
