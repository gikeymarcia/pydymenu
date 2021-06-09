# `pydymenu`: Python wrapper for `fzf`, `dmenu`, and `rofi`

A single package to serve any of your dynamic menu-ing needs in Python.

# Installation from PyPi

```bash
pip install --user pydymenu
```

## Usage

```python
import pydymenu

selection = pydymenu.fzf(['one', 'two', 'three'], prompt="Pick a number: ")
if selection:
    print(selection)
else:
    print("no selection made")
```

### Work in Progress

The initial release is a proof-of-concept that only covers basic `fzf` usage but 
is most of the use case I need. Biggest missing feature is `--preview` and will 
be added. I'm trying to be similar to `iterfzf` but am not constraining myself 
completely to his design decisions.

**Next big thing:** Support for _other_ menu-ing systems

```python
dmenu = pydymenu.dmenu(['one', 'two', 'three'], prompt='Pick a number: ')
rofi = pydymenu.rofi(['one', 'two', 'three'], prompt='Pick a number: ')
```
