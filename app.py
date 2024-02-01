from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_text = data.get('text')
    # Aqui você implementará a lógica para escolher a resposta pré-pronta.
    # Por enquanto, vamos apenas retornar o texto recebido.
    response = {"response": f"Sua entrada foi: {user_text}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
