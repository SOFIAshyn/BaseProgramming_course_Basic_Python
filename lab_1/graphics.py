import matplotlib.pyplot as plt

def main():
    print ("This program inlustrate s a chaotic function")
    lst = []
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x  = 3.9 * x * (1 - x)
        lst.append(x)
        plt.figure(1)
        plt.legend(["truly Y", "truly X"])
        plt.plot(lst)
    print(lst)
    plt.show()

main()
