import matplotlib.pyplot as plt
import os

class Plotter:
    @staticmethod
    def save_plot(trajectories, output_path='plot.png'):
        plt.figure(figsize=(10, 6))
        for trajectory in trajectories:
            x_vals, y_vals = zip(*[(row[3], row[2]) for row in trajectory])
            plt.plot(x_vals, y_vals, label=f'ID {trajectory[0][1]}')
        plt.ylabel('Latitudinal (y)')
        plt.xlabel('Longitudinal (x)')
        plt.title('Trajectories')
        plt.legend()
        plt.grid(True)
        plt.savefig(output_path)
        plt.close()


