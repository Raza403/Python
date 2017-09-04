def main():
    cough(3)
    sneez(3)
def cough(n):
    say ("cough", 3)
def sneez(n):
    say("sneez" ,3)
def say(word,n):
    for i in range (n):
        print(word)
if __name__ == "__main__":
    main()