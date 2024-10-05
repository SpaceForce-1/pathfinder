from skyfield.api import load
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ['CG_PDF_VERBOSE'] = '1'

class SolarSystemPlotter:
    def __init__(self):
        self.planets = {
            'Mercury': (0.39, 'gray'),
            'Venus': (0.72, 'orange'),
            'Earth': (1.00, 'blue'),
            'Mars': (1.52, 'red'),
            'Jupiter': (5.20, 'brown'),
            'Saturn': (9.58, 'gold'),
            'Uranus': (19.22, 'cyan'),
            'Neptune': (30.05, 'purple')  # Added Neptune
        }
        self.ts = load.timescale()
        # change the path to the location of the ephemeris file on your system
        self.ephemeris = load('de440s.bsp')

    def calculate_position(self, planet, date):
        try:
            t = self.ts.utc(*date)
            planet_barycenter = self.ephemeris[planet + ' barycenter']
            sun = self.ephemeris['sun']
            barycentric = planet_barycenter.at(t)
            position = barycentric.observe(sun).position.au
            return position[0], position[1]
        except KeyError as e:
            print(f"Error: {e}. Check if the planet name is correct in the ephemeris.")
            raise

    def plot_orbits_and_positions(self, date):
        plt.figure(figsize=(10, 10))
        
        for planet, (a, color) in self.planets.items():
            # Plot orbit as a circle
            theta = np.linspace(0, 2 * np.pi, 100)
            x = a * np.cos(theta)
            y = a * np.sin(theta)
            plt.plot(x, y, color=color, linestyle='--', alpha=0.5)

            # Get actual position and invert it
            px, py = self.calculate_position(planet, date)
            px, py = -px, -py  # Invert both x and y to mirror the position
            
            plt.scatter(px, py, color=color, s=100, label=planet)  # Set dot size to 100 for all planets

        plt.scatter(0, 0, color='yellow', s=200, label='Sun')  # Sun at the origin with larger size
        plt.title(f"Simplified Solar System on {date}")
        plt.xlabel("Distance (AU)")
        plt.ylabel("Distance (AU)")
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.axis('equal')
        plt.xlim(-35, 35)  # Set x-axis limits to keep some distance
        plt.ylim(-35, 35)  # Set y-axis limits to keep some distance
        plt.show()

# Example usage
def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    
    plotter = SolarSystemPlotter()
    plotter.plot_orbits_and_positions((year, month, day, 0, 0))  # Default hour and minute to 0

if __name__ == "__main__":
    main()
