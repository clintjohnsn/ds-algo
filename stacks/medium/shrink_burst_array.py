# Reduce the string by removing K consecutive identical characters

# Input: K = 3, str = “qddxxxd” 
# Output: q 
# qddxxxd -> qddd -> q
# burst (k) = 3
# i/p - "abbccdddddccbddef"
# o/p - "addef"

class Node:
    def __init__(self,v,f):
        self.v = v
        self.f = f

def shrink(st,burst):
    S = []
    for c in st:
        if not S:
            S.append(Node(c,1))
        else:
            if S[-1].v == c:
                S[-1].f +=1
            else:
                if S[-1].f >=burst:
                    S.pop()
                if S[-1].v == c:
                    S[-1].f +=1
                else:
                    S.append(Node(c,1))
    return "".join([node.v * node.f for node in S])

        
def push(S,c,burst):
    if not S:
        S.append(Node(c,1))
    else:
        if S[-1].v == c:
            S[-1].f +=1
        else:
            if S[-1].f >=burst:
                S.pop()
                push(S,c,burst)
            else:
                S.append(Node(c,1))



def shrink2(st,burst):
    S = []
    for c in st:
        push(S,c,burst)
    return "".join([node.v * node.f for node in S])


s = "abbccdddddccbddef"
burst = 3
print(shrink2(s,burst))