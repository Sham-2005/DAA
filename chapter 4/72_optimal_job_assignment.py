def minimum_time_required(jobs, k):
    jobs.sort(reverse=True)
    workers = [0] * k
    min_max_time = [float('inf')]
    def dfs(job_idx):
        if job_idx == len(jobs):
            min_max_time[0] = min(min_max_time[0], max(workers))
            return
        if max(workers) >= min_max_time[0]:
            return
        seen_times = set()
        for i in range(k):
            if workers[i] in seen_times:
                continue
            seen_times.add(workers[i])
            workers[i] += jobs[job_idx]
            dfs(job_idx + 1)
            workers[i] -= jobs[job_idx]
            if workers[i] == 0:
                break
    dfs(0)
    return min_max_time[0]
print(f"Job Assignment Ex 1: {minimum_time_required([3,2,3], 3)}")       
print(f"Job Assignment Ex 2: {minimum_time_required([1,2,4,7,8], 2)}")   