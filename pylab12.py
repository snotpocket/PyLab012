from simulation import *
from solarsystem import *
from planet import *
from sun import *
if __name__ == '__main__':
    solar_system = SolarSystem()
    the_sun = Sun("SOL", 5000, 10000000, 5800, 0, 0)
    solar_system.add_sun(the_sun)
    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, 100, 100)
    solar_system.add_planet(earth)
    mars = Planet("MARS", 40.5, .1, 62, 10.0, 125.0, 100, 100)
    solar_system.add_planet(mars)
    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()
