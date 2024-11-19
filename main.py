from src.banner import show_banner
from src.dsTokenChecker import discord_token_checker
from rich.console import Console
from src.console import *


def infinite_input():
  while True:
    user_input = console.input("█")

    if user_input.lower() == "exit":
      console.print("Выход из программы.")
      break
    if user_input == "1":
      show_banner()
      discord_token_checker()
    else:
      show_banner()


def main():
  show_banner()
  infinite_input()


if __name__ == "__main__":
  main()
