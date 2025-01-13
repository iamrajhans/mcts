```markdown
# Logistics Route Optimization with Monte Carlo Tree Search

This project demonstrates how to optimize a delivery route using the **Monte Carlo Tree Search (MCTS)** algorithm, integrated with the **Google Maps API** for real-world distance calculations. The goal is to minimize delivery costs and time by finding the most efficient route.

---

## Features

- Utilizes **Monte Carlo Tree Search** for route optimization.
- Integrates **Google Maps API** for accurate distance and route calculations.
- Scalable to multiple destinations.
- Provides an optimal delivery route based on simulations and backpropagation.

---

## Prerequisites

### 1. Python Installation
Ensure you have Python 3.7 or higher installed. You can download it from [python.org](https://www.python.org/).

### 2. Required Libraries
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Google Maps API Key
- Obtain a Google Maps API key from the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Directions API** for your project.
- Replace the placeholder `YOUR_GOOGLE_MAPS_API_KEY` in the code with your actual API key.

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/iamrajhans/mcts.git
cd mcts
```

### 2. Configure the API Key
Open the script file and update the following line with your Google Maps API key:
```python
gmaps = googlemaps.Client(key="GOOGLE_MAPS_API_KEY")
```

### 3. Run the Script
Execute the Python script:
```bash
python mcts.py
```

---

## Example

### Input:
- Starting Location: **Bangalore**
- Delivery Destinations:
  - Kempegowda International Airport Bengaluru,
  - Cubbon Park, Bangalore

### Output:
```
Optimal Route: Kempegowda International Airport Bengaluru -> Cubbon Park, Bangalore
```

---

## Project Structure

```
logistics-route-optimization/
├── mcts.py                # Main Python script for MCTS and route optimization
├── README.md              # Documentation file
└── requirements.txt       # List of required Python libraries
```

---

## Concepts Used

### 1. Monte Carlo Tree Search (MCTS)
MCTS is a heuristic search algorithm that balances exploration and exploitation to optimize decision-making. It iteratively builds a decision tree by simulating possible outcomes and refining the tree.

### 2. Google Maps API
The Google Maps API is used to calculate distances between locations, providing real-world accuracy for route optimization.

---

## Limitations

- **API Quota**: The script is limited by the free tier quota of the Google Maps API.
- **Scalability**: Computational complexity increases with the number of destinations.

---

## Future Improvements

- Include **live traffic data** for real-time optimization.
- Allow dynamic updates (e.g., new destinations during route execution).
- Visualize the optimal route on a map.

---
