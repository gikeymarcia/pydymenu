# `pydymenu`: Python wrapper for `fzf`, `rofi`, and `dmenu`

A single package to serve all your dynamic menu-ing needs with a simple Pythonic 
interface.

# Installation from PyPi

```bash
pip install --user pydymenu
```

## Usage

```python
from pydymenu import rofi, fzf

# using rofi
selection = rofi(['one', 'two', 'three'], prompt="Pick a number: ")
# using fzf
selection = fzf(['one', 'two', 'three'], prompt="Pick a number: ")
```

### Universal Options

`prompt`
: The prompt text shown at the selection _(default: ` > `)_

`multi`
: Whether or not to allow multiple selections. When `multi=True` returns a list 
of selected values. If one selection is made returns a list of length one. If no 
selection is made returns `None`. _(default: `multi=False`)_

`case_sensitive`
: Whether or not to use case sensitive search _(default: 
`case_sensitive=False`)_

### Project Status

Working support for the most common `fzf` and `rofi` use cases. Currently 
expanding functionality for those two programs then going to move onto adding 
`dmenu` support.

I'm trying to keep this package as a pretty simple drop-in replacement for 
`iterfzf`. Biggest design changes are:

- `fzf` automatically sorts results based on match quality.
- `multi=True` returns a list even if only one selection is made.


**Roadmap:**

- `fzf` preview
- Support for _dmenu_ systems

```python
dmenu = pydymenu.dmenu(['one', 'two', 'three'], prompt='Pick a number: ')
rofi = pydymenu.rofi(['one', 'two', 'three'], prompt='Pick a number: ')
```

### Source of Truth

This project is available on [github](https://github.com/gikeymarcia/pydymenu) 
and
[gitlab](https://gitlab.com/gikeymarcia/pydymenu). Each push to `master` 
automatically goes to both so choose whichever platform you prefer.
