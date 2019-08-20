# Let's implement a text buffer data structure, that could be utilized by the text editors we use everyday, with the following methods:
# __str__ - Allows us to call print() on our buffer to print out all of its contents
# append - Adds a character to the back of the text buffer
# prepend - Adds a character to the front of the text buffer
# delete_front - Removes a character from the front of the text buffer
# delete_back - Removes a character from the back of the text buffer
# join - Concatenates another text buffer onto the end of this buffer
# These methods should all be as efficient as possible (we can get most of them down to O(1) time). To achieve this, what data structure(s) would make good candidates for backing our text buffer implementation? An array? A LinkedList? A DoublyLinkedList?


from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    #init is a string we can initialize the buffer with
    def __init__(self, init = None):
        self.contents = DoublyLinkedList()

        if init:
            for char in init:
                self.contents.add_to_tail(char)

    def __str__(self):
        #needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, char_to_add):
        self.contents.add_to_tail(char_to_add)

    def prepend(self, char_to_add):
        self.contents.add_to_head(char_to_add)
# Delete a provided number of characters from the front
    def delete_front(self, num_to_remove):
        for _ in range(num_to_remove):
            self.contents.remove_from_head()
# Delete a provided number of characters from the back
    def delete_back(self, num_to_remove):
        for _ in range(num_to_remove):
            self.contents.remove_from_tail()
# join - concatenates another text buffer onto the end of this buffer
    def join(self, other_buffer):

        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail

        self.contents.tail = other_buffer.contents.tail


tb = TextBuffer("Hello CS20")
print(tb)

tb.append("9")
tb.prepend("0")

#Expected output: 0Hello CS209
print(tb)

tb.delete_front(2)
tb.delete_back(2)

print(tb)

tb2 = TextBuffer("We made it!")
tb.join(tb2)

print(tb)