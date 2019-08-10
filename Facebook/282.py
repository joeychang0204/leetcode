class Solution:
    def addOperators(self, num: 'str', target: 'int'):

        answers = []
        # '123', target=6
        def recurse(index, prev_operand, current_operand, value, string):
            print(index, prev_operand, current_operand, value, string)
            # Done processing all the digits in num
            if index == len(num):

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            recurse(index + 1, current_operand, 0, value + current_operand, string + ['+', str_op])

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                recurse(index + 1, -current_operand, 0, value - current_operand, string + ['-', str_op])

                # MULTIPLICATION
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string + ['*', str_op])
        recurse(0, 0, 0, 0, [])    
        return answers
Solution().addOperators('123', 6)
