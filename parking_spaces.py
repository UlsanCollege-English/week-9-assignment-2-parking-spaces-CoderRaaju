import heapq

def min_parking_spots(intervals):
    """
    Given a list of (start, end) times, return the minimum number of
    parking spots required so that no car has to wait.

    Rule:
    - If one car leaves at time t and another arrives at t, they can share a spot.
    """

    # Edge case: no intervals
    if not intervals:
        return 0

    # Step 1: sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: min-heap to track current car end times
    heap = []

    # Step 3: iterate over all intervals
    max_spots = 0
    for start, end in intervals:
        # Free up spots for cars that already left
        while heap and heap[0] <= start:
            heapq.heappop(heap)

        # Assign a spot for current car
        heapq.heappush(heap, end)

        # Update maximum concurrent cars
        max_spots = max(max_spots, len(heap))

    return max_spots
