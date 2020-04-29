import numpy

"""
Insertion-Sort takes an input array A[1..n] and sorts the sequence of elements such that A[1] <= A[2] <= ... <= A[n].

Insertion-Sort takes an input array A[1..n] and sorts elements in place by maintaining a list of sorted elements in the
left of the array, with a constant number stored outside the array while inserting.

Input: A sequence of n numbers <a_1, a_2, ..., a_n>.
Output: A permutation <a'_1, a'_2, ..., a'_n> of the input sequence such that a'_1 <= a'_2 <= ... <= a'_n.
"""


def insertion_sort(unsorted_sequence):
    # 1  for j = 2 to A.length
    for j in range(2, len(unsorted_sequence)):
        # 2  key = A[j]
        key = unsorted_sequence[j]
        # 4  i = j - 1
        i = j - 1
        # 5  while i > 0 and A[i] > key
        while i >= 0 and unsorted_sequence[i] > key:
            # 6  A[i + 1] = A[i]
            unsorted_sequence[i + 1] = unsorted_sequence[i]
            i = i - 1
        unsorted_sequence[i + 1] = key
    return unsorted_sequence
