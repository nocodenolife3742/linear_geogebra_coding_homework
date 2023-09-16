# 取得需要的數學常數
from math import pi, log10


# 定義 matrix (0-indexed)
class matrix:
    # 用 list 初始化 matrix 的元素
    def __init__(self, array=[]):
        # 用 list 建立 matrix 的 content，content 為實際儲存元素的地方
        self.content = array

    # 定義 matrix 如何被轉換成字串
    def __str__(self):
        # 將 content 轉為字串
        return str(self.content)

    # 定義 matrix 的相等
    def __eq__(self, other):
        # 檢查兩個 matrix 的長度是否相等，若不相等則回傳 False
        if len(self.content) != len(other.content):
            return False
        if len(self.content[0]) != len(other.content[0]):
            return False

        # 檢查兩個 matrix 的內容是否相等，若不相等則回傳 False
        column_count = len(self.content)
        row_count = len(self.content[0])
        for i in range(column_count):
            for j in range(row_count):
                if self.content[i][j] != other.content[i][j]:
                    return False

        # 若皆相等則回傳 True
        return True

    # 定義 matrix 的加法
    def __add__(self, other):
        # 將兩個 matrix 的所有元素相加，並回傳
        column_count = len(self.content)
        row_count = len(self.content[0])
        ret = matrix([[0 for _ in range(row_count)] for _ in range(column_count)])
        for i in range(column_count):
            for j in range(row_count):
                ret.content[i][j] = self.content[i][j] + other.content[i][j]
        return ret

    # 定義 matrix 的減法
    def __sub__(self, other):
        # 將兩個 matrix 的所有元素相減，並回傳
        column_count = len(self.content)
        row_count = len(self.content[0])
        ret = matrix([[0 for _ in range(row_count)] for _ in range(column_count)])
        for i in range(column_count):
            for j in range(row_count):
                ret.content[i][j] = self.content[i][j] - other.content[i][j]
        return ret

    # 定義 matrix 的純量乘法
    def scalar_multiply(self, scalar):
        # 將 matrix 的所有元素乘以 scalar，並回傳
        column_count = len(self.content)
        row_count = len(self.content[0])
        ret = matrix([[0 for _ in range(row_count)] for _ in range(column_count)])
        for i in range(column_count):
            for j in range(row_count):
                ret.content[i][j] = self.content[i][j] * scalar
        return ret

    # 定義 matrix 的乘法
    def __mul__(self, other):
        # 將兩個 matrix 的列行做內積，並回傳
        column_count = len(self.content)
        row_count = len(other.content[0])
        num_count = len(self.content[0])
        ret = matrix([[0 for _ in range(row_count)] for _ in range(column_count)])
        for i in range(column_count):
            for j in range(row_count):
                # 以下迴圈為內積
                for k in range(num_count):
                    ret.content[i][j] += self.content[i][k] * other.content[k][j]
        return ret

    # 找出 matrix 的轉置矩陣
    def transpose(self):
        # 設定轉置矩陣的長度
        column_count = len(self.content)
        row_count = len(self.content[0])
        ret = matrix([[0 for _ in range(column_count)] for _ in range(row_count)])

        # 轉置過程
        for i in range(column_count):
            for j in range(row_count):
                ret.content[j][i] = self.content[i][j]
        return ret

    # 找出 matrix 的反矩陣 (目前函數只能用於2*2矩陣)
    def inverse(self):
        # 算出矩陣的行列式值
        det = (
            self.content[0][0] * self.content[1][1]
            - self.content[0][1] * self.content[1][0]
        )

        # 算出矩陣的逆矩陣
        column_count = len(self.content)
        row_count = len(self.content[0])
        ret = matrix([[0 for _ in range(column_count)] for _ in range(row_count)])
        ret.content[0][0] = self.content[1][1]
        ret.content[0][1] = -self.content[0][1]
        ret.content[1][0] = -self.content[1][0]
        ret.content[1][1] = self.content[0][0]

        # 判斷矩陣是否為有反矩陣(檢查矩陣的行列式值是否為 0)
        try:
            ret = ret.scalar_multiply(1 / det)
            return ret
        except ZeroDivisionError:
            print("error : No inverse")

    # 判斷是否為對稱矩陣
    def is_symmetric(self):
        # 判斷矩陣本身是否與轉置矩陣相同
        return self == self.transpose()

    # 判斷是否為對角矩陣
    def is_diagonal(self):
        # 判斷矩陣非對角線上的元素是否為 0
        column_count = len(self.content)
        row_count = len(self.content[0])
        for i in range(column_count):
            for j in range(row_count):
                if i != j and self.content[i][j] != 0:
                    return False
        return True


# 定義 A, B, C, E, F, I
A = matrix([[2, -2], [3, -5]])
B = matrix([[-2, 0], [0, 3]])
C = matrix([[-1, 2, 0], [2, 0, 3]])
E = matrix([[2, -1], [pi, log10(2)], [-2, 3]])
F = matrix([[1, 2, 3], [2, 3, 4], [3, 5, 7]])
I = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
