import numpy as np
from framework.plotting.plotter import Plotter

class VehicleData:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data=self.preprocess_data()

    def preprocess_data(self):
        """
        Remove single-occurrence IDs from the data.
        """
        id_counts = {}
        filtered_data = []
        data = np.load(self.data_file)
        
        
        for row in data:
            _, obj_id, *_ = row
            id_counts[obj_id] = id_counts.get(obj_id, 0) + 1
            filtered_data.append(row)
        
        return [row for row in filtered_data if id_counts[row[1]] > 1]
    
        
    def segment(self):
        """
        Split the data into segments based on the 'id' column.
        Returns a dictionary where keys are IDs and values are lists of corresponding rows.
        """
        segments = {}
        for row in self.data:
            _, obj_id, *_ = row
            segments.setdefault(obj_id, []).append(row)
        return segments
    
    def filter(self, filter_function=None):
        """
        Filter the segments based on a given filter function.
        If no filter function is provided, return all segments.
        """
        if filter_function:
            return [segment for segment in self.segment().values() if filter_function(segment)]
        return list(self.segment().values())
    
    def plot(self, trajectories):
        """
        Plot trajectories using the Plotter class.
        """
        Plotter.save_plot(trajectories)
