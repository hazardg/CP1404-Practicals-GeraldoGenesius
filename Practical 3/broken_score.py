def main():
    score = float(input("Enter the score: "))
    print(determine_status(score))

def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >=90:
        return "Excellent"
    elif score >=50:
        return "Passable"
    else:
        return "Bad"

main()