try:
    a = 8/0
    str = a
except ZeroDivisionError as error:
    print("Zero Division Error")
except Exception as error: #any error
    print("Other Error")
