class Parenthesis:

    @staticmethod
    def is_valid(s):
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                token = stack.pop()
                if token == "(" and c != ")":
                    return False
                if token == "[" and c != "]":
                    return False
                if token == "{" and c != "}":
                    return False

        return len(stack) == 0
