def sum_of_intervals(intervals):
    intervals.sort()
    combined_intervals = []
    for chunk in intervals:
        if not combined_intervals or chunk[0] > combined_intervals[-1][1]:
            combined_intervals.append(chunk)
        else:
            combined_intervals[-1][1] = max(combined_intervals[-1][1], chunk[1])
    length_intervals= sum(end - start for start, end in combined_intervals)
    return length_intervals



print(sum_of_intervals([
    [0, 20],
    [-100000000, 10],
    [30, 40]
]))