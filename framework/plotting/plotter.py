import matplotlib.pyplot as plt
import os

class Plotter:
    @staticmethod
    def save_plot(trajectories, output_path='plot.png'):
        plt.figure(figsize=(10, 6))
        for trajectory in trajectories:
            x_vals, y_vals = zip(*[(row[2], row[3]) for row in trajectory])
            plt.plot(x_vals, y_vals, label=f'ID {trajectory[0][1]}')
        plt.xlabel('Latitudinal (x)')
        plt.ylabel('Longitudinal (y)')
        plt.title('Trajectories')
        plt.legend()
        plt.grid(True)
        plt.savefig(output_path)
        plt.close()


