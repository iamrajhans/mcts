import googlemaps
import random
from collections import defaultdict
from math import sqrt, log

# Initialize Google Maps API client
gmaps = googlemaps.Client(key="GOOGLE_MAPS_API_KEY")

# Node for the MCTS tree
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.remaining_destinations)

    def best_child(self, exploration_weight=1.4):
        return max(
            self.children,
            key=lambda child: (child.value / (child.visits + 1)) + exploration_weight * sqrt(log(self.visits + 1) / (child.visits + 1))
        )

# State representing the current state of delivery
class State:
    def __init__(self, current_location, remaining_destinations):
        self.current_location = current_location
        self.remaining_destinations = remaining_destinations

    def next_states(self):
        # Generate next possible states by visiting each remaining destination
        next_states = []
        for destination in self.remaining_destinations:
            new_remaining = list(self.remaining_destinations)
            new_remaining.remove(destination)
            next_states.append(State(destination, new_remaining))
        return next_states

# MCTS algorithm
class MCTS:
    def __init__(self, root_state):
        self.root = Node(root_state)

    def run(self, iterations=1000):
        for _ in range(iterations):
            node = self._select(self.root)
            if not node.state.remaining_destinations:  # Terminal state
                reward = self._simulate(node.state)
            else:
                node = self._expand(node)
                reward = self._simulate(node.state)
            self._backpropagate(node, reward)

    def _select(self, node):
        while node.children and node.is_fully_expanded():
            node = node.best_child()
        return node

    def _expand(self, node):
        next_states = node.state.next_states()
        for state in next_states:
            if not any(child.state == state for child in node.children):
                new_node = Node(state, node)
                node.children.append(new_node)
                return new_node
        return node

    def _simulate(self, state):
        total_distance = 0
        current_location = state.current_location
        for destination in state.remaining_destinations:
            total_distance += self._get_distance(current_location, destination)
            current_location = destination
        return -total_distance  # Negative because we want to minimize distance

    def _backpropagate(self, node, reward):
        while node:
            node.visits += 1
            node.value += reward
            node = node.parent

    def _get_distance(self, origin, destination):
        directions_result = gmaps.directions(origin, destination)
        distance = directions_result[0]["legs"][0]["distance"]["value"]  # in meters
        return distance / 1000  # Convert to kilometers

# Example usage
def main():
    origin = "Bangalore"  # Starting point
    destinations = ["Kempegowda International Airport Bengaluru", "Cubbon Park, Bangalore"]

    initial_state = State(origin, destinations)
    mcts = MCTS(initial_state)
    mcts.run(iterations=1000)

    # Find the best route
    best_route = []
    node = mcts.root
    while node.children:
        node = node.best_child(0)  # Exploration weight = 0 for greedy choice
        best_route.append(node.state.current_location)

    print("Optimal Route:", " -> ".join(best_route))

if __name__ == "__main__":
    main()
