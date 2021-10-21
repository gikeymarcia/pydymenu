# pydymenu: A Pythonic interface for `fzf` and `rofi`

A single package to serve all your dynamic menu-ing needs with a simple Pythonic 
interface.

## Installation

### Dependencies

```bash
sudo apt install fzf rofi -y
```

### From [PyPi][pypi]

```bash
pip3 install pydymenu
# upgrade to newest release (if previously installed)
pip3 install -U pydymenu
```

## Demonstration

To see each finder in action and get a sample code snippet to get you started 
try the module command-line interface.

```bash
python3 -m pydymenu --fzf
python3 -m pydymenu --rofi
```

## Basic Usage

- Import the finder you want
    - `from pydymenu import fzf`
    - `from pydymenu import rofi`
- Takes an iterable object and streams each item into the selected finder tool 
  as soon as it is available.

### `pydymenu.MENU(items: Iterable[str], **options) -> Optional[List[str]]`


### Parameters

`items: Iterable[str]` (_required_)
: The only required argument is an iterable of objects that can be cast to `str`
: If `items` is a [generator][gen] each option will display as it is yielded

`prompt: str`
: The prompt text shown at the selection _(default: ` > `)_

`multi: bool`
: Whether or not to allow multiple selections. _(default: `multi=False`)_

`case_sensitive: bool`
: Whether or not to use case sensitive search _(default: `case_sensitive=False`)_

`preview: str` **(fzf only)**
: Command that will be run on each entry and displayed as it's preview when 
using the fuzzy finder. [Read more in the fzf documentation][prev docs]

### Return Value

As soon as a selection is made the finder closes and returns the result as a 
`list[str]`. If no selection is made and/or the selection is cancelled `None` is 
returned. This return signature allows for the following nice pythonic use case.

```python
from pydymenu import fzf

selection = fzf(items)
if selection:
    print(selection)
else:
    print('No selection made.')
```

## Project Status

I'm trying to keep this package as a pretty simple drop-in replacement for 
[`iterfzf`][iterfzf]. Biggest design changes are:

- `fzf` automatically sorts results based on match quality.
- Selections always return lists of strings. When `multi=False` returns a list 
  of length 1.

**Roadmap:**

- Incorporate built in smart fzf preview script
    - Plan is to make it so `python3 -m pydymenu.fzf_preview {}` would generate 
      previews for a bunch of common file types (and even folders)
        - `.cow`
        - `.deb`
        - `.flf`
        - `.iso`
        - `.json`
        - `.mkv`
        - `.mp3`
        - `.mp4`
        - `.pdf`
        - `.py`
        - `.ttf`
        - `.webm`
        - directories

- ~~Support for _dmenu_~~ this is on the back burner because I'm not using 
  `dmenu` much these days

### Source of Truth

This project is available on [GitHub][github] and [GitLab][gitlab]. Each push to 
`master` automatically goes to both so choose whichever platform you prefer. All 
releases are uploaded to [PyPi][pypi].

Big thanks to [fzf][fzf] and [Rofi][rofi] developers for making the utilities 
this tool relies upon.

[prev docs]: <https://github.com/junegunn/fzf#preview-window>
"fzf on GitHub: preview window"
[fzf]: <https://github.com/junegunn/fzf>
"junegunn/fzf: A command-line fuzzy finder"
[rofi]: <https://github.com/davatorium/rofi>
"Rofi: A window switcher, application launcher, and dmenu replacement"
[github]: <https://github.com/gikeymarcia/pydymenu>
"gikeymarcia/pydymenu @ GitHub: All your dynamic menu-ing needs in one place"
[gitlab]: <https://gitlab.com/gikeymarcia/pydymenu>
"gikeymarcia/pydymenu @ GitLab: All your dynamic menu-ing needs in one place"
[pypi]: <https://pypi.org/project/pydymenu/>
"A pythonic wrapper interface for fzf and Rofi."
[iterfzf]: <https://github.com/dahlia/iterfzf>
"dahlia/iterfzf: Pythonic interface to fzf, a CLI fuzzy finder"
[gen]: <https://realpython.com/introduction-to-python-generators/>
"Real Python: How to use generators and yield in Python"
