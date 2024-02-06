import asyncio
import websockets
import json

async def test_cart_consumer():
    uri = "ws://localhost:8001/ws/cart/?token=token_teste"
    async with websockets.connect(uri) as websocket:
        # Supondo que você já tenha um objeto Comida com ID 1 no seu banco de dados.
        # Substitua 1 pelo ID real do objeto Comida que você deseja testar.
        comida_id = 1

        # Adicionar um item ao carrinho
        add_message = {
            "action": "add",
            "comida_id": comida_id,
            "quantidade": 2
        }
        await websocket.send(json.dumps(add_message))
        response = await websocket.recv()
        print(f"Resposta ao adicionar: {response}")

        # Visualizar itens no carrinho
        view_message = {"action": "view"}
        await websocket.send(json.dumps(view_message))
        response = await websocket.recv()
        print(f"Itens no carrinho: {response}")

        # Remover um item do carrinho
        remove_message = {
            "action": "remove",
            "comida_id": comida_id
        }
        await websocket.send(json.dumps(remove_message))
        response = await websocket.recv()
        print(f"Resposta ao remover: {response}")

asyncio.run(test_cart_consumer())
