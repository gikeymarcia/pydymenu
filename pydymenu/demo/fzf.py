from pydymenu import fzf

# import sample data
from pydymenu.demo_data import gen_options as items

fzf_selection = fzf(
    items,
    prompt="Choose with fzf: ",
    multi=True,
    preview="echo {} | sed -E 's/[aeiou]//g' | figlet",
)
