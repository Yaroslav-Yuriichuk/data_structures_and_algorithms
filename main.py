from bst.bst import BST


def main():
    bst = BST()

    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.insert(8)
    bst.insert(10)

    print(bst)

    bst.delete(2, delete_all=False)
    bst.delete(2, delete_all=False)
    bst.delete(3)
    bst.delete(8)
    # bst.delete_max(delete_all=False)
    # bst.delete_max(delete_all=False)

    print(bst.items())

    print(bst.count(2))


if __name__ == "__main__":
    main()
