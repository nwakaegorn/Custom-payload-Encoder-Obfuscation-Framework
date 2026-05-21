import base64
import zlib

class PayloadDecoder:

    @staticmethod
    def multi_layer_decode(encoded_data: str) -> str:
        base64_bytes = bytes.fromhex(encoded_data)
        compressed = base64.b64decode(base64_bytes)
        original = zlib.decompress(compressed)
        return original.decode()