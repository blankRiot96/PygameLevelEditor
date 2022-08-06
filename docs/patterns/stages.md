# Stages
Stages is a design pattern made specifically for game development
which involves low level control of events.

## What is it and where should one use it?
It essentially revolves around a series of inheritance 
to split up game logic while still having access to all previous data initialized.
In simpler words, it allows you to split up all your logic 
into bits and pieces which flow in a particular order.

An example,
```py
class InitLevelStage:
    def __init__(self):
        self.info = {"difficulty": "hard"}
        self.tilemap = TileMap("tilemap.json")
    
class PlayerStage(InitLevelStage):
    def __init__(self):
        super().__init__()
        self.player = Player()
    
    def update(self):
        self.player.update()
        for tile in self.tilemap:
            player.handle_collision(tile)
    
    def draw(self):
        self.player.draw()

class Level(PlayerStage):
    pass
```

Over here, we split up our logic pertaining to the `Level` through a series of inheritance. 
The `Level` itself should only contain top-level information about the level which wouldn't be 
needed in its logic itself, in most cases you only create the `Level` identifier so that it can be 
imported elsewhere, you normally don't have logic in the `Level` identifier.

Each block of inheritance is called a "stage". Each stage should initialize, update and draw 
any action or event that goes on in a game state.
For example, say that we made a little game, and here we are dealing with the level game state.
We have tiles, which we store as an attribute to the `Level` class, and also a player, which needs each `Tile`
object in a tile map. The `TileMap` object is iterable, and each iterator is an instance of `Tile`.
Over here, we make our own little `PlayerStage`, and over here we deal with any logic that modifies or deals with the player.

That means, if the player is being modified, that logic should go to the `PlayerStage`.

### Where should this be used?
This has been found to be useful when splitting up logic of game states.
This pattern has been used in 2 games thus far, namely [Dariyoki](https://github.com/dariyoki/dariyoki) 
and [Dave's Anniversary](https://github.com/blankRiot96/Daves-Anniversary)

A perfect showcase of how stages has helped clean up a code base immensely can be found in dariyoki 
[here](https://github.com/dariyoki/dariyoki/blob/main/dariyoki/states/levels.py)

But the best usage of stages so far has been for the pygame community summer game jam submission,
you can find its usages [here](https://github.com/blankRiot96/Daves-Anniversary/blob/main/game/states/main_menu.py)

This code base will be using stages extensively.

## Rules of stages
  1. All logic pertaining to an event in a game, such as wind strength, grass, rendering messages, etc. must
  be contained within it's own Stage. Each stage can have substages.

  2. Any code modifying an entity or event must go within its respective stage.

  3. The last and final stage, called the game state class, should be untouched 
  and contain the least amount of logic possible.

  4. Each `super().method()` call should *always* be at the top of the method in which it is being called.
  Any fancy-schmancy logic flow can be separated into its own stages.

  5. Stages must use inheritance and composition is not allowed.


## Pros and Cons
Pros:
  - Stages allow you to isolate your logic into separated code blocks, while
  still having direct access to all the data required for the logic.
  - Stages allow you to also split your logic across multiple files, which is why
  simply creating thousands of method to the game state class would not be the same.
  Also the `__init__` method of the game state class would become extremely bloated,
  an example of such an atrocity - <a href="https://github.com/dariyoki/dariyoki/blob/main/dariyoki/states/levels.py#L252">dariyoki</a>
  - A well defined logic flow.

Cons:
  - Stages is new and underdeveloped. It hasn't been tested and desired as much
  as other patterns(yet).
  - There aren't many online resources for this pattern there, this is the only
  resource at present(6th August 2022).
  - It is complicated.
