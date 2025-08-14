def main():
    try:
        a=int(input("enter a number"))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("hey am inside pf finally")

main()