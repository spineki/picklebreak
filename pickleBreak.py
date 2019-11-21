from src.core.game import Core
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = "python pickleBreak.py", description = "Challenging python game.")
    parser.add_argument("-n", dest = "new_levels", type = int, default = -1, help = "Number of blank levels to generate.")
    parser.add_argument("-r", dest = "remove_save", action = "store_true", help = "Reset saves.")
    args = parser.parse_args()

    new_levels = max(-1, args.new_levels)
    rem = args.remove_save

    c = Core()

    if new_levels == -1 and rem == False:
        c.load_challenge(c.save.save_dict["level"])
        c.run()
    if rem == True:
        c.reset_game()
    if new_levels != -1:
        c.create_new_levels(new_levels)