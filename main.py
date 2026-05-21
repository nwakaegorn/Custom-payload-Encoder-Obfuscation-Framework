from encoder import PayloadEncoder
from obfuscator import PayloadObfuscator
from decoder import PayloadDecoder

def main():
    payload = input("Enter your payload: ")

    encoder = PayloadEncoder()
    obfuscator = PayloadObfuscator()
    decoder = PayloadDecoder()

    # Encode
    encoded = encoder.multi_layer_encode(payload)
    print("\nEncoded Payload:")
    print(encoded)

    # Obfuscate
    obfuscated = obfuscator.reverse_string(encoded)
    print("\nObfuscated Payload:")
    print(obfuscated)

    # Deobfuscate
    restored = obfuscator.reverse_string(obfuscated)

    # Decode
    decoded = decoder.multi_layer_decode(restored)
    print("\nDecoded Payload:")
    print(decoded)

if __name__ == "__main__":
    main()