from logic import *
from ui.UI import init_ui


if __name__ == "__main__":

    # data
    order = order()
    order.append_entity(entity("Kobold", 24, -2))
    order.append_entity(entity("Istota", 12, 4))
    order.append_entity(entity("Smok", 200, 10))

    # UI
    init_ui(order)
