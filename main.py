# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", ], True))
print(arithmetic_arranger(["32 + 6989"]))
print(arithmetic_arranger(["3244 - 69895"]))
print(arithmetic_arranger(["3244 - 6t89"]))
print(arithmetic_arranger(["3244 * 6t89"]))
print(arithmetic_arranger(["3244 - 6t89"]))
print(arithmetic_arranger(["3244 - 6989", "3801 - 2", "45 + 43", "123 + 49", "123 + 49", "0 + 0"], True))
print(arithmetic_arranger(["0 + 0"], True))
print(arithmetic_arranger(["9999 + 9999"], True))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))


# Run unit tests automatically
main(['-vv'])
