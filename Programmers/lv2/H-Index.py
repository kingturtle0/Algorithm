def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    else:
        return idx + 1