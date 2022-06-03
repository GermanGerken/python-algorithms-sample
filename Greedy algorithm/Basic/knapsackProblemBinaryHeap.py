import heapq  # implementation of the heap queue algorithm standard library modul


def heap_knapsack(capacity, items):
    order = [(-v / w, w) for v, w in items]  # get list of value of weight and weight pairs
    # note that we add - sign to invert heap
    heapq.heapify(order)  # make binary heap out of order

    acc = 0  # our accumulated value
    while order and capacity:
        v_per_w, w = heapq.heappop(order)  # getting elements from heap
        can_take = min(w, capacity)  # show how much space left in knapsack
        acc -= v_per_w * w
        capacity -= can_take
    return acc


print(heap_knapsack(50, [[60, 20], [100, 50], [120, 30]]))
