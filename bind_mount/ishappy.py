def isHappy(n):
    history = set()
    while n != 1 and n not in history:
        history.add(n)
        # 지환님의 로직 유지
        a = 0
        while True:
            if 10**a <= n < 10**(a+1): break
            else: a += 1
        arr = []
        temp_n = n
        while a >= 0:
            digit = temp_n // (10**a)
            arr.append(digit)
            temp_n %= (10**a)
            a -= 1
        n = sum(x**2 for x in arr)
    return n == 1

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    # 반드시 이 경로로 저장해야 호스트에서 볼 수 있습니다 
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")
