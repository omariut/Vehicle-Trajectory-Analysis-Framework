# Vehicle Trajectory Analysis Framework

## Overview

The Vehicle Trajectory Analysis Framework is an object-oriented Python framework designed to analyze and visualize trajectory data extracted from videos showing vehicles driving over a scene, such as an intersection. This framework allows users to segment, filter, and plot trajectories based on various criteria.

## Features

### Segment

The framework provides the ability to split the trajectory data into segments based on the unique `id` assigned to each object traveling through the scene.

### Filter

Users can define filter functions that take a trajectory segment as input and return `True` or `False` based on specific criteria. Filtered segments can then be used for further analysis or visualization.

### Plot

The framework supports plotting trajectories using popular data visualization libraries like Matplotlib. Users can pass a list of trajectory segments to the `plot` function to visualize the trajectories on a latitudinal/longitudinal plane.

## Usage

To use the Vehicle Trajectory Analysis Framework, follow these steps:

1. Import the `VehicleData` class from the framework.
2. Create an instance of the `VehicleData` class by providing the path to the trajectory data file (e.g., `data.npy`).

```python
from framework.vehicle_data import VehicleData

obj = VehicleData('./data.npy')
```

To see a sample execution,  run:
```python
pip install -r requirements.txt
python main.py

```
