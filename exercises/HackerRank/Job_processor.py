import heapq


class JobProcessor:

    def __init__(self):
        self.jobs = []
        self.arrival_id = 0

    def add_job(self, job_id, priority, description):
        self.arrival_id += 1
        heapq.heappush(self.jobs, (priority, self.arrival_id, job_id, description))

    def get_next_job(self):
        if not self.jobs:
            return None

        priority, arrival_id, job_id, description = heapq.heappop(self.jobs)
        return priority, job_id, description

    def get_job_count(self):
        return len(self.jobs)

    def get_next_jobs(self, n):
        if not isinstance(n, int):
            raise TypeError("Input Integer for n")

        if n <= 0:
            raise ValueError("n is not valid")

        if n > self.get_job_count():
            n = self.get_job_count()

        next_jobs = []
        copied_jobs = self.jobs.copy()
        for x in range(n):
            priority, arrival_id, job_id, description = heapq.heappop(copied_jobs)
            next_jobs.append((priority, job_id, description))

        return next_jobs

    def cancel_job(self, job_id):

        if not isinstance(job_id, str):
            raise TypeError("Input needs to be a string")
        #Assumption that all job id start with job
        if job_id[0:3] != "Job":
            raise ValueError("Is not a Job ID")

        new_stack = []
        job_deleted = False

        for job in self.jobs:
            if job[2] != job_id:
                new_stack.append(job)

            else:
                job_deleted = True

        heapq.heapify(new_stack)
        self.jobs = new_stack
        return job_deleted