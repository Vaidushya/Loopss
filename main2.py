text = input("enter a sentence :")
text = text.split()
print("The original string is ",str)
bigWordLen = 0

for wrd in text:
    wrdlen = len(wrd)
    if wrdlen>bigWordLen:
        bigWordLen=wrdlen

print("\nLargest word:")

for wrd in text:
    wrdlen = len(wrd)
    if wrdlen==bigWordLen:
        print(wrd)