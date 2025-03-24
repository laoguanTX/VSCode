import os
from SET_GPUS import set_gpus

def RENDER(py_file_name):
    set_gpus(1)
    cmd = "manim " + py_file_name + " -p"
    os.system(cmd)

if __name__ == "__main__":
    RENDER("RENDER.py")