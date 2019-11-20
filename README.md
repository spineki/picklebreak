PickleBreak: A Centrale-Supelec project
=
A python software designed to challenge your python skills on python puzzles (that's a lot of python).

## Install requirements
- Python is installed on your computer
- Open your terminal
- Go to picklebreak folder
- Type: __pip install -r requirements.txt__
- Wait for the installation process

# Launch the game

run picklebreak.py with python (E.G: type __python picklebreak.py__ in your terminal)

## Create a new level

   - In the level_manager.py file (src.core.libs.level_manager.py), use the [write_level](src/core/libs/level_manager.py) function
   - The function takes 2 arguments:
        * level: (default None). the number of the level that need to be created.\
            If no number is given, a new level is create before every level, that are incremented by on level.  
            Example: (new_0, new_1)-> write_level()-> (new_0,new_1, new_2)  where new_1 is the previous new_0

        * backend_file(default None). path to a backend file that will handle authorized imports, functions...
            
   The newly created level is finally saved in the [levels.json file.](src/res/levels/levels.json)

## Authors: 
- [Yohann Bosqued]
- [Remon Majoor](https://github.com/Remon-prog)
- [Alexandre LeBian]
- [Victor Collodel]
- [Antoine Marras](https://github.com/spineki)

### Supervised by: 
[Pascual Romain](https://github.com/romainpascual)

## Contributing
[Please follow these steps to contribute](contributing.md).

## License
This project is licensed under the [MIT License](LICENSE.md).