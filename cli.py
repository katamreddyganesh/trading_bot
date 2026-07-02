import typer
from bot.client import get_client
from bot.orders import place_order
from bot.orders import get_open_orders, cancel_order
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()


@app.command()
def trade(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    client = get_client()
    try:
        print(symbol, order_type, side, quantity)
        response = place_order(client, symbol, side, order_type, quantity, price)
        print("Order Response:", response)
        logger.info(f"TRADE: {symbol} {side} {order_type} {quantity} -> {response}")
    except Exception as e:
        print("Error:", e)
        logger.error(f"TRADE ERROR: {e}")


@app.command()
def open_orders(symbol: str = None):
    client = get_client()
    try:
        response = get_open_orders(client, symbol)
        print("Open Orders:", response)
        logger.info(f"OPEN ORDERS: {symbol} -> {response}")
    except Exception as e:
        print("Error:", e)
        logger.error(f"OPEN ORDERS ERROR: {e}")


@app.command()
def cancel(symbol: str, order_id: int):
    client = get_client()
    try:
        response = cancel_order(client, symbol, order_id)
        print("Cancel Response:", response)
        logger.info(f"Cancel Response: {symbol} -> {response}")
    except Exception as e:
        print("Error:", e)
        logger.error(f"CANCEL Response ERROR: {e}")


if __name__ == "__main__":
    app()
