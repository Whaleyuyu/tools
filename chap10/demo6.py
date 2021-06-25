# AUTHOR : 温幸文
# TIME : 2021/5/27  下午5:05
while True:
    n1 = input("请输入被除数：")
    n2 = input("请输入除数：")
    if n1 == 'exit' or n2 == 'exit':
        print('程序结束')
        break
    try:
        result = int(n1) / int(n2)
        print(result)
    except ZeroDivisionError:
        print('对不起，除数不能为0')
    except ValueError:
        print('对不起，只能输入数字')
