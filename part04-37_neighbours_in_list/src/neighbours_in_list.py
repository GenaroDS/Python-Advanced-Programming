def longest_series_of_neighbours(numbers):
    longest_series = 0
    current_series = 1

    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) == 1:
            current_series += 1
        else:
            longest_series = max(longest_series, current_series)
            current_series = 1

    return max(longest_series, current_series)

