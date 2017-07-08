import numpy as np
import math

class Angle:

    def calculate_vectors(self,front_location,rear_location_one,rear_location_two):
        self.vector_one = np.array(front_location) - np.array(rear_location_one)
        self.vector_two = np.array(front_location) - np.array(rear_location_two)

    def vector_magnitudes(self):
        self.magnitude_one = math.sqrt(sum(self.vector_one**2))
        self.magnitude_two = math.sqrt(sum(self.vector_two**2))

    def vector_dot_product(self):
        self.dot_product = np.vdot(self.vector_one,self.vector_two)

    def calculate_angle(self):
        self.angle = math.acos(self.dot_product/(self.magnitude_one*self.magnitude_two))*180/math.pi
        return self.angle

the_angle = Angle()

the_angle.calculate_vectors([0,0,0],[1,0,0],[0,1,0])

the_angle.vector_magnitudes();

the_angle.vector_dot_product();

theta = the_angle.calculate_angle()

print(theta)