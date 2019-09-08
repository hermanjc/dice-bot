import random
import re

# Dice Regex Expression: (\d+)d(\d+)
# Dice Regex Expression 2.0: (\d+)d(\d+)|\d
dice_regex = re.compile(r'(\d+)d(\d+)')

# Decimal Dice Regex Expression: (\d+)d(\d+)\.(\d+)

# Matches all strings: ((\d+)d(\d+)|\d+)(\s*[\+\-\*/]\s*((\d+)d(\d+)|\d+))*

class DiceError(RuntimeError):
    def __init__(self, error_string):
        self.error_string = error_string

def roll_die(sides):
    if(sides > 0):
        #return random.randrange(1, sides + 1)
        return random.randint(1, sides)
    else:
        raise DiceError("ERROR: Dice must have 1 or more sides")

def roll_expression(expr, long_output=False, special_message=False):
    # if(dice_regex.match(expr) == None):
    #     raise DiceError("ERROR: Invalid expression")

    if(re.match(r'((\d+)d(\d+)|\d+)(\s*[\+\-\*/]\s*((\d+)d(\d+)|\d+))*', expr) == None):
        raise DiceError("ERROR: Invalid expression")
    
    num_dice = int(dice_regex.match(expr).group(1))
    sides = int(dice_regex.match(expr).group(2))

    output_str = ""
    total = 0

    for i in range(num_dice):
        roll = roll_die(sides)
        total += roll

        if(long_output and num_dice > 1):
            output_str += str(roll)

            if(i != num_dice - 1):
                output_str += " + "
    
    if(long_output and num_dice > 1):
        output_str += " = " + str(total)
    else:
        output_str += str(total)
    
    if(special_message):
        if(expr == "1d20" and total == 20):
            output_str += "\n**CRITICAL HIT!**"
        # elif(expr == "1d20" and total == 1):
        #     output_str += "\n**CRITICAL FAILURE!**"
        elif(num_dice > 0 and total == num_dice * sides):
            output_str += "\n**MAXIMUM DAMAGE!**"

    return output_str

if __name__ == '__main__':
    print(roll_expression("1d20 + 5", special_message=True))

    # for i in range(20):
    #     print(roll_expression("1d20", special_message=True))
    # while(1):
    #     i = input()
    #     try:
    #         print(roll_expression(i, special_message=True, long_output=True))
    #     except DiceError as e:
    #         print("ERROR: " + e.error_string)