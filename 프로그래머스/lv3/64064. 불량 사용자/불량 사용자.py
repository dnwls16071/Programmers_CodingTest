import re

def solution(user_id, banned_id):
    def is_match(user, ban):
        return re.match("^" + ban.replace("*", "[a-z0-9]") + "$", user) is not None
    
    candidates = []
    for ban in banned_id:
        matches = [user for user in user_id if is_match(user, ban)]
        candidates.append(matches)
    
    def backtrack(index, selected):
        if index == len(candidates):
            result.add(tuple(sorted(selected)))
            return
        
        for user in candidates[index]:
            if user not in selected:
                selected.add(user)
                backtrack(index + 1, selected)
                selected.remove(user)
    
    result = set()
    backtrack(0, set())
    
    return len(result)
