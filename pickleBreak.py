from src.core.game import Core
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = "python pickleBreak.py", description = "Challenging python game.")
    parser.add_argument("-n", dest = "new_levels", type = int, default = -1, help = "Number of blank levels to generate.")
    args = parser.parse_args()

    new_levels = max(-1, args.new_levels)

    c = Core()

    if new_levels == -1:
        c.load_challenge(c.save.save_dict["level"])
        c.run()
    else:
        c.create_new_levels(new_levels)