# `pydymenu`: Pythonic wrapper for `fzf` and `rofi`

A single package to serve all your dynamic menu-ing needs with a simple Pythonic 
interface.

# Installation from [PyPi](https://pypi.org/project/pydymenu/)

```bash
pip install --user pydymenu
```

## Usage `pydymenu.MENU(input_list, **options) -> Union[list[str], None]`

```python
import pydymenu

people = ["Joe", "Sam", "Daniel", "Bret", "Jordan", "Eric", "Lex"]

# simple
rofi = pydymenu.rofi(people, prompt="Pick a podcaster: ")
fzf = pydymenu.fzf(people, prompt="Pick a podcaster: ")

# mutli
fzf = pydymenu.fzf(people, prompt="Pick a podcaster: ", multi=True)
rofi = pydymenu.rofi(people, prompt="Pick a podcaster: ", multi=True)
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

### FZF Options

`preview`
: Command that will be run on each entry and displayed as it's preview when 
using the fuzzy finder.


## Project Status

Working support for the most common `fzf` and `rofi` use cases. Currently 
expanding functionality for those two programs then going to move onto adding 
`dmenu` support.

I'm trying to keep this package as a pretty simple drop-in replacement for 
[`iterfzf`](https://github.com/dahlia/iterfzf). Biggest design changes are:

- `fzf` automatically sorts results based on match quality.
- Selections always return lists of strings. When `multi=False` returns a list 
  of legnth 1.


**Roadmap:**

- Support for _dmenu_ systems

### Source of Truth

This project is available on [github](https://github.com/gikeymarcia/pydymenu) 
and
[gitlab](https://gitlab.com/gikeymarcia/pydymenu). Each push to `master` 
automatically goes to both so choose whichever platform you prefer.
