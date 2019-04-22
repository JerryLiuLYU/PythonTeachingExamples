"""
简单的块加密程序
By JerryLiu
20190418
"""

import random

def makeMatrix():
    """构造加密矩阵，为一个列表的列表"""
    listOfChars = []
    for ascii in range(32, 128):
        listOfChars.append(chr(ascii))
    #print(listOfChars)
    random.shuffle(listOfChars)
    #print(listOfChars)
    matrix = []
    i = 0
    for row in range(8):
        matrix.append([])
        for column in range(12):
            matrix[row].append(listOfChars[row*12+column])
    return matrix
def printMatrix(matrix):
    '''打印加密矩阵'''
    for row in range(8):
        for column in range(12):
            print(matrix[row][column],end=' ')
        print()
def findCharInMatrix(matrix, targetChar):
    '''查找某个字符在加密矩阵中的位置，如果找不到返回none'''
    for row in range(8):
        for column in range(12):
            if matrix[row][column] == targetChar:
                return row,column
    return None


def encrypt(plainText, matrix):
    """使用matrix加密原始文本plainText,返回值为加密后的文本"""
    cypherText = ""
    limit = len(plainText)
    # 判断是否为奇数个字符，如果是，则最后一位无需加密处理
    if limit % 2 == 1:
        limit -= 1
    # Use the matrix to encrypt pairs of characters
    i = 0
    while i < limit:
        cypherText += encryptPair(plainText, i, matrix)
        i += 2
    # 如果是奇数个字符，则将最后一位直接附加在最后即可
    if limit < len(plainText):
        cypherText += plainText[limit]
    return cypherText

def decrypt(cipherText, matrix):
    """解密函数，同加密算法一样"""
    return encrypt(cipherText, matrix)

def encryptPair(plainText, i, matrix):
    """加密一对字符，对原始字符串中的下标为i和i+1的字符进行加密"""
    afterChar1=''
    afterChar2=''
    (row1, col1) = findCharInMatrix(matrix,plainText[i])
    (row2, col2) = findCharInMatrix(matrix, plainText[i + 1])
    # 如果在同一行或同一列，则直接互换位置即可，否则进行对角线互换
    if row1 == row2 or col1 == col2:
        afterChar1 = plainText[i + 1]
        afterChar2 = plainText[i]
    else:
        afterChar1 = matrix[row2][col1]
        afterChar2 = matrix[row1][col2]
    return afterChar1+afterChar2

def main(plainText = None):
    if not plainText:
        plainText = input("请输入加密文本： ")
    matrix = makeMatrix()
    print("加密矩阵为: ")
    printMatrix(matrix)
    cipherText = encrypt(plainText, matrix)
    print("加密中 . . .\n",
        "原始文本: " + plainText,
        "\n加密文本: " + cipherText)
    oldText = decrypt(cipherText, matrix)
    print("解密中 . . .\n",
           "加密文本: " + cipherText,
           "\n原始文本: " + oldText)
              

if __name__ == "__main__":
    main()
    
            
