import pandas as pd
import numpy as np


def randn_sample_withoutreturn(data_list,ratio=0.25):
    # 对一个list进行无放回的抽样
    # 返回抽样出来的list2和剩下的list1
    from sklearn.model_selection import train_test_split
    df = pd.DataFrame(data=data_list, columns=['value'])
    X_train, X_test, y_train, y_test = train_test_split(df.values, df.index, test_size=ratio)
    list1 = X_train.reshape(-1).tolist()
    list2 = X_test.reshape(-1).tolist()
    return list1,list2

if __name__ == '__main__':
    a = list('123456789')
    x1,x2=randn_sample_withoutreturn(data_list=a,ratio=0.05)
    print(x1)
    print(x2)