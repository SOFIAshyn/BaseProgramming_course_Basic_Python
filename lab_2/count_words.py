STRESSED_OUT = """I wish I found some better sounds no one's ever heard
I wish I had a better voice that sang some better words
I wish I found some chords in an order that is new
I wish I didn't have to rhyme every time I sang
I was told when I get older all my fears would shrink
But now I'm insecure and I care what people think
My name's Blurryface and I care what you think
My name's Blurryface and I care what you think
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
We're stressed out
Sometimes a certain smell will take me back to when I was young
How come I'm never able to identify where it's coming from
I'd make a candle out of it if I ever found it
Try to sell it, never sell out of it, I'd probably only sell one
It'd be to my brother, 'cause we have the same nose
Same clothes homegrown a stone's throw from a creek we used to roam
But it would remind us of when nothing really mattered
Out of student loans and tree-house homes we all would take the latter
My name's Blurryface and I care what you think
My name's Blurryface and I care what you think
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
We used to play pretend, give each other different names
We would build a rocket ship and then we'd fly it far away
Used to dream of outer space but now they're laughing at our face
Saying, "Wake up, you need to make money"
Yeah
We used to play pretend, give each other different names
We would build a rocket ship and then we'd fly it far away
Used to dream of outer space but now they're laughing at our face
Saying, "Wake up, you need to make money"
Yeah
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
Wish we could turn back time, to the good old days
When our momma sang us to sleep but now we're stressed out
Used to play pretend, used to play pretend, bunny
We used to play pretend, wake up, you need the money
Used to play pretend, used to play pretend, bunny
We used to play pretend, wake up, you need the money
We used to play pretend, give each other different names
We would build a rocket ship and then we'd fly it far away
Used to dream of outer space but now they're laughing at our face
Saying, "Wake up, you need to make money"
Yeah"""

def counter(song):
    words = STRESSED_OUT.lower().split()

    dict = {}
    #for i in range(len(words)) ітерація по індексах
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    lst = []
    for word in dict:
        lst.append([dict[word], word])

    lst.sort(reverse = True)
    return lst

print(counter(STRESSED_OUT))
# print(max(lst))

#прискорений оператор присвоєння x *= 2
