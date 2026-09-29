class Solution(object):

    def threeSum(self, nums):

        arr = sorted(nums)
        ans = []

        for i in range(len(arr) - 2):

            # Skip duplicate x
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            x = arr[i]

            y = i + 1
            z = len(arr) - 1

            while y < z:

                two_sum = arr[y] + arr[z]

                if two_sum == -x:

                    ans.append([x, arr[y], arr[z]])

                    y += 1
                    z -= 1

                    # Skip duplicate y
                    while y < z and arr[y] == arr[y - 1]:
                        y += 1

                    # Skip duplicate z
                    while y < z and arr[z] == arr[z + 1]:
                        z -= 1

                elif two_sum > -x:
                    z -= 1

                else:
                    y += 1

        return ans