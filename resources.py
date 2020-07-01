def calc(*params):
    sum=0
    for i in params:
        sum+=i
    return sum



def main():
    sum = calc(1,2,3,4)
    print(sum)

if __name__ == "__main__":
    main()