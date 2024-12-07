# dictionaries
#  dictionary is mutable, unordered, changeable, dynamic, key-value pair.
# are represented as {"keys":"values", "key1":"value2", ....}

# for example
dictionary = {
    "Fruit": "apple",
    "veg":"potato"
}
print(dictionary["Fruit"])
# output:  prints out the value assigned to key "Fruit" ---apple
# if the key is not present in the dictionary, it will throw an error
# to avoid this, we can use the get() method
print(dictionary.get("Fruit"))
# output: prints out the value assigned to key "Fruit" ---apple
# to add new item in dictionary
dictionary["Fruit"]="banana"
print(dictionary)
# output: prints out the updated dictionary ---{"Fruit": "banana", "veg":"potato"}
# to delete an item from dictionary
dictionary.pop("Fruit")
print(dictionary)
# output: prints out the updated dictionary ---{"veg":"potato"}
# loop thorugh a dictionary
for key, value in dictionary.items():
    print(f"{key}:{value}")
    # output: prints out the key-value pairs of the dictionary ---veg:potato


