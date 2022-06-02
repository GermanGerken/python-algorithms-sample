def sorted_knapsack(capacity, items):
    order = [(v / w, w) for v, w in items]  # get list of value of weight and weight pairs
    order.sort(reverse=True)  # sorting the list

    acc = 0  # our accumulated value
    for v_per_w, w in order:
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        else:
            acc += v_per_w * capacity
            break
    return acc


print(sorted_knapsack(50, [[60, 20], [100, 50], [120, 30]]))
