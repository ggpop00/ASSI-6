def ds(roll_no, name):
    # Create and add parameters to data structures
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {"roll_no": roll_no, "name": name}

    # Change values during runtime
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")

    my_list[0] = new_roll_no
    my_list[1] = new_name

    # Tuples are immutable, so we need to create a new tuple
    my_tuple = (new_roll_no, new_name)

    my_set.remove(roll_no)
    my_set.add(new_roll_no)
    my_set.remove(name)
    my_set.add(new_name)

    my_dict["roll_no"] = new_roll_no
    my_dict["name"] = new_name

    # Delete data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    # Printing the deleted data structures will raise NameError

# Test the function
ds("123", "John")


