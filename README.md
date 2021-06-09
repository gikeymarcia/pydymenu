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
