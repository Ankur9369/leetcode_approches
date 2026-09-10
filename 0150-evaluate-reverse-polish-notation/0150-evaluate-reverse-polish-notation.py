class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second_recent = stack.pop()
                first_recent = stack.pop()

                if token == "+":
                    stack.append(first_recent + second_recent)

                elif token == "-":
                    stack.append(first_recent - second_recent)

                elif token == "*":
                    stack.append(first_recent * second_recent)

                elif token == "/":
                    result = abs(first_recent) // abs(second_recent)

                    if (first_recent < 0) != (second_recent < 0):
                        result = -result

                    stack.append(result)

            else:
                stack.append(int(token))

        return stack[-1]