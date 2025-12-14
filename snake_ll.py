from utils import *

class Node:
    """
    Represents a single node (segment) in the Snake's body Linked List.
    Each node holds its position on the grid and a reference to the next segment.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None  # Pointer to the next node in the linked list

class SnakeLinkedList:
    """
    Implements the Snake's body using a Singly Linked List data structure.
    
    Why Linked List?
    - Efficient Movement: Moving the snake involves adding a new head and removing the tail.
      These are O(1) operations (with a tail pointer) or O(N) for tail removal in singly linked list,
      which is performant enough for this game scale.
    - Dynamic Growth: Easy to extend the body without reallocation overhead common in arrays.
    """
    def __init__(self):
        # Starting position of the snake (Center of the grid)
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        
        # Initialize the snake with 3 segments (Nodes)
        # The head is at the starting position
        self.head = Node(start_x, start_y)
        
        # Create body segments extending downwards for the initial setup
        node2 = Node(start_x, start_y + 1)
        node3 = Node(start_x, start_y + 2)
        
        # Link the nodes together: Head -> Node2 -> Node3
        self.head.next = node2
        node2.next = node3
        
        # Keep track of the tail node for potential optimizations or easy access
        self.tail = node3 
        
        # Initial movement direction (Moving UP towards the top of the screen)
        self.direction = UP 
        
        # Flag to indicate if the snake should grow on the next move
        self.grow_pending = False 

    def move(self):
        """
        Moves the snake one step in the current direction.
        
        The Linked List movement logic:
        1. Calculate new head coordinates based on current direction.
        2. Create a new Node at these coordinates.
        3. Insert this new Node at the beginning of the list (New Head).
        4. If the snake is NOT growing, remove the last Node (Tail) to maintain length.
        """
        # 1. Calculate new head coordinates
        new_x = self.head.x + self.direction[0]
        new_y = self.head.y + self.direction[1]
        
        # 2. Create the new head node
        new_head = Node(new_x, new_y)
        
        # 3. Insert at the beginning (Head Insertion)
        new_head.next = self.head
        self.head = new_head
        
        # 4. Handle Tail deletion (Movement vs Growth)
        if not self.grow_pending:
            # If not growing, the tail moves 'forward' by being deleted
            self.delete_tail()
        else:
            # If growing, we keep the tail (effectively increasing length by 1)
            # Reset the flag after consuming the growth 'credit'
            self.grow_pending = False 

    def delete_tail(self):
        """
        Removes the last node (tail) from the linked list.
        
        In a Singly Linked List, to delete the last node, we need access to the 
        second-to-last node to update its 'next' pointer to None.
        
        This requires traversing the list from the head, which is an O(N) operation.
        While a Doubly Linked List would make this O(1), O(N) is negligible here 
        given the maximum possible size of the snake.
        """
        # Safety check: Do nothing if list is empty or has only one node
        if self.head is None or self.head.next is None:
            return 

        # Traverse to find the second-to-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # 'current' is now the node BEFORE the tail
        # Remove the link to the old tail
        current.next = None
        
        # Update our tail reference to be this new last node
        self.tail = current

    def grow(self):
        """
        Signals that the snake should grow on the next move.
        This is typically called when the snake eats food.
        """
        self.grow_pending = True

    def check_collision_with_self(self):
        """
        Checks if the snake's head has collided with any part of its body.
        
        This requires an O(N) traversal of the list to compare coordinates.
        """
        head_x = self.head.x
        head_y = self.head.y
        
        # Start checking from the second node (neck), as head cannot collide with itself
        current = self.head.next 
        while current is not None:
            if current.x == head_x and current.y == head_y:
                return True # Collision detected
            current = current.next
        return False
        
    def get_coordinates(self):
        """
        Returns a list of (x, y) tuples representing the snake's body positions.
        Used primarily for rendering the snake on the screen.
        """
        coords = []
        current = self.head
        while current is not None:
            coords.append((current.x, current.y))
            current = current.next
        return coords
