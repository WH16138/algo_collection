import bisect

class MergeSortTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[] for _ in range(4*self.n)]
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = [data[start]]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = sorted(self.tree[node*2] + self.tree[node*2+1])

    def query_up(self, l, r, val, node=1, start=0, end=None): # count of elements > val
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            idx = bisect.bisect_right(self.tree[node], val)
            return len(self.tree[node]) - idx
        
        mid = (start + end) // 2
        left = self.query_up(l, r, node*2, start, mid)
        right = self.query_up(l, r, node*2+1, mid+1, end)
        return left + right
    
    def query_down(self, l, r, val, node=1, start=0, end=None): # count of elements < val
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            idx = bisect.bisect_left(self.tree[node], val)
            return idx
        
        mid = (start + end) // 2
        left = self.query_down(l, r, val, node*2, start, mid)
        right = self.query_down(l, r, val, node*2+1, mid+1, end)
        return left + right
    
    def query(self, l, r, val, node=1, start=0, end=None): # count of elements == val
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            idx_left = bisect.bisect_left(self.tree[node], val)
            idx_right = bisect.bisect_right(self.tree[node], val)
            return idx_right - idx_left
        
        mid = (start + end) // 2
        left = self.query(l, r, val, node*2, start, mid)
        right = self.query(l, r, val, node*2+1, mid+1, end)
        return left + right

# e.g.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = MergeSortTree(arr)

print(st.query(0, 3, 4))  # count of elements == 4 in range [0, 3] -> 1
print(st.query_up(0, 3, 4))  # count of elements > 4 in range [0, 3] -> 0
print(st.query_down(0, 3, 4))  # count of elements < 4 in range [0, 3] -> 3 (1, 2, 3)