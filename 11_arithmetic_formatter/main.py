class ArithmeticFormatter:
    
    def arithmetic_arranger(problems, show_answers=False):
    #max number of problems
        if len(problems) > 5: 
            return "Error: Too many problems."

        return problems

    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')