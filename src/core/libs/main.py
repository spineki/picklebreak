from src.core.libs.GUI.test import Application
from src.core.libs.level_loader import LevelLoader

class Core:
    def __init__(self):
        self.window = Application()
        self.level_loader = LevelLoader()

