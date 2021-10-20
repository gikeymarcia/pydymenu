from pydymenu import rofi

# import sample data
from pydymenu.demo_data import gen_options as items

rofi_selection = rofi(
    items,
    prompt="Choose with rofi: ",
    multi=True,
)
