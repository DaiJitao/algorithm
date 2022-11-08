import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

def demo162(nums):
    if nums is None:
        return
    n = len(nums)
    if n <=2:
        return

    midd = n // 2
    left = midd - 1
    right = midd + 1
    while 0 < left < midd < right < n:
        if nums[left] < nums[midd] > nums[right]:
            return midd
        if nums[left] < nums[midd] < nums[right]:
            left = midd
            midd = right
            right += 1
        


if __name__ == '__main__':
    unittest.main()
