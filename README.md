# PygameLevelEditor
A level editor for pygame based applications 

## Current Idea
This level editor aims to be an application that you can use to instantly get started
with your projects. For now, this is something that only I intend to use, but I want to
build it in a way that others can use too.


### Features Planned
  - Placing tiles
  - Default tileset to start prototyping out of the box
  - Loading custom images using dialogue box interface
  - Layers [Tiled and Object]
  - Zoom in / Zoom out
  - Custom tile names
  - Custom layer names

## Versioning and releases 
As of now, I won't be releasing this to pypi.org
This is primarily because it doesn't solve anything or do the things 
I intend it to(yet). Hence, after version 0.0.1 gets released, the
way you use this is by including the line
```
git+https://github.com/blankRiot96/PygameLevelEditor/
```
In your `requirements.txt` file. 

### Versions
  - `0.0.1`, By 0.0.1 I aim to have the very basic functionality required to
  load tilesets into the editor, import this package and use it for your games, build the foundation
  of how this tool is meant to be used, and afterwards use it for a game to test things out.
  I won't be implementing aesthetic UI or layering yet, as they aren't needed for the MVP which
  this version intends to be.
  - `0.0.2`, By 0.0.2 I wish to have the more core features of this editor such as zoom in/out, 
    better UI and polishing with VFX when placing tiles. This will still not be released to pypi.org.
  - `0.0.3`, *This* is the version that I intend to publish to `pypi.org`, and will also include
  a more complete version of what I want this editor to be. This version will include layering(yes!), 
  allow animated tiles, *two* abstract base classes for players in platformers and topdown games repsectively,
  and more UI polishing.
  - `0.0.4+`, from this version and above I will include things that are beyond my reach for now,
  such as an inbuild pixel art editor for better/quicker prototyping and animation editor. But this
  version and beyond will hopefully be providing requested features and doing bug fixes.

The reason why I intend to distribute the releases across multiple versions like this, rather
than packing all of it into `0.0.1`, is that this level editor/builder is a pretty big project, and
honestly speaking I don't think I could stay dedicated to it the entire time. But at the same time, I 
wouldn't want to abandon or quit this one like the many other previous ones of mine. I want
this project to materialize, and for that I want to feel that I've published and completed complete
versions of this editor, so that I can come back and implement a particular feature. If you notice,
every version planned has its own independant mechanism that separates it from its previous ones,
so it means that I can jump into this project with a new task to fill everytime. I hope this works out,
and one crucial factor for that to happen is that the code quality should be pretty good. I intend to build
a really abstract and reusable/configurable hierarchy code-wise from the get go. That means between 
`0.0.1` to `0.0.8`, there should be no need for any major refactoring, and I should feel happy with the 
code I've written. While this may imply I haven't improved in that duration(which might as well be years), 
I hope it just means that the structure I've build is just that good, and wouldn't require any huge refactors.
Also, hopefully down the line I gain other wonderful contributors who help me achieve my goals, so any refactoring 
won't completely be only on my shoulders.


## Contributions
Contributions are always welcome. There is no guide yet.
