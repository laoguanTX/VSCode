from manim import *
from RENDER import RENDER
from SET_GPUS import set_gpus

class Try(Scene):
    def construct(self):
        set_gpus([0,1])
        plane0 = NumberPlane(
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.5},
        )
        vector1=Vector([1,0])
        vector2=Vector([0,1])
        plane1 = NumberPlane(
            x_range=[-100, 100, 1],
            y_range=[-100, 100, 1]
        )
        self.add(plane0,plane1)
        self.play(Write(vector1),Write(vector2))
        matrix1 = [[1, 1], [-1, -1]]
        matrix2 = [[1, -1], [-1, 1]]
        self.wait()
        self.play(ApplyMatrix(matrix2, plane1),ApplyMatrix(matrix2, vector1),ApplyMatrix(matrix2, vector2))
        self.play(ApplyMatrix(matrix1, plane1),ApplyMatrix(matrix1, vector1),ApplyMatrix(matrix1, vector2))
        self.wait()

if __name__ == '__main__':
    RENDER("demo1.py")