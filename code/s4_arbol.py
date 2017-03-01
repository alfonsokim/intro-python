# =============================================================================
class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, node):
        return self.value < node.value

    def __le__(self, node):
        return self.value <= node.value

    def __gt__(self, node):
        return self.value > node.value

    def __ge__(self, node):
        return self.value > node.value

    def __eq__(self, node):
        return self.value == node.value

    def __ne__(self, node):
        return self.value != node.value

    def __str__(self):
        return '%s' % str(self.value)


# =============================================================================
class Tree():

    def __init__(self):
        self.root = None
        self.lenght = 0

    # -------------------------------------------------------------------------
    def append(self, value):
        new = Node(value)
        def recursive_add(node):
            if new < node:
                if node.left:
                    return recursive_add(node.left)
                else:
                    node.left = new
                    self.lenght += 1
                    return True
            elif new > node:
                if node.right:
                    return recursive_add(node.right)
                else:
                    node.right = new
                    self.lenght += 1
                    return True
            else:
                return False
        if not self.root:
            self.root = new
            self.lenght += 1
            return True
        else:
            return recursive_add(self.root)

    # -------------------------------------------------------------------------
    def values(self):
        elements = []
        def recursive_values(node):
            if node:
                recursive_values(node.left) 
                elements.append(node.value)
                recursive_values(node.right)
        # ----
        recursive_values(self.root)
        return elements

    # -------------------------------------------------------------------------
    def __add__(self, other):
        new = Tree()
        for value in self.values():
            new.append(value)
        for value in other.values():
            new.append(value)
        return new

    # -------------------------------------------------------------------------
    def __contains__(self, value):
        node = Node(value)
        def recursive_find(other):
            if other:
                if other == node:
                    return True
                elif node < other:
                    return recursive_find(other.left)
                else:
                    return recursive_find(other.right)
            return False
        # ---
        return recursive_find(self.root)

    # -------------------------------------------------------------------------
    def __len__(self):
        return self.lenght

    # -------------------------------------------------------------------------
    def __str__(self):
        def recursive_str(node):
            if node:
                return '%s %s %s' % (
                    recursive_str(node.left), 
                    str(node), 
                    recursive_str(node.right)
                )
            else:
                return ''
        # ----
        return recursive_str(self.root)


# =============================================================================
tree = Tree()
map(tree.append, range(10))
print 'Arbol: %s' % str(tree)
print 'Agregar 2?: %s' % tree.append(2)
print 'Agregar 20?: %s' % tree.append(20)
print 'Arbol contiene 5? %s' % (5 in tree)
print 'Arbol contiene -1? %s' % (-1 in tree)

tree2 = Tree()
map(tree2.append, range(0, -10, -1))
print 'Arbol 2: %s' % str(tree2)
tree3 = tree + tree2
print 'Arbol 3: %s' % str(tree3)
