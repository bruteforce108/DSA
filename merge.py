def merge_sort_orders(orders):
    if len(orders) <= 1: return orders
    
    mid = len(orders) // 2
    L = merge_sort_orders(orders[:mid])
    R = merge_sort_orders(orders[mid:])
    
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i]['time'] < R[j]['time']:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
            
    # Append any remaining elements
    return res + L[i:] + R[j:]

# Example usage:
orders = [{"id": "Ord1", "time": 45}, {"id": "Ord2", "time": 15}, {"id": "Ord3", "time": 30}]
print("Sorted Orders:", merge_s ort_orders(orders))
