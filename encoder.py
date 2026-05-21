import base64
import zlib

class PayloadEncoder:

    @staticmethod
    def encode_base64(data: str) -> str:
        return base64.b64encode(data.encode()).decode()

    @staticmethod
    def encode_hex(data: str) -> str:
        return data.encode().hex()

    @staticmethod
    def compress_data(data: str) -> bytes:
        return zlib.compress(data.encode())

    def multi_layer_encode(self, payload: str) -> str:
        compressed = self.compress_data(payload)
        base64_encoded = base64.b64encode(compressed)
        hex_encoded = base64_encoded.hex()
        return hex_encoded