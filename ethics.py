# Ethical warning for XSS Payload Generator

def show_warning():
    print("========================================")
    print("          ETHICAL USE WARNING")
    print("========================================")
    print("This tool is for educational and authorized")
    print("security testing purposes only.")
    print("Unauthorized access may violate Malaysia's")
    print("Computer Crimes Act 1997.")
    print("Only test systems with written permission.")
    print("Testing must stay within the approved scope.")
    print("========================================")

def check_authorization():
    answer = input("Do you have written authorization? (y/n): ")

    if answer.strip().lower() in ["y", "yes"]:
        print("Authorization confirmed.")
        return True
    else:
        print("Access denied. Authorization is required.")
        return False

if __name__ == "__main__":
    show_warning()

    if check_authorization():
        print("You may continue.")
    else:
        print("Program stopped.")

