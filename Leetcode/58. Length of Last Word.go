func lengthOfLastWord(s string) int {
	answer := 0
	flag := false
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] != 32 {
			answer++
			flag = true
		} else {
			if flag {
				return answer
			}
		}
	}
    return answer
}
