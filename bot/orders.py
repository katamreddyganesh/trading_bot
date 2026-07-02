def place_order(client, symbol, side, order_type, quantity, price=None):
    if order_type == "MARKET":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    elif order_type == "LIMIT":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

def get_open_orders(client, symbol=None):
    return client.futures_get_open_orders(symbol=symbol)

def cancel_order(client, symbol, order_id):
    return client.futures_cancel_order(symbol=symbol, orderId=order_id)

