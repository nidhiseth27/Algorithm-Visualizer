import random
import inspect
from .sorting import SortingAlgorithms
from .pathfinding import PathfindingAlgorithms


class AlgorithmManager:
    def __init__(self):
        self.data = [random.randint(1, 100) for num in range(50)]
        self.highlight_indices = (-1, -1)
        self.status_message = ""
        self.sorting_algos, self.pathfinding_algos = self.get_algo_names()
        print(self.sorting_algos)
        print(self.pathfinding_algos)

    def get_algo_names(self):
        sorting_names = dict()
        pathfinding_names = dict()
        for name, member in inspect.getmembers(SortingAlgorithms()):
            if inspect.isfunction(member) or inspect.ismethod(member):
                if member.__doc__ is not None:
                    sorting_names.update({member.__doc__: member})
        for name, member in inspect.getmembers(PathfindingAlgorithms()):
            if inspect.isfunction(member) or inspect.ismethod(member):
                if member.__doc__ is not None:
                    pathfinding_names.update({member.__doc__: member})
        return sorting_names, pathfinding_names

    def reset_data(self):
        """Generates a new random dataset."""
        self.data = [random.randint(1, 100) for num in range(50)]

    def get_generator(self, algorithm):
        """Return a generator for the selected algorithm."""
        if algorithm in self.sorting_algos:
            self.status_message = f"{algorithm}ing..."
            params = inspect.signature(self.sorting_algos[algorithm]).parameters
            if len(params) > 1:
                return self.sorting_algos[algorithm](0, len(self.data) - 1, self.data)
            else:
                return self.sorting_algos[algorithm](self.data)

        if algorithm in self.pathfinding_algos:
            pass
