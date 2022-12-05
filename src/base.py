import os

from dotenv import load_dotenv

load_dotenv()


class AdventOfCode:
    def __init__(self):
        self.input = []

    def load(self, file: str):
        with open(file, "r") as f:
            self.input = f.read().splitlines()

        return self
