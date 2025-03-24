from manim import *
import numpy as np
from RENDER import RENDER

class MatrixMultiplication3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create axes
        axes = ThreeDAxes()
        self.add(axes)
        
        # Define matrices
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[2, 0], [1, 2]])
        
        # Create matrix objects
        matrix1_mob = Matrix(matrix1)
        matrix2_mob = Matrix(matrix2)
        
        # Position matrices
        matrix1_mob.shift(LEFT * 3)
        matrix2_mob.shift(RIGHT * 3)
        
        # Display matrices
        self.play(Write(matrix1_mob), Write(matrix2_mob))
        self.wait(2)
        
        # Perform matrix multiplication
        result_matrix = np.dot(matrix1, matrix2)
        result_matrix_mob = Matrix(result_matrix)
        
        # Position result matrix
        result_matrix_mob.shift(DOWN * 3)
        
        # Display result matrix
        self.play(Write(result_matrix_mob))
        self.wait(2)

if __name__ == '__main__':
    RENDER(__file__)