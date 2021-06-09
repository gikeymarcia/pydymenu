#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import pydymenu
import pytest


def test_has_bin():
    assert pydymenu.has_bin("fzf") == True
    assert pydymenu.has_bin(None) == False
    assert pydymenu.has_bin("") == False
    assert pydymenu.has_bin("printf") == True


# def test_unavilable_package(monkeypatch):
#     monkeypatch.setenv("PATH", "")
#     assert pydymenu.fzf().available == False


# def test_avilable_package():
#     assert pydymenu.fzf().available == True


# def test_menu_modes_all_missing(monkeypatch):
#     monkeypatch.setenv("PATH", "")
#     assert pydymenu.Menu().present() == {
#         "fzf": False,
#         "rofi": False,
#         "dmenu": False,
#     }


# def test_menu_generic_missing(monkeypatch):
#     monkeypatch.setenv("PATH", "")
#     menu = pydymenu.Menu()
#     assert menu.present() == {
#         "fzf": False,
#         "rofi": False,
#         "dmenu": False,
#     }


# def test_menu_generic_found():
#     menu = pydymenu.Menu()
#     assert menu.present() == {
#         "fzf": True,
#         "rofi": True,
#         "dmenu": True,
#     }


# def test_fzf_default_prompt():
#     fzf = pydymenu.fzf()
#     assert fzf.prompt == " > "


# @pytest.mark.parametrize(
#     "prompt_val, except_type",
#     [
#         ([], TypeError),
#         (type(str), TypeError),
#         # ("monkey", KeyError),
#     ],
# )
# def test_fzf_bad_prompt(prompt_val, except_type):
#     with pytest.raises(except_type) as except_info:
#         fzf = pydymenu.fzf(prompt=prompt_val)
#         print(fzf.prompt)
#     assert except_info.type == except_type


# def test_set_fzf_prompt():
#     fzf = pydymenu.fzf(prompt="ready")
#     assert fzf.prompt == "ready"


# vim: set foldlevel=2:
