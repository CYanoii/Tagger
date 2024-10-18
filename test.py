# def divide(a, b):  
#     if b == 0:  
#         raise ZeroDivisionError("Cannot divide by zero")  
#     return a / b  
  
# def complex_calculation(a, b, c):  
#     try:   
#         result = divide(a, b)
#         print("after error")
#         return result * c 
#     except ZeroDivisionError as e:  
#         # 在这里不处理异常，让它继续传递
#         print("123")
#         raise
#     finally:
#         print("456")
    
    
  
# def main():  
#     try:  
#         # 调用 complex_calculation 函数  
#         result = complex_calculation(10, 0, 5)  
#         print(result)  
#     except ZeroDivisionError as e:  
#         # 在 main 函数中捕获并处理异常  
#         print("Caught a ZeroDivisionError:", e)  
  
# main()

# dic = {}
# dic[1]='123'
# dic[2]='234'

# if 1 not in dic:
#     print(1)
# if 3 not in dic:
#     print(3)

# def change(n):
#     print(id(n))
#     n = 1000
#     print(id(n))

# x = 3
# print(id(x))
# change(x)
# print(x)

def change(n):
    print(id(n))
    n.append(4)

x = [1, 2, 3]
print(id(x))
change(x)
print(x)