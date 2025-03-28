from gaphor.abc import Service, ActionProvider
from gaphor.core import action


class MBSEMethodology(Service, ActionProvider):

    def __init__(self, element_menu):
        self.element_menu = element_menu
        print(type(element_menu))
        if self.element_menu:
            element_menu.add_actions(self)

    def shutdown(self):
        self.element_menu.remove_actions(self)

    @action(
        name="MBSEMethodology",
        label="Frank Was Here!",
        tooltip="Foobar",
    )
    def mbse_methodology_action(self):
        print("FVB WAZ ERE!")
