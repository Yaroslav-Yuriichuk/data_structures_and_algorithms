import sys
from merge_sort.merge_sort import MergeSort

def parse_data(data):
    data, sort_order = list(map(lambda x: x + ',', data[1:])), data[0]
    assert(sort_order == "asc" or sort_order == "desc")
    return [int(x) for x in "".join(data).split(",") if not x == ''], sort_order

def main():
    sort_orders ={
        "asc": False,
        "desc": True
    }
    data, sort_order = parse_data(sys.argv[1:])
    
    MergeSort.sort(data, show_info=True, reverse=sort_orders[sort_order])

if __name__ == "__main__":
    main()