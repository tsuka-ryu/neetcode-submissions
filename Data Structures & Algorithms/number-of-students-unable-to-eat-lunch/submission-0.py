class ListNode:
    def __init__(self, val=None):
            self.val = val
            self.next = None

class LinkedList:
    def __init__(self, arr=None):
        self.head = ListNode()
        self.tail = self.head

        if arr:
            for val in arr:
                self.insertEnd(val)

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def removeHead(self):
        if self.head.next:
            if self.head.next == self.tail:
                self.tail = self.head
            self.head.next = self.head.next.next

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwitcheList = LinkedList(sandwiches)
        studentList = LinkedList(students)
        attempts = 0
        remaining = len(students)

        while sandwitcheList.head.next and studentList.head.next and attempts < remaining:
            currentSandwitch = sandwitcheList.head.next
            currentStudent = studentList.head.next

            if currentSandwitch.val == currentStudent.val:
                sandwitcheList.removeHead()
                studentList.removeHead()
                remaining -= 1
                attempts = 0
            else:
                studentList.insertEnd(currentStudent.val)
                studentList.removeHead()
                attempts += 1
        return remaining