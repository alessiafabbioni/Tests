from tkinter import Menubutton
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

money_machine.report()
coffee_maker.report()
is_on: True

while is_on:
    options = menu.get_items()