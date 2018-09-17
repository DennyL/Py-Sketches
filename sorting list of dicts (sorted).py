"""We are given a table with all available goods in the store. The data is represented as a list of dicts.
Example:
bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
])
The task is to find the TOP most expensive goods.
The amount we are looking for will be given as a first argument and the whole data as the second one.

Input: int and list of dicts. Each dict has two keys - "name" and "price"
Output: the same as the second Input argument.
"""


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]
    
