import os
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box
from src.console import *


def show_banner():
  os.system("cls")
  txt = Text()
  txt.append(f"""\u001b[35m
     ██████   █████ ██████████ ███████████ █████  █████ █████ █████
    ░░██████ ░░███ ░░███░░░░░█░█░░░███░░░█░░███  ░░███ ░░███ ░░███ 
     ░███░███ ░███  ░███  █ ░ ░   ░███  ░  ░███   ░███  ░░███ ███  
     ░███░░███░███  ░██████       ░███     ░███   ░███   ░░█████   
     ░███ ░░██████  ░███░░█       ░███     ░███   ░███    ███░███  
     ░███  ░░█████  ░███ ░   █    ░███     ░███   ░███   ███ ░░███ 
     █████  ░░█████ ██████████    █████    ░░████████   █████ █████
    ░░░░░    ░░░░░ ░░░░░░░░░░    ░░░░░      ░░░░░░░░   ░░░░░ ░░░░░ 
    \033[0m""")
  console.print(txt, justify="center")

  credit = Text.from_ansi(
      "\u001b[35m>\033[0m Discord token checker by Netux\n\n")
  console.print(credit, justify="center")

  table = Table(
      show_header=False,
      box=box.DOUBLE,
      title="Options",
      title_style="bold",
      pad_edge=False,
  )
  table.add_column("Num", style="red")
  table.add_column("Title", style="white")
  table.add_column("Overview", style="dim")

  table.add_row("1", "Check Tokens", "Check all tokens and sorting")

  console.print(table, justify="center")
