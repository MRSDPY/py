class My:

    top = 0

    s = []
        
    def push(self, v):
        top = top + 1
        s[top] = v
            
    def pop(self):
        if top == 0:
           return 0
        else:
            temp = s[top]
            top = top - 1
        return temp


x = My()
x.push(3)
ans = x.pop()

print(ans)
