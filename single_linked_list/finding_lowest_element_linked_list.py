class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def findLowestValue(head):

  # --- EDGE CASE ---
  # if head is none return None
  # if head has only one value return data immedielty 
  
  if head is None:
    return None

  if not head.next:
    return head.data

  min_value = head.data
  pointer = head

  while pointer:
    if pointer.data < min_value:
      min_value = pointer.data
    pointer = pointer.next
  return min_value

 # --- TIME COMPLEXITY ---
 # O(N) depends on the length of the nodes becaouse you have to visit each once

 # --- SPACE COMPLEXITY ---
 # O(1) as we saving a single minimum value

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(1)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))



 
    
    