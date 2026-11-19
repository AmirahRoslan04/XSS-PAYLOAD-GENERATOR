import sys
import ethics
import ui
import encoders
import storage

def main():
    ui.show_banner()
    ethics.show_warning()
    
    if not ethics.check_authorization():
        sys.exit()
        
    while True:
        payload = ui.get_payload()
        if payload.lower() == 'exit':
            print("\n[!] Exiting safely. Goodbye!")
            sys.exit()
            
        all_encodings = encoders.generate_all_encodings(payload)
        
        ui.display_results(all_encodings)
        
        if ui.ask_save():
            saved_path = storage.save_payloads(payload, all_encodings)
            if saved_path:
                print(f"\n[+] Payloads safely saved to {saved_path}")
            else:
                print("\n[-] Error saving payloads to disk.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting safely. Goodbye!")
        sys.exit(0)
