class Solution(object):
    def compress(self, chars):
        s = []
        ch_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                ch_count += 1
            else:
                s.append(chars[i - 1])
                if ch_count > 1:
                    num_list = [str(digit) for digit in str(ch_count)]
                    s += num_list
                ch_count = 1
        s.append(chars[-1])
        if ch_count > 1:
            num_list = [str(digit) for digit in str(ch_count)]
            s += num_list
        chars[:] = s
        return len(chars)

time optimized code
//class Solution(object):
    def compress(self, chars):
        write_idx = 0  # Index for writing compressed characters
        ch_count = 1   # Count of consecutive occurrences of the current character

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                ch_count += 1
            else:
                chars[write_idx] = chars[i - 1]
                write_idx += 1

                if ch_count > 1:
                    ch_count_str = str(ch_count)
                    for digit in ch_count_str:
                        chars[write_idx] = digit
                        write_idx += 1

                ch_count = 1

        chars[write_idx] = chars[-1]
        write_idx += 1

        if ch_count > 1:
            ch_count_str = str(ch_count)
            for digit in ch_count_str:
                chars[write_idx] = digit
                write_idx += 1

        return write_idx
