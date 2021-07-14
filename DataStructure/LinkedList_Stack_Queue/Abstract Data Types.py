'''
An abstract data type(ADT) is an abstraction of a data structure.

An ADT spcifies:
-Data stored
-Operations on the data
-Error conditionjs associated with operations

Example: ADT modeling a simple stock trading system
    -The data stored are buy/sell orders
    -The operations supported are
        -order buy(stock, shares, price)
        -order sell(stock, shares, price)
        -void cancel(order)
    -Error conditions:
        -Buy/Sell a nonexistent stock
        -Cancel a nonexistent order
'''