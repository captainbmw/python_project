def findMedianSortedArrays(nums1, nums2):
    nums=nums1 + nums2
    nums.sort()
    n=len(nums)
    if n % 2==1:
        return nums[n//2]
    else:
        return (nums[n//2-1] + nums[n//2])/2

nums1=[2,4,5,7,5,1]
nums2=[2,3,6,8,9]
print(findMedianSortedArrays(nums1, nums2))

nums1=[1,2,3]
nums2=[4,5,6]
print(findMedianSortedArrays(nums1, nums2))

def check_weird(n):
    if n % 2 != 0:
        print("Not Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Not Weird")
    elif n % 2 == 0 and n > 60:
        print("Weird")

n=int(input("Enter the number of elements: "))
check_weird(n)


