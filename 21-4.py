# n=5 
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print() 

transactions = [
    {"tx_id": "0xabc123", "type": "receive", "amount": 150.0, "token": "USDT", "from": "0x1a2b3c", "to": "my_wallet"},
    {"tx_id": "0xdef456", "type": "send", "amount": 40.0, "token": "USDT", "from": "my_wallet", "to": "0x9f8e7d"},
    {"tx_id": "0xghi789", "type": "receive", "amount": 0.02, "token": "ETH", "from": "0xaaaaaa", "to": "my_wallet"},
    {"tx_id": "0xjkl012", "type": "send", "amount": 0.01, "token": "ETH", "from": "my_wallet", "to": "0xbbbbbb"},
    {"tx_id": "0xzzz999", "type": "receive", "amount": 100.0, "token": "USDC", "from": "0xcccccc", "to": "my_wallet"},
]
# Hiển thị danh sách giao dịch

for tx in transactions:
    print(tx['tx_id'])

#---------------------------
# Số dư token mỗi loại

# balances = {}

# for tx in transactions:
#     token = tx["token"]
#     amount = tx["amount"]
#     if token not in balances:
#         balances[token] = 0.0
#     if tx["type"] == "receive":
#         balances[token] += amount
#     elif tx["type"] == "send":
#         balances[token] -= amount

# print("Số dư token:")
# for token, balance in balances.items():
#     print(f"{token}: {balance}")

#-----------------------------------
# Giao dịch có lời

# threshold = float(input("Nhập ngưỡng giá trị: "))
# print(f"Các giao dịch có giá trị lớn hơn {threshold}:")
# for tx in transactions:
#     if tx["amount"] > threshold:
#         print(tx)

#---------------------------------------
# Đếm số giao dịch
# send_count = 0
# receive_count = 0

# for tx in transactions:
#     if tx["type"] == "send":
#         send_count += 1
#     elif tx["type"] == "receive":
#         receive_count += 1

# print(f"Số gd gửi (send): {send_count}")
# print(f"Số gd nhận (receive): {receive_count}")
