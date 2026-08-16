# Copyright (c) 2020 Oxia. All rights reserved.
"""
单线程安全，多线程不安全

输入示例：
bank_data_path = '/Users/Oxia/Downloads/bank_demo.csv'
```
id,user_id,transfer_to_user_id,amount,create_time
1,E,B,100,"2020-01-01 12:00:00"
2,A,B,100,"2020-01-01 12:10:00"
3,A,B,100,"2020-01-01 12:11:00"
4,B,X,100,"2020-01-01 12:12:00"
5,X,M,100,"2020-01-01 12:13:00"
6,X,Y,100,"2020-01-01 12:14:00"
7,M,Y,100,"2020-01-01 12:15:00"
8,M,Z,100,"2020-01-01 12:16:00"
9,Z,A,100,"2020-01-01 12:16:00"
10,B,C,100,"2020-01-01 12:04:00"
11,C,Y,100,"2020-01-01 12:07:00"
12,C,D,100,"2020-01-01 12:12:00"
```

输出示例:
000000000001 None ['E', 1, 'B', 10, 'C', 11, 'Y']
000000000002 None ['A', 2, 'B', 4, 'X', 5, 'M', 7, 'Y']
000000000003 000000000002 ['A', 3, 'B', 4, 'X', 5, 'M', 7, 'Y']
000000000004 000000000001 ['E', 1, 'B', 4, 'X', 5, 'M', 7, 'Y']
000000000005 000000000001 ['E', 1, 'B', 10, 'C', 12, 'D']
000000000006 000000000002 ['A', 2, 'B', 4, 'X', 6, 'Y']
000000000007 000000000003 ['A', 3, 'B', 4, 'X', 6, 'Y']
000000000008 000000000004 ['E', 1, 'B', 4, 'X', 6, 'Y']
000000000009 000000000002 ['A', 2, 'B', 4, 'X', 5, 'M', 8, 'Z', 9, 'A']
000000000010 000000000003 ['A', 3, 'B', 4, 'X', 5, 'M', 8, 'Z', 9, 'A']
000000000011 000000000004 ['E', 1, 'B', 4, 'X', 5, 'M', 8, 'Z', 9, 'A']
"""

import pandas as pd
from datetime import datetime

# 全局唯一ID初始化
GLOBAL_UUID = 1


def ls_rindex(ls, val, start=None):
    """
    获取list中最后出现元素val的位置
    """
    if start is None:
        start = len(ls) -1
    for i in range(start, -1, -1):
        if ls[i] == val:
            return i


def get_increased_uuid():
    """
    生成全局唯一ID
    """
    global GLOBAL_UUID
    result = '{:012d}'.format(GLOBAL_UUID)
    GLOBAL_UUID += 1
    return result

class FinancialChain(object):
    """
    资金转移链对象
    :param parent_uuid: 表明该链条是从何处copy而来
    :param uuid: 该链条自身全局唯一标识
    :param joiner: 参与该链条资金转移的账户
    :param chain: 资金转移链详情, i.e, [A, 1, B, 2, C,...]表示A先给B转账，账单ID=1，之后B给C转账，账单ID=2
    """
    def __init__(self, parent_uuid=None):
        self.parent_uuid = parent_uuid
        self.uuid = get_increased_uuid()
        self.joiner = set()
        self.chain = []

    def rebuild_from_chain(self, chain, parent_uuid=None):
        """
        从给定的chain信息中重新构建出该资金链的joiner和chain
        """
        if parent_uuid:
            self.parent_uuid = parent_uuid

        joiner = set()
        for i in range(0, len(chain), 2):
            joiner.add(chain[i])

        self.joiner = joiner
        self.chain = chain
        return self

    def init(self, id, user_id, transfer_to_user_id):
        """
        初始化链条的第一个记录
        """
        if self.joiner or self.chain:
            raise Exception('该链条已被初始化过')

        self.chain = [user_id, id, transfer_to_user_id]
        self.joiner = {user_id, transfer_to_user_id}
        return self


    def insert(self, id, user_id, transfer_to_user_id):
        """
        插入一条新的资金转记录(user_id, id, transfer_to_user_id)到该资金链
        1).如果该转账发起人不在已记录的参与者中，则抛出异常
        2).否则，检查该转账记录是否自然顺位的账单，如果是，则直接添加记录; 否则
        3).从该链中中找到该转账人最后一次的转账记录，拷贝该链所寻找的前半部分，将新的记录添加进去，形成一条新链
        """
        if user_id not in self.joiner:
            raise Exception(f'转账发起人不在该链的参与中:({user_id}, {id}, {transfer_to_user_id})')

        if user_id == self.chain[-1]:
            self.chain.extend([id, transfer_to_user_id])
            self.joiner.add(user_id)
            self.joiner.add(transfer_to_user_id)
            return self
        else:
            index = ls_rindex(self.chain, user_id)
            chain_fk = self.chain[:index + 1]
            chain_fk.extend([id, transfer_to_user_id])
            return FinancialChain(parent_uuid=self.uuid).rebuild_from_chain(chain_fk)


def financial_chain_algorithms(bank_data_path):
    """
    1).读取账单记录，并按照时间从远到近排序，以便后续处理;
    2).处理每条转账记录，动态构建资金转移链
        (1).global_joiners用来判断新出现的转账者，此时需要新建一条资金转移链;
        (2).否则，不是新出现的转账者，必然可以添加到已存在的一条或多条资金转移链中.
    """
    bank_trade_rcd_df = pd.read_csv('/Users/yuanguo/Downloads/bank_demo.csv')
    bank_trade_rcd_df = bank_trade_rcd_df.sort_values(by=['create_time'])

    fchains = {}
    global_joiners = set()
    for row in bank_trade_rcd_df.itertuples():
        id, user_id, transfer_to_user_id = row.id, row.user_id, row.transfer_to_user_id
        if user_id not in global_joiners:
            fc = FinancialChain().init(id, user_id, transfer_to_user_id)
            fchains[fc.uuid] = fc
        else:
            new_fchains = []  # 每次迭代都可能产生新链
            for uuid, fc in fchains.items():
                if user_id in fc.joiner:
                    r_fc = fc.insert(id, user_id, transfer_to_user_id)
                    if uuid != r_fc.uuid:
                        new_fchains.append(r_fc)

            # 将新链添加到总链的记录中
            for fc in new_fchains:
                fchains[fc.uuid] = fc

        global_joiners |= {user_id, transfer_to_user_id}

    final_chains = list(fchains.values())
    final_chains.sort(key=lambda x: x.uuid)

    for fc in final_chains:
        print(fc.uuid, fc.parent_uuid, fc.chain)


def run(bank_data_path):
    financial_chain_algorithms(bank_data_path)


if __name__ == "__main__":
    run('/Users/Oxia/Downloads/bank_demo.csv')
