#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    visited = set()  # Set to keep track of visited boxes

    # Define a recursive helper function to perform DFS traversal
    def dfs(box_index):
        visited.add(box_index)  # Mark the current box as visited

        # Iterate through the keys in the current box
        for key in boxes[box_index]:
            # If the key opens a box that we haven't visited yet, recursively visit that box
            if key not in visited and key < n:
                dfs(key)

    dfs(0)  # Start the DFS traversal from the first box (boxes[0])

    return len(visited) == n

