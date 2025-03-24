from manim import *
from RENDER import RENDER
import math
from SET_GPUS import set_gpus

class Tailor_sin(Scene):
    def construct(self):
        set_gpus([0,1])
        ax = Axes(
            x_range=[-2.25*PI, 2.25*PI,0.5*PI],
            y_range=[-1, 1],
            x_length=4.5*PI,
            y_length=2,
        )
        function = lambda x: math.sin(x)
        graph = FunctionGraph(function, x_range=(-2*PI, 2*PI), color=YELLOW)
        self.play(Create(ax))
        self.play(Create(graph))
        self.wait(0.2)

        function1 = lambda x: x
        graph1 = FunctionGraph(function1, x_range=(-2*PI, 2*PI), color=RED)
        tex1 = MathTex(r"f(x)=x")
        tex1.move_to(UP*3)
        self.play(Create(graph1))
        self.play(Write(tex1))
        self.wait(0.2)

        function2 = lambda x: x - x ** 3 / 6
        graph2 = FunctionGraph(function2, x_range=(-2*PI, 2*PI), color=RED)
        tex2 = MathTex(r"f(x)=x-\dfrac{x^3}{2!}")
        tex2.move_to(UP*3)
        self.play(Transform(graph1, graph2),Transform(tex1, tex2))
        self.wait(0.2)

        function3 = lambda x: x - x ** 3 / 6 + x ** 5 / (2 * 3 * 4 * 5)
        graph3 = FunctionGraph(function3, x_range=(-2*PI, 2*PI), color=RED)
        tex3 = MathTex(r"f(x)=x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}")
        tex3.move_to(UP*3)
        self.play(Transform(graph1, graph3),Transform(tex1, tex3))
        self.wait(0.2)

        function4 = lambda x: x - x ** 3 / 6 + x ** 5 / (2 * 3 * 4 * 5) - x ** 7 / (2 * 3 * 4 * 5 * 7)
        graph4 = FunctionGraph(function4, x_range=(-2*PI, 2*PI), color=RED)
        tex4 = MathTex(r"f(x)=x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\dfrac{x^7}{7!}")
        tex4.move_to(UP*3)
        self.play(Transform(graph1, graph4),Transform(tex1, tex4))
        self.wait(0.2)

        function5 = lambda x: x - x ** 3 / 6 + x ** 5 / (2 * 3 * 4 * 5) - x ** 7 / (2 * 3 * 4 * 5 * 6 * 7) + x ** 9 / (2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
        graph5 = FunctionGraph(function5, x_range=(-2*PI, 2*PI), color=RED)
        tex5 = MathTex(r"f(x)=x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\dfrac{x^7}{7!}+\dfrac{x^9}{9!}")
        tex5.move_to(UP*3)
        self.play(Transform(graph1, graph5),Transform(tex1, tex5))
        self.wait(0.2)

        function6 = lambda x: x - x ** 3 / 6 + x ** 5 / (2 * 3 * 4 * 5) - x ** 7 / (2 * 3 * 4 * 5 * 6 * 7) + x ** 9 / (2 * 3 * 4 * 5 * 6 * 7 * 8 * 9) - x ** 11 / (2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11)
        graph6 = FunctionGraph(function6, x_range=(-2*PI, 2*PI), color=RED)
        tex6 = MathTex(r"f(x)=x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\dfrac{x^7}{7!}+\dfrac{x^9}{9!}-\dfrac{x^11}{11!}")
        tex6.move_to(UP*3)
        self.play(Transform(graph1, graph6),Transform(tex1, tex6))
        self.wait(0.2)

        graphfinal = FunctionGraph(lambda x:math.sin(x), x_range=(-2*PI, 2*PI), color=RED)
        texfinal = MathTex(r"f(x)=x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\dfrac{x^7}{7!}+\dfrac{x^9}{9!}-\dfrac{x^{11}}{11!}+\cdots")
        texfinal.move_to(UP*3)
        self.play(Transform(graph1, graphfinal),Transform(tex1, texfinal))
        self.wait(2)

if __name__=="__main__":
    RENDER("demo2.py")