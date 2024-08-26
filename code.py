#範例一
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """將元素推入堆疊"""
        self.stack.append(value)

    def pop(self):
        """從堆疊彈出元素"""
        return self.stack.pop()

    def decimal_to_base(self, decimal_number, base):
        """將十進制數字轉換為指定進制"""
        if decimal_number < 0:
            raise ValueError("Negative numbers are not supported")

        if base < 2 or base > 16:
            raise ValueError("Base must be between 2 and 16")

        # 特殊情況處理：十進制數字為0
        if decimal_number == 0:
            return "0"

        # 清空堆疊
        self.stack = []

        # 定義進制字符集
        digits = "0123456789ABCDEF"

        # 將十進制數字轉換為指定進制，並將結果推入堆疊
        while decimal_number > 0:
            remainder = decimal_number % base
            self.push(digits[remainder])
            decimal_number = decimal_number // base

        # 從堆疊中構建進制表示
        base_number = ''
        while self.stack:
            base_number += self.pop()

        return base_number

# 創建 Stack 類的實例
stack = Stack()

# 設定十進制數字
decimal_number = 45

#範例二
binary_number = stack.decimal_to_base(decimal_number, 2)
print(f"Binary: {binary_number}")  # 輸出: Binary: 101101

#範例三
octal_number = stack.decimal_to_base(decimal_number, 8)
print(f"Octal: {octal_number}")  # 輸出: Octal: 55
