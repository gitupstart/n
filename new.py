from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["exampleDatabase"]
collection = db["exampleCollection"]



# Step 3: Create (Insert Data)
# Insert one document
collection.insert_one({"name": "Alice", "age": 25, "city": "New York", "hobbies": ["reading", "traveling"]})

# Insert multiple documents
documents = [
    {"name": "Bob", "age": 30, "city": "Los Angeles", "hobbies": ["sports", "movies"]},
    {"name": "Charlie", "age": 35, "city": "Chicago", "hobbies": ["gaming", "coding"]},
    {"name": "David", "age": 28, "city": "New York", "hobbies": ["music", "traveling"]},
    {"name": "Eve", "age": 22, "city": "Los Angeles", "hobbies": ["fashion", "fitness"]}
]
collection.insert_many(documents)

# Step 4: Read (Retrieve Data)
print("\nAll Documents:")
for doc in collection.find():
    print(doc)

# Query with a filter
print("\nDocuments where city is 'New York':")
for doc in collection.find({"city": "New York"}):
    print(doc)

# Retrieve a single document
print("\nSingle Document (Name: Alice):")
doc = collection.find_one({"name": "Alice"})
print(doc)

# Project specific fields (Exclude `_id`)
print("\nProjecting only 'name' and 'city' fields:")
for doc in collection.find({}, {"name": 1, "city": 1, "_id": 0}):
    print(doc)

# Step 5: Count Documents
count = collection.count_documents({"city": "New York"})
print(f"\nNumber of people in 'New York': {count}")

# Step 6: Update (Modify Data)
# Update one document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
print("\nAfter updating Alice's age:")
print(collection.find_one({"name": "Alice"}))

# Update multiple documents
collection.update_many({"city": "Los Angeles"}, {"$set": {"state": "California"}})
print("\nAfter updating city 'Los Angeles' with state 'California':")
for doc in collection.find({"city": "Los Angeles"}):
    print(doc)

# Step 7: Sort Results
print("\nAll Documents Sorted by Age (Descending):")
for doc in collection.find().sort("age", -1):  # -1 for descending, 1 for ascending
    print(doc)

# Step 8: Limit Results
print("\nLimit to 2 Documents:")
for doc in collection.find().limit(2):
    print(doc)

# Step 9: Delete (Remove Data)
# Delete one document
collection.delete_one({"name": "Eve"})
print("\nAfter Deleting Eve:")
for doc in collection.find():
    print(doc)

# Delete multiple documents
collection.delete_many({"city": "New York"})
print("\nAfter Deleting All Documents from 'New York':")
for doc in collection.find():
    print(doc)

# Count after deletion
remaining_count = collection.count_documents({})
print(f"\nRemaining Documents Count: {remaining_count}")

# Step 10: Aggregate (Optional Advanced Operation)
# Example: Group by city and count people
print("\nAggregate: Count People in Each City:")
pipeline = [
    {"$group": {"_id": "$city", "total_people": {"$sum": 1}}}
]
for result in collection.aggregate(pipeline):
    print(result)
