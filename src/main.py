from src.settings.settings import TITLE
from src.user_interface.control_interface import ControlInterface

if __name__ == '__main__':

    root = ControlInterface()
    root.title(string=TITLE)
    root.mainloop()

