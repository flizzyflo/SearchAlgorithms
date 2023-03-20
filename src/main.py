from src.settings.settings import TITLE
from src.user_interface.control_interface import ControlInterface


if __name__ == '__main__':

    r = ControlInterface()
    r.title(string=TITLE)
    r.mainloop()
