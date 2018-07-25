from multiprocessing import cpu_count, Process
from redis import Redis
from rq import Worker

import tasks

def process():
    c = Redis(host=tasks.REDIS_HOST)
    w = Worker(['default'], connection=c)
    w.work()

if __name__ == '__main__':
    n = cpu_count()
    ps = []
    for i in range(n):
        p = Process(target=process, args=())
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
