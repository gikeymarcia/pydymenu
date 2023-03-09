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
try the command-line interface.

```bash
python3 -m pydymenu --fzf
python3 -m pydymenu --rofi
```

## Basic Usage

To begin, use `fzf` to pick an item from a list.

```python
import pydymenu

with_a_list = ["apples", "grapes", "bananas", "pears", "strawberries"]
choice = pydymenu.fzf(with_a_list, prompt="Which fruit? ")
print(f"Enjoy your {choice[0]}")
# if you wanted to use rofi instead
choice = pydymenu.rofi(with_a_list, prompt="Which fruit? ")
```

My favorite way to use this tool is with a dictionary of values. Python makes it
easy to select from a list of human-readable names but retrieve programming
related values like lambda, lists, or dictionaries, or even your own custom
objects!

```python
import pydymenu

from_dict = {
    "Coder": {"First": "Mikey", "Last": "Garcia", "alignment": "chaotic good"},
    "square()": lambda x: x*x,
    "List of fruits": ["apples", "grapes", "bananas", "pears", "strawberries"],
    "rofi selector": pydymenu.rofi,
    "fzf selector": pydymenu.fzf,
}
choice = pydymenu.fzf(from_dict, prompt="Which option? ")
if choice:
    value = from_dict[choice[0]]
    print(f"{choice[0]}: {value}")
else:
    print("No selection made.")

```

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
import pydymenu

selection = pydymenu.fzf(items)
if selection:
    print(selection[0])
else:
    print('No selection made.')
```

## Development

To get started with development:

- clone the repository
- install development dependencies
- `source ./tools.sh`

See my [Super Python Project Template][template] on GitHub to learn more about
the automated features of this development environment. Clone the repo to get
your own Python projects up and running quickly!

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
[template]: <https://github.com/gikeymarcia/super-python-project-template>
"Super Python Project Template @ GitHub"
