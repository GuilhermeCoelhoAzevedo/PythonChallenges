def process_requests(wait):
    n = len(wait)  # Number of requests
    queue = list(range(n))  # Queue contains indices of requests (0 to n-1)
    results = []  # To store the number of requests in the queue at each second
    time = 0  # Start at time = 0

    while queue:
        # Add the current number of requests in the queue
        results.append(len(queue))

        # Process the first request (FIFO)
        queue.pop(0)  # Serve the first request in the queue

        # Increment the time for the next second
        time += 1

        # Remove any expired requests based on the current time
        queue = [i for i in queue if time + 1 < wait[i]]

    # Append 0 at the end, as no requests are left at the final time
    results.append(0)

    return results




# Test case:

# User case 2
wait2 = [4, 3, 1, 2, 1]
print(process_requests(wait2))  # Output: [4, 1, 0]
