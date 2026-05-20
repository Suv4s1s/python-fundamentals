#use of *args and **kwargs 

def cheese_shop(kind, *args, **kwargs):
    print(f"Do you have any {kind}?")
    print(f"I'm sorry , we're out of all {kind}")

    for arg in args:
        print(arg) 

    print("-"*40)

    for kw in kwargs:
        print(kw, ":", kwargs[kw])

    def main():
        cheese_shop("Limburger","It's very runny, sir",
        "It's very really runny sir",
        shop_keeper = "Michael Palin",
        client="John Cleese",
        sketch= "Cheese Shop")

    if __name__ == "__main__":
        main()

    def add(*args):
        sum=0
        for arg in args:
            sum=sum+arg
        return sum
    print(add(1,2,3,4,5,6))   
    