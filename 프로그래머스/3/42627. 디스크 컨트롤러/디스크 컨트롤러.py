import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])

    total_turnaround_time = 0  
    current_time = 0           
    job_idx = 0                
    completed_count = 0        
    

    wait_queue = []
    num_jobs = len(jobs)
    
    while completed_count < num_jobs:
        while job_idx < num_jobs and jobs[job_idx][0] <= current_time:
            request_time, execution_time = jobs[job_idx]
            heapq.heappush(wait_queue, (execution_time, request_time))
            job_idx += 1
            
        if wait_queue:
            execution_time, request_time = heapq.heappop(wait_queue)
            current_time += execution_time
            total_turnaround_time += (current_time - request_time)
            completed_count += 1
        else:
            current_time = jobs[job_idx][0]
            
    return total_turnaround_time // num_jobs
