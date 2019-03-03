def main():
    print ("This program inlustrate s a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x  = 3.9 * x * (1 - x)
        #3.9 * (x - x * x)
        #3.9 * x - 3.9 * x * x
        print (x)

main()

"""0.73125
0.76644140625
0.6981350104385375
0.8218958187902304
0.5708940191969317
0.9553987483642099
0.166186721954413
0.5404179120617926
0.9686289302998042
0.11850901017563877"""
