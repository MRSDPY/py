from math import inf as infinity

n = int(input("How Many Coin You Can Enter : "))
coins = [int(input()) for _ in range(n)]

amount = int(input("Enter The Amount : "))

def coin_get(c, amount):
  table = [[infinity for _ in range(amount+1)] for _ in range(len(c))]

  for i in range(len(c)):
    table[i][0] = 0

  for i in range(len(c)):
    for j in range(amount+1):
      if c[i] > j:
        table[i][j] = table[i-1][j]
      else:
        table[i][j] = min(table[i-1][j], 1+table[i][j - c[i]])

  print(f"For this amount {table[len(c)-1][amount]} coin required.")
  print("\n Table Are : ")
  for i in table:
  	print("\n ", i)


if __name__ == "__main__":
  coin_get(coins, amount)