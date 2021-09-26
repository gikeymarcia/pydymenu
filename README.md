# pydymenu: A Pythonic interface for `fzf` and `rofi`

A single package to serve all your dynamic menu-ing needs with a simple Pythonic 
interface.

## Installation from [PyPi](https://pypi.org/project/pydymenu/)

```bash
pip install --user pydymenu
```

## Usage 

```python
from pydymenu import fzf, rofi

people = ["Joe", "Sam", "Daniel", "Bret", "Jordan", "Eric", "Lex"]

# fzf
talker = fzf(people, prompt="Pick a podcaster: ", preview="figlet {}")
if talker:
    return talker[0]

# rofi
gui_select = rofi(people, prompt="Pick a podcaster: ", multi=True)
if gui_select:
    return gui_select
```

`pydymenu.MENU(item: Iterable[str], **options) -> Union[List[str], None]`

### Options

`prompt: str`
: The prompt text shown at the selection _(default: ` > `)_

`multi: bool`
: Whether or not to allow multiple selections. _(default: `multi=False`)_

`case_sensitive: bool`
: Whether or not to use case sensitive search _(default: `case_sensitive=False`)_

`preview: str` **(fzf only)**
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
  of length 1.

**Roadmap:**

- Support for _dmenu_ systems

### Source of Truth

This project is available on [GitHub](https://github.com/gikeymarcia/pydymenu) and
[GitLab](https://gitlab.com/gikeymarcia/pydymenu). Each push to `master` 
automatically goes to both so choose whichever platform you prefer. All releases 
are uploaded to [PyPi](https://pypi.org/project/pydymenu/) 

Big thanks to [fzf](https://github.com/junegunn/fzf) and [Rofi](https://github.com/davatorium/rofi) developers for making the utilities this tool relies upon.
