def solution(info, query):
    answer = []
    for requirement in query:
        requirement = requirement.replace(" and", "")
        lang, job, career, food, score = requirement.split(" ")
        num = 0
        for job_seeker in info:
            job_seeker_lang, job_seeker_job, job_seeker_career, job_seeker_food, job_seeker_score = job_seeker.split()
            
            if lang != '-' and lang != job_seeker_lang:
                continue
                
            if job != '-' and job != job_seeker_job:
                continue
                
            if career != '-' and career != job_seeker_career:
                continue
                
            if food != '-' and food != job_seeker_food:
                continue
                
            if score != '-' and int(score) > int(job_seeker_score):
                continue
                
            num += 1
            
        answer.append(num)
        
    return answer