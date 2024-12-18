# Indefinite Path Finder

## Overview
This code checks if there is an **indefinite path** in a directed graph where every edge meets or exceeds a specified minimum weight. If such a path exists, it returns a list of node labels forming a cycle. Otherwise, it returns `None`.

## Key Functions

### `find_indefinite_path(G, start_node, min_weight)`
Finds an indefinite path in the graph.

#### Parameters:
- **`G`**: Directed graph object.
- **`start_node`**: Starting node for the path.
- **`min_weight`**: Minimum weight required for edges in the path.

#### Steps:
1. Removes edges with weights below `min_weight`.
2. Checks for a cycle starting from `start_node`.
3. If a cycle is found, returns the path. Otherwise, returns `None`.

### `findInital(start_node, end1, end2)`
An incomplete helper function that prints edges in the graph.

#### Parameters:
- **`start_node`**: Starting node.
- **`end1`, `end2`**: Unused parameters.

#### Returns:
- Currently `None`.

## Graph Input
- The graph data is loaded from a file in JSON format.
- Example JSON:
  ```json
  {
    "nodes": ["a", "b", "c"],
    "edges": [
      {"source": "a", "target": "b", "weight": 100},
      {"source": "b", "target": "c", "weight": 80},
      {"source": "c", "target": "a", "weight": 50}
    ]
  }
  ```

## Example Usage
1. Load the graph:
   ```python
   G = DG.DGraph()
   with open('roads.txt', 'r') as f:
       G.loadJSON(f.read())
   ```

2. Find an indefinite path:
   ```python
   print(find_indefinite_path(G, 'a', 50))
   ```
