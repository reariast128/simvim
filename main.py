from app.tui import MyApplication
from typing import List

if __name__ == '__main__':
    notebooks: List = ["Personal, Trabajo, Python"]
    app = MyApplication()
    app.notebooks = notebooks
    app.run()