def length_filter(trajectory, threshold=10):
    """
    Filter function that checks if the length of the trajectory is greater than a threshold.
    
    :param trajectory: List of rows representing a trajectory
    :param threshold: Minimum length threshold
    :return: True if the length of the trajectory is greater than the threshold, False otherwise

    """
    return len(trajectory) > threshold
