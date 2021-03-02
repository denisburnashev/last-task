class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_balanced(self, text, brackets='〈〉()[]{}'):
        opening = brackets[::2]
        closing = brackets[1::2]
        stack = Stack()
        for character in text:
            if character in opening:
                stack.push(opening.index(character))
            elif character in closing:
                if stack.size() == 0:
                    return 'Несбалансированно'
                elif stack and stack.peek() == closing.index(character):
                    stack.pop()
                else:
                    return 'Несбалансированно'
        return 'Сбалансированно'


list_bracket = ['((({})))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']

for bracket in list_bracket:
    print(Stack().is_balanced(bracket))
