class Node:
  def __init__(self, data=None):
    self.left = None
    self.right = None
    self.data = data
def insertNode(root,node):
  if root is None:
    root = node
  else:
    if root.data < node.data:
      if root.right is None:
        root.right = node
      else:
        insertNode(root.right,node)
    else:
      if root.left is None:
        root.left = node
      else:
        insertNode(root.left,node)
def inOrder(root):
  if root:
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
def search(root, data):
  if (root == None or root.data == data):
    return root
  if root.data < data:
    return search(root.right,data)
  return search(root.left,data)



root = Node(50)
insertNode(root, Node(30))
insertNode(root, Node(20))
insertNode(root, Node(40))
insertNode(root, Node(70))
insertNode(root, Node(60))
insertNode(root, Node(80))

inOrder(root)
res = search(root, 10)
if res:
  print(res.data)
else:
  print("Key not found!")
