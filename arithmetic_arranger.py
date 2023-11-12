def arithmetic_arranger(problems, display_result=False):
  if len(problems) > 5:
      return "Error: Too many problems."
  
  arranged_problems = {"top": [], "bottom": [], "dash": [], "result": []}
  
  for problem in problems:
    operand1, operator, operand2 = problem.split()

    if operator not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'."

    if not operand1.isdigit() or not operand2.isdigit():
        return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."

    result = str(eval(problem))
    max_length = max(len(operand1), len(operand2))

    arranged_problems["top"].append(operand1.rjust(max_length + 2))
    arranged_problems["bottom"].append(operator + operand2.rjust(max_length + 1))
    arranged_problems["dash"].append("-" * (max_length + 2))
    arranged_problems["result"].append(result.rjust(max_length + 2) if display_result else "")

  if display_result:
    arranged_lines = [
        "\t".join(arranged_problems["top"]),
        "\t".join(arranged_problems["bottom"]),
        "\t".join(arranged_problems["dash"]),
        "\t".join(arranged_problems["result"])
    ]
  else:
    arranged_lines = [
        "    ".join(arranged_problems["top"]),
        "    ".join(arranged_problems["bottom"]),
        "    ".join(arranged_problems["dash"])
    ]

  return "\n".join(arranged_lines)
  

print(arithmetic_arranger(["3298 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
