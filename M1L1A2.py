# ---- Library Book Organiser ----

# STEP 1 - Create a dictionary
book = {
    "title": "Python Basics",
    "author": "Riya Sharma",
    "price": 450,
    "copies": 5
}
print("Book details:", book)

# STEP 2 - Access dictionary values
print("Book title:", book["title"])
print("Author:", book["author"])
print("Price:", book.get("price", "Not found"))
print("Copies:", book.get("copies", "Not found"))

# STEP 3 - Modify dictionary values
book["price"] = 500
book["copies"] = 6
print("\nAfter updating book details:", book)

# STEP 4 - Add a new item
book["publisher"] = "ABC Publications"
print("After adding publisher:", book)

# STEP 5 - Remove an item
book.pop("copies")
print("After removing copies:", book)

# STEP 6 - Access the updated dictionary
print("\nUpdated book details:", book)
print("Publisher:", book["publisher"])
print("Price:", book["price"])
