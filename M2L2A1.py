# ---- Movie Explorer ----

# STEP 1 - Create tuples for movie details (fixed — cannot be changed)
movie1 = ("The Lion King", "Animation", 118, "Easy")
movie2 = ("Interstellar", "Sci-Fi", 169, "Hard")
print("Movie 1:", movie1)
print("Name:", movie1[0])
print("Genre:", movie1[1])
print("Difficulty:", movie1[-1])

# STEP 2 - Nested tuples and slicing
all_movies = (movie1, movie2)
print("\nFirst movie name:", all_movies[0][0])
print("Second movie time:", all_movies[1][2], "mins")
print("Movie 1 details (sliced):", movie1[1:3])

# STEP 3 - Iterate through a tuple
print("\nMovie 1 details:")
for detail in movie1:
    print(" -", detail)

# STEP 4 - Create sets for movie features (no duplicates allowed)
movie1_features = {"Animation", "Family", "Adventure", "Music", "Adventure"}
movie2_features = {"Science", "Space", "Adventure", "Drama", "Music", "Future"}
print("\nMovie 1 features:", movie1_features)
print("Movie 2 features:", movie2_features)
print("Total movie 1 features:", len(movie1_features))

# STEP 5 - Modify the set
movie1_features.add("Comedy")
movie1_features.discard("Music")
print("\nUpdated movie 1 features:", movie1_features)

# STEP 6 - Set operations
all_features = movie1_features.union(movie2_features)
common = movie1_features.intersection(movie2_features)
only_movie1 = movie1_features.difference(movie2_features)
unique_to_each = movie1_features.symmetric_difference(movie2_features)

print("\nAll features (union):", all_features)
print("Common features (intersection):", common)
print("Only in Movie 1 (difference):", only_movie1)
print("Not shared (sym. difference):", unique_to_each)
