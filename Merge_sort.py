class Solution(object) :
    def merge(self, nums1, m, nums2,n):
        nums1_valid = nums1[:m]
        nums2_valid = nums2[:n]
        num = nums1_valid + nums2_valid
        num.sort()
        for i in range(len(num)):
            nums1[i] = num[i]

        return nums1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol.merge(nums1, m, nums2, n)
    print(nums1)