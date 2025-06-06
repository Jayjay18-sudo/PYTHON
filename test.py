# Python Operators
"""
    Python divides the operators in the following groups:

    Arithmetic operators - Arithmetic operators are used with numeric values to perform common mathematical operations
    Assignment operators - Assignment operators are used to assign values to variables
    Comparison operators - Comparison operators are used to compare two values
    Logical operators - Logical operators are used to combine conditional statements
    Identity operators - Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
    Membership operators - Membership operators are used to test if a sequence is presented in an object
    Bitwise operators - Bitwise operators are used to compare (binary) numbers

    Operator Precedence - Operator precedence describes the order in which operations are performed

    1. Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
    2. Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions
    3. If two operators have the same precedence, the expression is evaluated from left to right
"""

# Python Lists
"""
    Lists are used to store multiple items in a single variable.
    Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    Lists are created using square brackets


    List Items
        List items are ordered, changeable, and allow duplicate values.
        List items are indexed, the first item has index [0], the second item has index [1] etc

    Ordered
        When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
        If you add new items to a list, the new items will be placed at the end of the list.

    Changeable
        The list is changeable, meaning that we can change, add, and remove items in a list after it has been created

    List Length
        To determine how many items a list has, use the len() function

    List Items - Data Types
        String, int and boolean data types
        A list with strings, integers and boolean values

    type()
        From Python's perspective, lists are defined as objects with the data type 'list':

    The list() Constructor
        It is also possible to use the list() constructor when creating a new list.

    Python Collections (Arrays)
        There are four collection data types in the Python programming language:
            List is a collection which is ordered and changeable. Allows duplicate members.
            Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
            Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
            Dictionary is a collection which is ordered** and changeable. No duplicate members.

    Python - Access List Items
        Access Items
            List items are indexed and you can access them by referring to the index number

        Negative Indexing
            Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.

        Range of Indexes
            You can specify a range of indexes by specifying where to start and where to end the range.
            When specifying a range, the return value will be a new list with the specified items.
            By leaving out the start value, the range will start at the first item:

    Python - Change List Items
        Change Item Value
            To change the value of a specific item, refer to the index number

        Change a Range of Item Values
            To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

        Insert Items
            To insert a new list item, without replacing any of the existing values, we can use the insert() method.
            The insert() method inserts an item at the specified index

    Python - Add List Items
        Append Items
            To add an item to the end of the list, use the append() method

        Insert Items
            To insert a list item at a specified index, use the insert() method.
            The insert() method inserts an item at the specified index

        Extend List
            To append elements from another list to the current list, use the extend() method

        Add Any Iterable
            The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

        Python - Remove List Items
            Remove Specified Item
                The remove() method removes the specified item

            Remove Specified Index
                The pop() method removes the specified index
                The del keyword also removes the specified index
                The del keyword can also delete the list completely

            Clear the List
                The clear() method empties the list.
                The list still remains, but it has no content

    Python - Loop Lists
        Loop Through a List
            You can loop through the list items by using a for loop

        Loop Through the Index Numbers
            You can also loop through the list items by referring to their index number.
            Use the range() and len() functions to create a suitable iterable

        Using a While Loop
            You can loop through the list items by using a while loop.
            Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
            Remember to increase the index by 1 after each iteration

        Looping Using List Comprehension
            List Comprehension offers the shortest syntax for looping through lists

    Python - List Comprehension
        List Comprehension
            List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
                Example:
                Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
                Without list comprehension you will have to write a for statement with a conditional test inside

    Python - Sort Lists

        Sort List Alphanumerically
            List objects have a sort() method that will sort the list alphanumerically, ascending, by default

        Sort Descending
            To sort descending, use the keyword argument reverse = True
        
        Customize Sort Function
            You can also customize your own function by using the keyword argument key = function
            The function will return a number that will be used to sort the list (the lowest number first)

        Case Insensitive Sort
            By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

        Reverse Order  
            What if you want to reverse the order of a list, regardless of the alphabet?
            The reverse() method reverses the current sorting order of the elements
            
    Python - Copy Lists
        Copy a List
            You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
        
        Use the copy() method    
            You can use the built-in List method copy() to copy a list

        Use the list() method
            Another way to make a copy is to use the built-in method list()

        Use the slice Operator
            You can also make a copy of a list by using the : (slice) operator

    Python - Join Lists
        Join Two Lists
            There are several ways to join, or concatenate, two or more lists in Python.
            One of the easiest ways are by using the + operator.

    Python - List Methods
        Python has a set of built-in methods that you can use on lists.
            append()	Adds an element at the end of the list
            clear()	Removes all the elements from the list
            copy()	Returns a copy of the list
            count()	Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()	Removes the element at the specified position
            remove()	Removes the item with the specified value
            reverse()	Reverses the order of the list
            sort()	Sorts the list
"""
# Python Tuples
"""
    Tuple
        Tuples are used to store multiple items in a single variable.
        Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
        A tuple is a collection which is ordered and unchangeable.
        Tuples are written with round brackets

    Tuple Items
        Tuple items are ordered, unchangeable, and allow duplicate values.
        Tuple items are indexed, the first item has index [0], the second item has index [1] etc

    Ordered
         When we say that tuples are ordered, it means that the items have a defined order, and that order will not change

    Unchangeable
        Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created
        
    Allow Duplicates
        Since tuples are indexed, they can have items with the same value
        
    Tuple Length
        To determine how many items a tuple has, use the len() function

    Create Tuple With One Item
        To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
    
    Tuple Items - Data Types
        Tuple items can be of any data type -> String, int and boolean data types
            
    Python Collections (Arrays)
        There are four collection data types in the Python programming language
            List is a collection which is ordered and changeable. Allows duplicate members.
            Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
            Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
            Dictionary is a collection which is ordered** and changeable. No duplicate members.

    Python - Access Tuple Items
        Access Tuple Items
            You can access tuple items by referring to the index number, inside square brackets

        Negative Indexing
            Negative indexing means start from the end.
            -1 refers to the last item, -2 refers to the second last item etc

        Range of Indexes
            You can specify a range of indexes by specifying where to start and where to end the range.
            When specifying a range, the return value will be a new tuple with the specified items

    Python - Update Tuples
        Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
        But there are some workarounds

        Change Tuple Values
            Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
            But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple    

            
            
            
            
"""
