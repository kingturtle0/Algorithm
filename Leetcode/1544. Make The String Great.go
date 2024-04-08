func isBad(x, y byte) bool {
    if x > y {
        return x - y == 32
    }
    return y - x == 32
}

func makeGood(s string) string {
    if len(s) == 0 {
        return ""
    } else if len(s) == 1 {
        return s
    } else {
        stack := make([]byte, 0, len(s))
        stack = append(stack, s[0])
        for i:= 1; i < len(s); i++ {
            if len(stack) > 0 && isBad(stack[len(stack) - 1], s[i]) {
                stack = stack[:len(stack) - 1]
            } else {
                stack = append(stack, s[i])
            }
        }
        return string(stack)
    }
}
