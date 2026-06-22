from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit))
    starts = [job[0] for job in jobs]

    n = len(jobs)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        next_job = bisect_left(starts, jobs[i][1])

        take = jobs[i][2] + dp[next_job]
        skip = dp[i + 1]

        dp[i] = max(take, skip)

    return dp[0]