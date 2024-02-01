from flask import request, jsonify

def register_predict_route(app):
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        user_text = data.get('text')
        # Implemente a lógica para escolher a resposta pré-pronta aqui.
        response = {"response": f"Sua entrada foi: {user_text}"}
        return jsonify(response)
