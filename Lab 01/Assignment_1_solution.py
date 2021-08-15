from typing import List, Dict, Set, Tuple
from doctest import testmod
from random import randint, seed
from functools import reduce


# -----------------------------------------------
# ----------------Question No. 01----------------
# -----------------------------------------------
def get_characters(s: str) -> List[str]:
    """Breaks a string into a list of characters.

    doctests:
    >>> get_characters("abc")
    ['a', 'b', 'c']
    >>> get_characters("IIITG")
    ['I', 'I', 'I', 'T', 'G']
    """

    return list(s)


# -----------------------------------------------
# ----------------Question No. 02----------------
# -----------------------------------------------
def get_string(s: List[str]) -> str:
    """Merges a list of characters into a string.

    doctests:
    >>> get_string(['a', 'b', 'c'])
    'abc'
    >>> get_string(['I', 'I', 'I', 'T', 'G'])
    'IIITG'
    """

    return "".join(s)


# -----------------------------------------------
# ----------------Question No. 03----------------
# -----------------------------------------------
def get_random(n: int) -> List[int]:
    """Generates a list of n random integer numbers.

    doctests:
    >>> get_random(5)
    [4, 2, 1, 2, 2]
    >>> get_random(3)
    [2, 1, 1]
    """

    x = []

    for i in range(n):
        seed(i)
        x.append(randint(1, n))

    return x


# -----------------------------------------------
# ----------------Question No. 04----------------
# -----------------------------------------------
def sort_descending(x: List[int]) -> List[int]:
    """Generates a list of n random numbers.

    doctests:
    >>> sort_descending([5, 2, 3, 1, 4])
    [5, 4, 3, 2, 1]
    >>> sort_descending([2, 3, 1])
    [3, 2, 1]
    """

    x.sort(reverse=True)
    return x


# -----------------------------------------------
# ----------------Question No. 05----------------
# -----------------------------------------------
def frequency_count(li: List[int]) -> Dict[int, int]:
    """Counts frequency of each numbers in a list of numbers.

    doctests:
    >>> frequency_count([1, 2, 3, 1, 2, 3, 5, 4, 7, 7])
    {1: 2, 2: 2, 3: 2, 5: 1, 4: 1, 7: 2}
    >>> frequency_count([2, 2, 2, 3, 1])
    {2: 3, 3: 1, 1: 1}
    """

    x = {}

    for i in li:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1

    return x


# -----------------------------------------------
# ----------------Question No. 06----------------
# -----------------------------------------------
def get_elements(li: List[int]) -> Set:
    """Extracts all the unique elements from a list of numbers.

    doctests:
    >>> get_elements([1, 2, 3, 1, 2, 3, 5, 4, 7, 7])
    {1, 2, 3, 4, 5, 7}
    >>> get_elements([2, 2, 2, 3, 1])
    {1, 2, 3}
    """

    x = set()

    for i in li:
        if i in x:
            pass
        else:
            x.add(i)

    return x


# -----------------------------------------------
# ----------------Question No. 07----------------
# -----------------------------------------------
def repeat(li: List[int]) -> int:
    """Returns first repeating element from a list of numbers.

    doctests:
    >>> repeat([1, 2, 3, 1, 2, 3, 5, 4, 7, 7])
    1
    >>> repeat([2, 2, 2, 3, 1])
    2
    """

    x = set()

    for i in li:
        if i in x:
            return i
        else:
            x.add(i)

    return x


# -----------------------------------------------
# ----------------Question No. 08----------------
# -----------------------------------------------
def create_dict(n: int) -> Dict[int, List[int]]:
    """Returns Dictionary with numbers from 0 to n as keys
       which are mapped to lists containing squares and
       cubes of the respective keys.

    doctests:
    >>> create_dict(1)
    {0: [0, 0], 1: [1, 1]}
    >>> create_dict(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    """

    x = {}

    for i in range(0, n + 1):
        x[i] = [i * i, i * i * i]

    return x


# -----------------------------------------------
# ----------------Question No. 09----------------
# -----------------------------------------------
def tuple_zip(list1: List, list2: List) -> List[Tuple]:
    """Creates tuples of elements having same indices from two lists.

    doctests:
    >>> tuple_zip([1, 2], ['x', 'y'])
    [(1, 'x'), (2, 'y')]
    >>> tuple_zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    """

    x = list(zip(list1, list2))

    return x


# -----------------------------------------------
# ----------------Question No. 10----------------
# -----------------------------------------------
def list_squares(n: int) -> List[int]:
    """Generates a list of squares of numbers from 0 to n using list comprehension.

    doctests:
    >>> list_squares(2)
    [0, 1, 4]
    >>> list_squares(5)
    [0, 1, 4, 9, 16, 25]
    """

    x = [i ** 2 for i in range(0, n + 1)]

    return x


# -----------------------------------------------
# ----------------Question No. 11----------------
# -----------------------------------------------
def dict_squares(n: int) -> Dict[int, int]:
    """Generates a dictionary with numbers from 0 to n as keys
       which are mapped to their squares using dictionary comprehension.

    doctests:
    >>> dict_squares(2)
    {0: 0, 1: 1, 2: 4}
    >>> dict_squares(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """

    x = {i: i ** 2 for i in range(0, n + 1)}

    return x


# -----------------------------------------------
# ----------------Question No. 12----------------
# -----------------------------------------------
class Class_name:
    """
    Class with mentioned properties.

    doctests:
    >>> Class_name(['s', 'w', 'a', 'r', 'a', 'j']).apply(square)
    Exception: TypeError has occurred, Try Again
    >>> Class_name(['p', 'a', 'r', 't', 'h']).apply(lambda x:x**2)
    Exception: TypeError has occurred, Try Again
    >>> Class_name([5, 10, 15, 20]).apply(lambda x:x**2)
    [25, 100, 225, 400]
    >>> Class_name([3, 20, 15, 9, 13]).apply(lambda x:x**2)
    [9, 400, 225, 81, 169]
    """

    def __init__(self, li: List) -> List:
        self.li = li

    def apply(self, function_argument) -> List:
        # Class_name.apply method takes another function as argument
        try:
            return [function_argument(var) for var in self.li]
        except TypeError:
            print("Exception: TypeError has occurred, Try Again")


def square(x: List) -> List:
    """
    The apply method written above will use this function as an argument.
    """

    return x ** 2


# -----------------------------------------------
# ----------------Question No. 13----------------
# -----------------------------------------------
def uppercase_word(li: List[str]) -> List[str]:
    """Upper-cases each word in a list of words.

    doctests:
    >>> uppercase_word(['aa', 'bb'])
    ['AA', 'BB']
    >>> uppercase_word(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    """

    x = list(map(lambda string: string.upper(), li))

    return x


# -----------------------------------------------
# ----------------Question No. 14----------------
# -----------------------------------------------
def product(li: List[int]) -> int:
    """Calculates the product of all the numbers in a list.

    doctests:
    >>> product([2, 1, 4])
    8
    >>> product([3, 1, 4, 2, 5, 8])
    960
    """

    x = reduce(lambda a, b: a * b, li)

    return x


if __name__ == "__main__":
    testmod(verbose=True)
