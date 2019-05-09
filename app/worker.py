from hotqueue import HotQueue
import datetime
import redis
import uuid

host = 'localhost'
port = 6379

rd = redis.StrictRedis(host=host, port=port, db=0)
queue = HotQueue("myqueue", host=host, port=port, db=0)

def generate_jid():
    return str(uuid.uuid4())

def generate_job_key(jid):
    return 'job.{}'.format(jid)

def get_job_by_id(jid):
    return rd.hgetall(generate_job_key(jid))

def get_all():
    for key in r.scan_iter("user:*"):
        print(r.hgetall(key))

def update_job(jid, new_status='complete'):
    job = get_job_by_id(jid)
    job['status'] = new_status
    rd.hmset(generate_job_key(jid), job)

def work(jid):
    key = generate_job_key(jid)
    queue.dequeue(key)
    dict = rd.hgetall(key)
    return dict['command']

def instantiate_job(jid, command, status):
    return {'id': jid,
            'status': status,
            'start_time': datetime.datetime.now(),
            'command': command }

@queue.worker
def say_hi(str):
    print(str)

def add_new_job(command, status='incomplete'):
    jid = generate_jid()
    job_dict = instantiate_job(jid, command, status)
    key = generate_job_key(jid)
    queue.put(key)
    rd.hmset(key, job_dict)
    return job_dict
