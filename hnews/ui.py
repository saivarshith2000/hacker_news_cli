# This is a constant
MAX_COLS = 80


def printAllResults(resultArray, printTopLine=False):
    # Prints a nicely formatted list of all results
    # Prints a horizontal line at the top if arg is passed
    if printTopLine:
        printHoriziontalLine()
    for result in resultArray:
        printResult(result)
        printHoriziontalLine()
    return


def printResult(result):
    # Function to display a neatly formatted result
    # Length of the box is MAX_COLS cols. (most common terminal size)
    # Any text above MAX_COLS cols wide will put be in a new line
    print(breakLine(result["name"]))
    print(breakLine(result["url"]))
    print(
        "{}     -----     {}".format(result["age"], result["points"]), end="")


def breakLine(text):
    # Takes a text and Breaks into lines of 76 characters
    numberOfLines = 1 + len(text) // MAX_COLS
    output = ""
    start = 0
    for i in range(0, numberOfLines):
        output = output + text[start: start + MAX_COLS] + "\n"
        start = start + MAX_COLS + 1
    return output


def printHoriziontalLine():
    # Prints a horizontal line with a width of MAX_COLS
    for i in range(0, MAX_COLS):
        print("_", end="")
    print()
