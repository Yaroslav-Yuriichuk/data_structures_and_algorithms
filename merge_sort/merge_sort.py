import time


class MergeSort:

    def __init__(self, arr, reverse):
        self.compares_number = 0
        aux = arr[:]
        self._sort(arr, aux, 0, len(arr)-1, reverse)

    def _compare(self, a, b, reverse):
        # returns true if a < b and not reverse
        self.compares_number += 1
        return a > b if reverse else a < b

    def _merge(self, arr, aux, low, high, reverse):
        mid = low + (high - low) // 2
        i, j = low, mid + 1

        for k in range(low, high+1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > high:
                arr[k] = aux[i]
                i+= 1
            elif self._compare(aux[j], aux[i], reverse):
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1

    def _sort(self, arr, aux, low, high, reverse):
        if  high - low < 1:
            return

        mid = low + (high - low) // 2
        self._sort(aux, arr, low, mid, reverse)
        self._sort(aux, arr, mid+1, high, reverse)
        self._merge(arr, aux, low, high, reverse) 

    @staticmethod
    def sort(arr, reverse=False, show_info=False):
        if show_info:
            print("MergeSort")
            print("Input list: ", arr)
            start_time = time.perf_counter()
            compares_number = MergeSort(arr, reverse=reverse).compares_number
            print("Execution time: %.7f" % (time.perf_counter() - start_time))
            print(f"Number of compares: {compares_number}")
            print("Sorted list: ", arr)
        else:    
            MergeSort(arr, reverse=reverse)

