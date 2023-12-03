from typing import List


file_content = "abcdABCD1234"
file_pointer = 0


def read4(buf4):
    global file_pointer
    count = 0

    while count < 4 and file_pointer < len(file_content):
        buf4[count] = file_content[file_pointer]
        file_pointer += 1
        count += 1

    return count


class Solution:
    def read(self, buf, n):
        buf4 = [None, None, None, None]
        total = 0

        while total < n:
            count = read4(buf4)
            if count < 4:
                for i in range(count):
                    if total == n:
                        break
                    buf[total] = buf4[i]
                    total += 1
                return total

            for i in range(4):
                if total == n:
                    return total
                buf[total] = buf4[i]
                total += 1
        return total


sol = Solution()
n = 12
buf = [""] * n
read_chars = sol.read(buf, n)
print(f"Read {read_chars} characters: {''.join(buf)}")
