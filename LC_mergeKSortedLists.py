# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoSortedLL(L1,L2):
        if L1==None and L2==None:
            return None
        elif L1==None:
            return L2
        elif L2==None:
            return L1
        curr1=L1
        curr2=L2
        if curr1.val>curr2.val:
            head=curr2
        else:
            head=curr1
        while(curr1!=None and curr2!=None):
            flg=0
            flg1=0
            while curr1!=None and curr2.val>=curr1.val:
                prev=curr1
                curr1=curr1.next
                flg=1
            if flg==1:
                prev.next=curr2
            if curr1!=None:
                while curr2!=None and curr1.val>curr2.val:
                    prev=curr2
                    curr2=curr2.next
                    flg1=1
                if flg1==1:
                    prev.next=curr1
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while(len(lists)>1):
            mergedLists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                mergedLists.append(Solution.mergeTwoSortedLL(l1,l2))
            lists=mergedLists
        return lists[0]
