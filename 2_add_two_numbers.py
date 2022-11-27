class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return (lambda V:all((V[0]or V[1])and[V.__setitem__(2,(V[0].val if V[0]else 0)+(V[1].val if V[1]else 0)+V[2]//10)or V[3].__setattr__('next',ListNode(V[2]%10))or V.__setitem__(0,V[0]and V[0].next)or V.__setitem__(1,V[1]and V[1].next)or V.__setitem__(3,V[3]and V[3].next)]for _ in iter(int,1))or V[2]>9 and V[3].__setattr__('next',ListNode(1))or V[4].next)([l1,l2,0]+[ListNode()]*2)

#=======================
# Explanation

# Expanded. Each line corresponds to a line in the original solution below
# Consecutive expressions are chained together using and/or operator.

# First set up the mutable variables: V = [l1, l2, carry, node, placeholder]
(lambda V:<INNER_LAMBDA>)([l1,l2,0]+[ListNode()]*2)
    # While loop
    all((V[0]or V[1])and <INNER_LOOP> for _ in iter(int,1)) or
        # Inner of while loop. Each expression below is Falsy, so use "or" to chain them
        # Set carry, node.next, l1, l2, node
        V.__setitem__(2,(V[0].val if V[0]else 0)+(V[1].val if V[1]else 0)+V[2]//10) or
        V[3].__setattr__('next',ListNode(V[2]%10)) or
        V.__setitem__(0,V[0]and V[0].next) or
        V.__setitem__(1,V[1]and V[1].next) or
        V.__setitem__(3,V[3]and V[3].next) or
    # Extra last digit if needed
    V[2]>9 and V[3].__setattr__('next',ListNode(1)) or
    # Return placeholder.next
    V[4].next

# The original solution
# Simply go through each pair of digit and sum them, carrying over if needed
class SolutionExpanded:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Trick: start with a placeholder node as the head of the result list
        # Then at the end remove the placeholder and return the rest
        # So we don't have to deal with None check
        placeholder = node = ListNode()
        carry = 0
        while l1 or l2:
            carry = (l1 and l1.val or 0)+(l2 and l2.val or 0)+carry//10
            node.next=ListNode(carry%10)
            l1=l1 and l1.next
            l2=l2 and l2.next
            node = node.next
        # Extra last digit if needed
        if carry//10: node.next = ListNode(1)
        return placeholder.next