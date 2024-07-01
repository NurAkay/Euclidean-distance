# Defining the Points
points = [(1, 2), (4, 6), (5, 9), (8, 8)]  # Example points, you can add your own

# Writing a Function for Euclidean Distance
def euclideanDistance(point1, point2):
    x_difference = point2[0] - point1[0]
    y_difference = point2[1] - point1[1]
    return (x_difference * x_difference + y_difference * y_difference) ** 0.5

# Calculating the Distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Finding the Minimum Distance
min_distance = min(distances)

# Printing the Results
print("Distances:", distances)
print("Minimum Distance:", min_distance)


