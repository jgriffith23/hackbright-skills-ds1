def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(n)      ]


    """

    if len(s1) != len(s2):          #O(1)
        return False

    for i in range(len(s1)):        #O(n)
        if s1[i] != s2[i]:          #O(1) for s1[i] and O(1) for s2[i]
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [      O(n)      ]

    """

    # O(n) to look for hippo, plus O(n) to look for platypus. Not looking
    # for platypus for each item we check for hippo.
    if "hippo" in animals or "platpypus" in animals: 
        return True                                  
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n)      ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:                         #O(n) to loop over set
        if -x in s:                     #O(1) to find an item in a set    
            result.append([-x, x])      #O(1) to append item to list.

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n^2)      ]

    """

    result = []

    for x in numbers:                  #O(n) to loop over list
        for y in numbers:              #O(n) to loop over list; loop for each x
            if x == -y:                #O(1) to compare
                result.append((x, y))  #O(1) to append list item.
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [      O(n^2)     ]

    """

    # If result were a set to start with, could avoid
    # the check for duplicates altogether.

    result = []

    for x in numbers:                            # O(n) to loop over list
        for y in numbers:                        # O(n) to loop; loop for each x 
            if x == -y and (y, x) not in result: # O(1) for cmp, O(n) for checking list
                result.append((x, y))            # O(1) for append
    return result
