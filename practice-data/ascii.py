def main():
    ascii(65)
    ascii(97)
    
def ascii(n):
    for i in range (n, n+26):
        print ("{} is {}".format(chr(i) , i))
if __name__ == "__main__":
    main()