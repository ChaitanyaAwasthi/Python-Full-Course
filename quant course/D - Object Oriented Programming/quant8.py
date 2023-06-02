# Abstract superclass
class SortingAlgorithm:
    def sort(self):
        pass


class InsertionSort(SortingAlgorithm):
    # Function override
    def sort(self):
        print("Insertion sort is running")


class SelectionSort(SortingAlgorithm):
    # Function override
    def sort(self):
        print("Selection sort is running")


class QuickSort(SortingAlgorithm):
    # Function override
    def sort(self):
        print("Quick sort is running")


num = int(input("Please select which sorting algorithm you would like to use: "))

sorting_algorithm_object = None  # Null object

if num == 0:
    sorting_algorithm_object = QuickSort()
elif num == 1:
    sorting_algorithm_object = InsertionSort()
elif num == 2:
    sorting_algorithm_object = SelectionSort()

sorting_algorithm_object.sort()