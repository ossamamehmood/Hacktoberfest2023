#Python program to convert numbers to Words

def number_to_words(number):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if number < 10:
        return units[number]
    elif number < 20:
        return teens[number - 10]
    elif number < 100:
        return tens[number // 10] + (" " + units[number % 10] if number % 10 != 0 else "")
    elif number < 1000:
        return units[number // 100] + " Hundred" + (" and " + number_to_words(number % 100) if number % 100 != 0 else "")
    elif number < 1000000:
        return number_to_words(number // 1000) + " Thousand" + (" " + number_to_words(number % 1000) if number % 1000 != 0 else "")
    else:
        return "Number out of range"

# Example usage
while True:
    try:
        num = int(input("Enter a number (0 to exit): "))
        if num == 0:
            break
        print("Number in words:", number_to_words(num))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
