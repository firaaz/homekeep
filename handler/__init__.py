"""Handler"""

import os
from dataclasses import dataclass


@dataclass
class Handler:

    def handle(path):
        print(path)
