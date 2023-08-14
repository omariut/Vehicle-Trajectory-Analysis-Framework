# AMAG - Interview assignment
Firstly, thank you for applying and taking the time, we really appreciate it. The following is
our attempt to try to get a good overview of how you tackle python programming and problem solving.
No test like this is ever a true measurement of your capabilities or quality but it is one of the
few things we can do to ensure that your capabilities match the requirements for the tasks that
our developers deal with every day.
With that in mind we wish you the best of luck and look forwards to seeing your solution.

## Problem Statement
One of the core systems of AMAG has to do with evaluating vector data that is directly taken
from videos showing vehicles driving over a scene (e.g intersection). This vector data is
a set of trajectories on a latitudinal/longitudinal plain. In this project we give you some
of that data and ask of you to start implementing a object oriented framework to analyze
and visualize the data. The main objectives of the framework are defined in "Object Functional
Requirements" below.

 
### About the data
The datafile (data.npy) is a numpy output of a matrix having the following columns

- index
- id
- x
- y

Each row in the matrix represents a point in time where a image from a video was processed to
generate the underlying data.

Column 0, the `index` is a index value counting from 1...n (where n is the number of rows in the matrix).
Column 1, the 'id' gives a unique id for the object travelling through the scene. The id's are not
  ordered and it's a part of the framework to build in the ability to get all the samples associated
  with an id number. Remember that the matrix is time sorted so the index numbers should always be
  strictly increasing as you move down a row.
Column 2, the `x` gives the latitudinal values of the trajectory
Column 3, the `y` gives the longitudinal values of the trajectory


Pitfalls:
Here is a common pitfall, there is a possibility to have a single id come up only once. This would
mean that in a single videoframe something was picked up as a car and registered. However, this
would need to be filtered out, which is part of the framework you need to build.


### Object Functional Requirements
We need the ability to do the following

- Segment: Split the data into segments based on the `id` column (see Data Review)
- Filter: Filter the data based on arbitrary functionality
- Plot: Plot a set of trajectories by passing them into

#### Object Functionality Example
We assume the object can be created somehow using a function like:
```
from framework import VehicleData

obj = VehicleData('./data.npy')
```
And in the following examples we will use this object.

##### Segment:
Ability to select a subset from the data using a specific id
```
single_id = obj.by_id(id)
```

##### Filter:
Ability to filter based on input functions. The input functions should use each segment as their
input i.e. the filter mechanism is for a single trajectory not a single point.
```
def length(trajectory):
  return len(trajectory)

list_of_lats_lngs = obj.filter(length)
```

##### Plot:
Ability to plot segments. The plot also needs to have the ability to plot only filtered
segments.
```
list_of_lats_lngs = obj.filter()
# Plots and shows only the list of segments we filtered
obj.plot(list_of_lats_lngs)
```


## Review Criteria
The following will be used to evaluate the code

- Correctness - Solves the fundamental capabilities as expected
- Extendability - Ability to extend the framework such that we can add new functionality to it
- Modifiability - Ability to change how certain functions work internally without
- Structure - Is the code soundly structured into files and folders so that any reasonable developer can understand it
- Documentation - Is the implementation documented, and if so how
- Testability - Is the codebase tested. If not, how easy is it to add unit-tests to the code base
