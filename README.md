PickleBreak: A CentraleSupélec project
=
A python software designed to challenge your python skills on python puzzles (that's a lot of python).

## Install requirements
- Python is installed on your computer
- Open your terminal
- Go to picklebreak folder
- Type: __pip install -r requirements.txt__
- Wait for the installation process

# Launch the game

Run picklebreak.py with python (E.G: type __python picklebreak.py__ in your terminal)

## Create a new level
### Init a level
Just run __python picklebreak.py -n X__ and it will create in [levels.json](src/res/levels/levels.json) X empty levels.

### Modify Level  
The Level is a dictionary in the levels.json. Here's an example

    "0_the_basics": {
        "id": "0_the_basics",
        "next": "1_halfed",
        "backend": "0_the_basics",
        "scripts": [
            "# Welcome to PickleBreak. Learn a large component",
            "# of python functions and libraries by resolving challenges.",
            "# The goal is to retrieve a 64-key like this one:",
            "# {}",
            "# Pressing reset will regenerate all key-based elements",
            "# whereas execute will reset and run your code.",
            " ",
            "# To send your answer, just call send_key like:",
            "# send_key(key)",
            "# Here, just try it, the key is right there.",
            "s = \"{}\"",
            ""
        ],
        "imports": [],
        "hints": [
            {
                "type": "txt",
                "data": "Level 0: The Basics."
            }
        ]
    },

We need to fill:       
-__"id"__ akka the level name  

-__"next"__: id of the next level  

-__"backend"__: the backend file that will control the generation of objects and their closing

-__"script"__: a list of string that will be displayed on the notepad part.  
     
     - empty string "" creates a writable field for the user (do not forget it!!)
     - other strings will create an instruction field, immutable  

-__"import"__: list of authorized imports

-__"hints:"__ a list of dictionary that contains
    
    - "type": type of the hint (currently supported: text. images incoming)
    - "data": what to display as a hint!

### Add backend to level
A level needs a backend file where the key will be changed, sliced, modified with your own challenging method!  
Here's an example:

    def gen (key, hints_data, scripts):
        """
            This function will be called on set and reset of the level.
            The level key, the hints_data and the scripts table are given as parameters.
            This function must returns a tuple with the 2 first elements being a parsed version of
            hints_data and scripts, and the third additionnal objects that needs to be closed
            is a special way.
        """
    
        new = hints_data.copy()
        new[0] = new[0].format(key)
    
        new_s = scripts.copy()
        new_s[0] = new_s[0].format(key)
    
        return new, new_s, [5]
    
    def close (key, objs):
        """
            This fuction is called on exit and reset of the level (before gen).
            It is used to softly close / kill objects or do post-level cleaning.
        """
    
        print(objs[0])
    


## Authors:
- [Yohann Bosqued](https://github.com/Mrlag31)
- [Remon Majoor](https://github.com/Remon-prog)
- [Alexandre LeBian](https://github.com/alex-lb33)
- [Victor Collodel]
- [Antoine Marras](https://github.com/spineki)

### Supervised by: 
[Pascual Romain](https://github.com/romainpascual)

## Contributing
[Please follow these steps to contribute](contributing.md).

### Trello Link
[Here](https://trello.com/b/9lrhoAEf/pickle-break), take a look at the project plannig

## License
This project is licensed under the [MIT License](LICENSE.md).