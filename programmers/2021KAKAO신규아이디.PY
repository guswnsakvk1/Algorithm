def solution(new_id):
    id = new_id.lower()
    dot_place = []
    for i in id:
        if not('a' <= i <= 'z' or '0' <= i <= '9' or i == '-' or i == '_' or i == '.'):
            id = id.replace(i,"")
    
    while '..' in id:
        id = id.replace("..", '.')
    
    if id[0] == '.':
        id = id[1:]
        
    if len(id) >= 1 and id[-1] == '.':
        id = id[:-1]
    
    if id == '':
        id = 'a'
    
    if len(id) > 15:
        id = id[:15]
        
    if id[-1] == '.':
        id = id[:-1]
        
    while len(id) < 3:
        id = id + id[-1]
    
    return id