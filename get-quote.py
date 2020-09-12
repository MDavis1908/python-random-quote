import random

def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #newLine = open("quotes.txt", 'a')
  #newLine.write("This is a new Quote")
  last = len(quotes) -1
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
