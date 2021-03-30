# Observer Pattern

class JobPost():
    def __init__(self, title: str) -> None:
        self._title = title

    def get_title(self):
        return self._title


class JobSeeker():
    def __init__(self, name: str) -> None:
        self._name = name

    def on_job_poster(self, job: JobPost):
        print(f'Hi {self._name}! New job posted: {job.get_title()}')


class EmploymentAgency():
    def __init__(self) -> None:
        self._observers: list[JobSeeker] = []

    def notify(self, job_posting: JobPost):
        for observer in self._observers:
            observer.on_job_poster(job_posting)

    def attach(self, observer: JobSeeker):
        self._observers.append(observer)

    def add_job(self, job_posting: JobPost):
        self.notify(job_posting)


# Create subscribers
johnDoe = JobSeeker('John Doe')
janeDoe = JobSeeker('Jane Doe')

# Create publisher and attach subscribers
job_postings = EmploymentAgency()
job_postings.attach(johnDoe)
job_postings.attach(janeDoe)

# Add a job and see if subscribers get notified
job_postings.add_job(JobPost('Software Engineer'))
