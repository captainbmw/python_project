# def findMedianSortedArrays(nums1, nums2):
#     nums=nums1 + nums2
#     nums.sort()
#     n=len(nums)
#     if n % 2==1:
#         return nums[n//2]
#     else:
#         return (nums[n//2-1] + nums[n//2])/2
#
# nums1=[2,4,5,7,5,1]
# nums2=[2,3,6,8,9]
# print(findMedianSortedArrays(nums1, nums2))
#
# nums1=[1,2,3]
# nums2=[4,5,6]
# print(findMedianSortedArrays(nums1, nums2))
#
# def check_weird(n):
#     if n % 2 != 0:
#         print("Not Weird")
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Weird")
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Not Weird")
#     elif n % 2 == 0 and n > 60:
#         print("Weird")
#
# n=int(input("Enter the number of elements: "))
# check_weird(n)





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

# Create first linked list: 2 -> 4 -> 3 (represents 342)
l1 = ListNode(2, ListNode(4, ListNode(3)))

# Create second linked list: 5 -> 6 -> 4 (represents 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Add the two numbers
result = addTwoNumbers(l1, l2)

# Print the resulting linked list: 7 -> 0 -> 8 (represents 807)
while result:
    print(result.val, end=" -> ")
    result = result.next

