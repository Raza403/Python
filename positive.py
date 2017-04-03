import cs50

def main():
    i = Getpositive()
    print ("{}".format (i))
    
def Getpositive():
    while True:
        n = cs50.get_int()
        if n >= 1:
            break
    return n
if __name__ == "__main__":
    main()