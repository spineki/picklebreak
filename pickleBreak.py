from src.core.game import Core

if __name__ == '__main__':
    c = Core()
    c.load_challenge("default")
    c.run()