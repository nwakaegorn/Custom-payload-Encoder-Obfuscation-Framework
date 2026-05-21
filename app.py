from flask import Flask, render_template, request
from encoder import PayloadEncoder
from obfuscator import PayloadObfuscator
from decoder import PayloadDecoder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encoded = None
    obfuscated = None
    decoded = None

    if request.method == "POST":
        payload = request.form.get("payload")

        encoder = PayloadEncoder()
        obfuscator = PayloadObfuscator()
        decoder = PayloadDecoder()

        encoded = encoder.multi_layer_encode(payload)
        obfuscated = obfuscator.reverse_string(encoded)
        restored = obfuscator.reverse_string(obfuscated)
        decoded = decoder.multi_layer_decode(restored)

    return render_template("index.html",
                           encoded=encoded,
                           obfuscated=obfuscated,
                           decoded=decoded)

if __name__ == "__main__":
    app.run(debug=True)