class ArithmeticFormatter:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.top_int = ""
        self.bottom_int = ""
        self.line_format = ""
        self.result= ""

    def arithmetic_arranger(self, problems, show_answers=False):
        self.reset()

    #max number of problems
        if len(problems) > 5: 
            return "Error: Too many problems."
        
        arranged_problems = []

        for problem in problems:
            parts = problem.split()
            operand1, operator, operand2 = parts

            if operator not in ('+', '-'):
                return "Error: Operator must ne '+' or '-'."
            
            if not operand1.isdigit() or not operand2.isdigit():
                return "Error: Numbers must only contain digits."
            
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."



        return problems

    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')