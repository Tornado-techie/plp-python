# Assignment 1: Design Your Own Class & Polymorphism Challenge

This project fulfills the requirements for Assignment 1: Design Your Own Class, focusing on object-oriented programming principles, specifically class design, inheritance, constructors, and polymorphism.

## Project Structure

The project consists of two main activities:

*   **Activity 1: Design Your Own Class** -  Implementation of a custom class with attributes, methods, constructors, and potential inheritance.
*   **Activity 2: Polymorphism Challenge** -  Demonstration of polymorphism through a common action implemented differently across various classes.

## Activity 1: Design Your Own Class

### Goal

To design and implement a custom class representing a real-world object, concept, or entity of your choice.  The class should include:

*   **Attributes:**  Data members that describe the properties of the object.
*   **Methods:**  Functions that define the object's behavior.
*   **Constructors:**  Special methods used to initialize new objects with specific values.
*   **Inheritance (Optional but Encouraged):**  Extend the base class with a derived class, exploring inheritance and related concepts like method overriding.

### Implementation Details

This implementation defines a class called `Smartphone`.

*   **Class:** `Smartphone`
*   **Attributes:**
    *   `brand` (string): The brand of the smartphone.
    *   `model` (string): The model name of the smartphone.
    *   `storage_capacity` (int): The storage capacity in GB.
    *   `camera_resolution` (float): The camera resolution in megapixels.
    *   `is_on` (bool):  Indicates whether the smartphone is currently on.
*   **Methods:**
    *   `__init__(self, brand, model, storage_capacity, camera_resolution)`:  The constructor, initializing the smartphone with the given values.  It sets `is_on` to `False` by default.
    *   `turn_on(self)`: Turns the smartphone on (sets `is_on` to `True`).
    *   `turn_off(self)`: Turns the smartphone off (sets `is_on` to `False`).
    *   `take_photo(self)`: Simulates taking a photo, printing a message if the phone is on.
    *   `get_info(self)`: Returns a string containing the smartphone's information.
*   **Example Usage:**
    ```python
    my_phone = Smartphone("Samsung", "Galaxy S23", 256, 50.0)
    print(my_phone.get_info())  # Prints Smartphone information
    my_phone.turn_on()
    my_phone.take_photo()      # Simulates taking a photo
    ```

## Activity 2: Polymorphism Challenge

### Goal

To demonstrate polymorphism by creating a program that includes different classes with a common method (`move()`) that behaves differently for each class.

### Implementation Details

This implementation uses `Animal` as a base class and defines subclasses `Dog`, `Cat`, and `Bird`.

*   **Base Class:** `Animal`
    *   `move()`:  A generic `move()` method that prints a default message.
*   **Subclasses:**
    *   `Dog`
        *   Overrides `move()` to print "Running"
    *   `Cat`
        *   Overrides `move()` to print "Prowling"
    *   `Bird`
        *   Overrides `move()` to print "Flying"
*   **Example Usage:**
    ```python
    animals = [Dog(), Cat(), Bird()]
    for animal in animals:
        animal.move()  # Prints "Running", "Prowling", "Flying" respectively
    ```

## Running the Code

1.  Ensure you have Python 3 installed.
2.  Save the code from each activity into separate `.py` files (e.g., `smartphone.py` and `animals.py`).
3.  Run each file from the command line:

    ```bash
    python smartphone.py
    python animals.py
    ```

## Dependencies

This project requires no external dependencies.  It uses only standard Python libraries.

## Future Enhancements

*   **Activity 1:** Add more sophisticated methods to the `Smartphone` class, such as methods to install apps, play music, or connect to Wi-Fi. Implement error handling for invalid inputs. Explore more advanced inheritance scenarios.
*   **Activity 2:** Expand the number of animal classes and their unique `move()` implementations. Implement more complex behaviors beyond simple printing.  Consider using abstract base classes for a more robust design.

## Author

[Salome Mundia]