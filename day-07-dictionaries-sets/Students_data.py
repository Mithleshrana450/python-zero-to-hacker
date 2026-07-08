students = {
    "Alice": [80, 90, 85],
    "Bob": [70, 75, 80],
    "Charlie": [95, 90, 100]
}

average = {}

for name in students:
    avg = sum(students[name]) / len(students[name])
    average[name] = avg
    print(name, "Average:", avg)

topper = max(average, key=average.get)
lowest = min(average, key=average.get)

print("Topper:", topper)
print("Lowest Scorer:", lowest)

print("\nLeaderboard:")
leaderboard = sorted(average.items(), key=lambda x: x[1], reverse=True)

for name, avg in leaderboard:
    print(name, ":", avg)