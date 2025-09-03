# Python List Manipulation Project

This project demonstrates fundamental list manipulation techniques in Python. It covers creating, modifying, and querying lists.

## Project Description

The script performs the following operations on a list:

1.  **Initialization:** Creates an empty list.
2.  **Appending:** Adds elements to the end of the list.
3.  **Insertion:** Inserts an element at a specific position.
4.  **Extension:** Extends the list with elements from another list.
5.  **Removal:** Removes the last element of the list.
6.  **Sorting:** Sorts the list in ascending order.
7.  **Index Finding:** Finds the index of a specific value within the list.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.x installed on your system. 

### Installation

1.  Clone the repository (if applicable, if you have it on GitHub, GitLab, etc.):

    ```bash
    git clone <repository_url>
    ```

2.  Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3.  (Optional) Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

### Running the Script

To execute the Python script, use the following command:

### Code explanation

```bash
python my_list.py  # Replace "main.py" with the actual filename if different

# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

print(f"Final List: {my_list}") #print the final list
Key Methods Used:

append()
: Adds an element to the end of the list.
insert()
: Inserts an element at a given index.
extend()
: Appends elements from another iterable (like another list).
pop()
: Removes and returns the last element (or the element at a specific index if provided).
sort()
: Sorts the list in place.
index()
: Returns the index of the first occurrence of a value.

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.