import random
import re

# Matches all strings: ((\d+)d(\d+)|\d+)(\s*[\+\-\*/]\s*((\d+)d(\d+)|\d+))*
# Dice Regex Expression: (\d+)d(\d+)|\d+
dice_regex = re.compile(r'(\d+)d(\d+)|\d+')

class DiceError(RuntimeError):
    def __init__(self, error_string):
        self.error_string = error_string

def roll_die(sides):
    if(sides > 0):
        return random.randint(1, sides)
    else:
        raise DiceError("ERROR: Dice must have 1 or more sides")

def roll_subexpr(subexpr, long_output=False, special_message=False, parentheses=False, equals=False):
    if dice_regex.fullmatch(subexpr) == None:
        raise DiceError("ERROR: Invalid expression")

    output_str = ""
    total = 0

    if re.fullmatch(r'\d+', subexpr) != None:
        total = int(subexpr)
        output_str += str(subexpr)
    else:
        num_dice = int(dice_regex.match(subexpr).group(1))
        sides = int(dice_regex.match(subexpr).group(2))

        if long_output and parentheses:
            output_str += "("

        for i in range(num_dice):
            roll = roll_die(sides)
            total += roll

            output_str += str(roll)
            if long_output and i != num_dice - 1:
                output_str += " + "    
        
        if not long_output:
            output_str += str(total)

        if long_output and parentheses:
            output_str += ")"
        
        if long_output and num_dice > 1 and equals:
            output_str += " = " + str(total)
    
        if(special_message):
            if(num_dice == 1 and sides == 20 and total == 20):
                output_str += "\nCRITICAL HIT!"
            elif(num_dice == 1 and sides == 20 and total == 1):
                output_str += "\nCRITICAL FAILURE!"

    return (total, output_str)

def roll_expression(expr, long_output=False, special_message=False):
    if re.fullmatch(r'((\d+)d(\d+)|\d+)(\s*[\+\-\*/]\s*((\d+)d(\d+)|\d+))*', expr) == None:
        raise DiceError("ERROR: Invalid expression")

    total = 0
    output_str = ""
    operator = ' ' 

    sub_exprs = expr.split()
    print(sub_exprs)

    if len(sub_exprs) == 1:
        return roll_subexpr(sub_exprs[0], long_output=long_output, special_message=special_message, equals=True)

    else:
        for e in sub_exprs:
            if(e == '+' or e == '-' or e == '*' or e == '/'):
                operator = e
            else:
                subresult = roll_subexpr(e, long_output=long_output, special_message=False, parentheses=True)

                if(operator == '+'):
                    total += subresult[0]
                    output_str += ' + ' + subresult[1]
                elif(operator == '-'):
                    total -= subresult[0]
                    output_str += ' - ' + subresult[1]
                elif(operator == '*'):
                    total *= subresult[0]
                    output_str += ' * ' + subresult[1]
                elif(operator == '/'):
                    if e == '0':
                        raise DiceError("Cannot divide by zero")
                    total /= subresult[0]
                    output_str += ' / ' + subresult[1]
                elif(operator == ' '):
                    total += subresult[0]
                    output_str += subresult[1]
                else:
                    raise DiceError("Invalid operator")
                
        output_str += ' = ' + str(total)
    
    return (total, output_str)