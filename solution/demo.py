from functools import partial


def _sum(inf):
    print("--->", inf)


# s = _sum(1, 2) + 100


a_100 = partial(_sum, 100)
print(a_100())


class CLSBase(object):
    def __init__(self, model):
        self.model = model

    def train(self, inputs):
        self._forward(inputs)

    def _forward(self, inputs):
        raise NotImplementedError


class HotTopicCLS(CLSBase):
    def _forward(self, inputs):
        print(self.model + ' ' + inputs)


from  multiprocessing import Pool
import os, time, random

def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    pool = Pool(5) #创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close()
    pool.join()
    print('结束测试')


if __name__ == '__main__1':
    keys = []
    with open('demo') as fp:
        for line in fp:
            key = line.strip().split('\t')[0]
            keys.append(key)

    print(','.join(keys))

    keys = '(id, policy_id, publish_date, publish_organization, digest_policy, superior_policy, forward_policy, ' \
           'deprecated_policy, official_organization, feature_policy, keywords, keywords_weight, background, ' \
           'main_content, other_content, hot_topic_policy, special_policy, policy_type, publish_policy_number, ' \
           'publish_region, superior_pub_policy_number, forward_pub_policy_number, deprecated_pub_policy_number)'

    insert_sql = f"insert into  {keys} values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    print(insert_sql)
