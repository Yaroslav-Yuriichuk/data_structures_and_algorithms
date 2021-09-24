import unittest
from bst.bst import BST
import random


class TestBST(unittest.TestCase):

    NUMBER_OF_TESTS_PER_TEST_CASE = 10

    def set_up(self):
        bst = BST()
        inserted_items = [random.randint(0, 100)
                          for _ in range(random.randint(1, 50))]
        for item in inserted_items:
            bst.insert(item)

        return bst, inserted_items

    def test_insert_and_items(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            self.assertEqual(bst.items(), sorted(inserted_items))

    def test_size(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            self.assertEqual(len(inserted_items), bst.size())

    def test_clear(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()
            bst.clear()

            self.assertEqual(bst.size(), 0)

    def test_count(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            count_items = {}
            for item in inserted_items:
                if item in count_items:
                    count_items[item] += 1
                else:
                    count_items[item] = 1

            for key, value in count_items.items():
                self.assertEqual(bst.count(key), value)

    def test_min(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            self.assertEqual(bst.min(), sorted(inserted_items)[0])

    def test_max(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            self.assertEqual(bst.max(), sorted(inserted_items)[-1])

    def test_delete_min_delete_all(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            item_to_delete = sorted(inserted_items)[0]
            bst.delete_min()

            self.assertEqual(bst.count(item_to_delete), 0)

    def test_delete_min_delete_one(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            item_to_delete = sorted(inserted_items)[0]
            prev_count = bst.count(item_to_delete)
            bst.delete_min(delete_all=False)

            self.assertEqual(prev_count-1, bst.count(item_to_delete))

    def test_delete_max_delete_all(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            item_to_delete = sorted(inserted_items)[-1]
            bst.delete_max()

            self.assertEqual(bst.count(item_to_delete), 0)

    def test_delete_max_delete_one(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            item_to_delete = sorted(inserted_items)[-1]
            prev_count = bst.count(item_to_delete)
            bst.delete_max(delete_all=False)

            self.assertEqual(prev_count-1, bst.count(item_to_delete))

    def test_delete_delete_all(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            index_to_delete = random.randint(0, len(inserted_items)-1)
            bst.delete(inserted_items[index_to_delete])

            self.assertEqual(bst.count(inserted_items[index_to_delete]), 0)

    def test_delete_delete_one(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            index_to_delete = random.randint(0, len(inserted_items)-1)
            prev_count = bst.count(inserted_items[index_to_delete])
            bst.delete(inserted_items[index_to_delete], delete_all=False)

            self.assertEqual(
                prev_count-1, bst.count(inserted_items[index_to_delete]))

    def test_contains(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()

            for item in inserted_items:
                self.assertTrue(item in bst)

    def test_rank(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()
            inserted_items.sort()

            for item in set(inserted_items):
                i = 0
                while i < len(inserted_items) and inserted_items[i] < item:
                    i += 1

                self.assertEqual(bst.rank(item), i)

    def test_floor(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()
            inserted_items.sort()

            for j in range(inserted_items[-1]+2):
                i = 0
                while i < len(inserted_items) and inserted_items[i] <= j:
                    i += 1

                if i > 0:
                    self.assertEqual(inserted_items[i-1], bst.floor(j))
                else:
                    self.assertEqual(None, bst.floor(j))

    def test_ceiling(self):
        for _ in range(TestBST.NUMBER_OF_TESTS_PER_TEST_CASE):
            bst, inserted_items = self.set_up()
            inserted_items.sort()

            for j in range(inserted_items[-1]+2):
                i = len(inserted_items)-1
                while i > -1 and inserted_items[i] >= j:
                    i -= 1

                if i < len(inserted_items) - 1:
                    self.assertEqual(inserted_items[i+1], bst.ceiling(j))
                else:
                    self.assertEqual(None, bst.ceiling(j))
