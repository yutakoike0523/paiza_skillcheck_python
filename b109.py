import heapq
s= list(map(int,input().split()))
N,H,W,p,q=s[0],s[1],s[2],s[3],s[4]

def find_best_seat(num_rows, num_cols, reserved_seats):
    reserved = set((r-1, c-1) for r, c in reserved_seats)
    
    heap = []

    for r in range(num_rows):
        for c in range(num_cols):

            if (r, c) in reserved:
                continue
            # (r,c)の座席の評価値を計算する
            value = abs(r - num_rows // 2) + abs(c - num_cols // 2)
            # ヒープに評価値と席の位置を追加する
            heapq.heappush(heap, (value, r, c))
    
    # 評価値が最小の席のリストを初期化する
    best_seats = []
    
    # 評価値が最小の席を探す
    while len(best_seats) < 3 and heap:
        _, r, c = heapq.heappop(heap)
        best_seats.append((r, c))
    
    # 最も映画を見やすい席を返す
    return [(r+1, c+1) for r, c in best_seats]

# 入力例1に対して実行してみる
num_rows = H
num_cols = N
reserved_seats =[]
for i in range(0,N):
    t= list(map(int,input().split()))
    y=(t[0],[1])
    reserved_seats.append(y)
print(find_best_seat(num_rows, num_cols, reserved_seats))