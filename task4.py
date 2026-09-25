def counter(n):
    c={}
    for i in n:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    sorted_c = sorted(c.items(), key=lambda item: item[1], reverse=True)
    top_3 = sorted_c[:3]
    for char, count in top_3:
        print(f"{char}: {count}")
counter(input().lower())
