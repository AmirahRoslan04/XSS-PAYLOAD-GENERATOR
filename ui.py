
def show_banner():
    print("=" * 60)
    print("       XSS PAYLOAD GENERATOR & OBFUSCATOR")
    print("=" * 60)
    print(" Educational Tool | Authorized Testing Only")
    print("=" * 60)

def get_payload():
    while True:
        payload = input("\nEnter your base payload: ").strip()

        if not payload:
            print("[!] Payload cannot be empty.")
        elif len(payload) > 2000:
            print("[!] Maximum length is 2000 characters.")
        else:
            return payload

def select_encodings(encoding_options):
    print("\nAvailable Encoding Methods")
    print("-" * 40)

    for number, option in enumerate(encoding_options, start=1):
        print(f"{number}. {option}")

    while True:
        choice = input(
            "\nSelect methods (e.g. 1,2,3): "
        ).strip()

        try:
            selected_numbers = [
                int(number.strip())
                for number in choice.split(",")
            ]

            if not selected_numbers:
                raise ValueError

            if any(
                number < 1 or number > len(encoding_options)
                for number in selected_numbers
            ):
                raise ValueError

            selected = list(dict.fromkeys(
                encoding_options[number - 1]
                for number in selected_numbers
            ))

            return selected

        except ValueError:
            print("[!] Invalid selection. Please try again.")

def display_results(results):
    print("\n" + "=" * 60)
    print("                 GENERATED RESULTS")
    print("=" * 60)

    for label, value in results.items():
        print(f"\n[{label}]")
        print(value)

    print("\n" + "=" * 60)

def ask_save():
    while True:
        choice = input(
            "\nDo you want to save the results? (Y/N): "
        ).strip().lower()

        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("[!] Please enter Y or N.")
