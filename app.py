import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs", "termcolor", "src"))

from termcolor import colored  # noqa: E402


def main():
    print(colored("Вітаємо у TaskTracker v1! Увійдіть у систему.", "green"))


if __name__ == "__main__":
    main()
