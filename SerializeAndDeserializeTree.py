# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        queue = Queue()
        queue.push(root)
        serial = []
        while queue.length != 0:
            node = queue.pop()
            raw_node = [node.val,node.left,node.right]
            if raw_node[1]:
                queue.push(raw_node[1])
                raw_node[1] = len(serial) + queue.length
            if raw_node[2]:
                queue.push(raw_node[2])
                raw_node[2] = len(serial) + queue.length
            serial.append(raw_node)
        return str(serial)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        def make_node(node_index,data):
            if node_index != None:
                node = TreeNode(data[node_index][0])
                node.left  = make_node(data[node_index][1],data)
                node.right = make_node(data[node_index][2],data)
                return node
            else:
                return None
        
        queue = Queue()
        node_list = [val.strip().strip('[').strip(']')  for val in data.split(',')]
        node_list = [int(val) if val != 'None' else None for val in node_list]
        node_list = [node_list[i:i+3] for i in range(0,len(node_list),3)]
        root = make_node(0, node_list)
        return root

        

class Queue(object):
    def __init__(self):
        self.queue = []
        self.length = 0
    
    def push(self,x):
        self.queue.append(x)
        self.length += 1
    
    def pop(self):
        val = self.queue[0]
        self.queue.remove(val)
        self.length -= 1
        return val
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
