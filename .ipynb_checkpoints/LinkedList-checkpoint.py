class LinkedList:
    
    def __str__(self):
        if self.size == 0:
            return '[]'
        result = []
        current = self.head
        while current:
            result.append(str(current))
            current = current.next
        return f"[{' -> '.join(result)}]"
    
    def is_empty(self):
        return self.head is None