# coding=utf-8
import pandas as pd
from pathlib import Path
import numpy as np
import shutil
import os

class SeparateAudio:
    '''
     创建该类是提取出同一身份证号的多个音频文件，分别作为提款首次录音和复提录音
    '''

    def __init__(self,root_audio_dir=None,\
                 target_first_audio_dir=None, \
                 target_second_audio_dir=None
                 ):
        self.root_audio_dir=root_audio_dir
        self.target_first_audio_dir = target_first_audio_dir
        self.target_second_audio_dir = target_second_audio_dir

    def separatefromaudio(self,audio_dir=None):
        '''
        遍历给定的根目录文件夹，查找对应的文件后缀的所有文件
        :return:
        '''
        if audio_dir is None:
            audio_dir=self.root_audio_dir
        p=Path(audio_dir)
        audiofile_lists=list(p.rglob('*.wav'))
        audiofile_df=pd.DataFrame(data=audiofile_lists,columns=['path'])
        audiofile_df['file_name']=audiofile_df['path'].map(lambda x:Path(x).stem)
        audiofile_df['id_no']=audiofile_df['file_name'].map(lambda x:str(x)[0:18])
        audiofile_df['rank'] = np.arange(0, audiofile_df.shape[0])
        # audiofile_df.set_index(['rank'], inplace=True)
        audiofile_df['row_number']=audiofile_df.groupby(['id_no'])['rank'].rank(ascending=False,method='first')
        first_dir=audiofile_df[(audiofile_df['row_number']==1)]
        second_dir = audiofile_df[(audiofile_df['row_number'] == 2)]
        print('首次完成音频采集的录音共{0}条'.format(sum(audiofile_df['row_number'] == 1)))
        print('第二次完成音频采集的录音共{0}条'.format(sum(audiofile_df['row_number'] == 2)))
        first_dir['path'].map(lambda x:shutil.copy(str(x),self.target_first_audio_dir))
        print('目录{0}音频文件已拷贝完成'.format(self.target_first_audio_dir))
        second_dir['path'].map(lambda x: shutil.copy(str(x), self.target_second_audio_dir))
        print('目录{0}音频文件已拷贝完成'.format(self.target_second_audio_dir))
        print('音频已区分完成')
        return





if __name__ == '__main__':
    root_audio_dir='E:\Data_temp\\records\\20200609\zhuxuechao\\audio\\'
    target_first_dir='E:\Data_temp\\records\\20200609\zhuxuechao\\firstaudio'
    target_second_dir = 'E:\Data_temp\\records\\20200609\zhuxuechao\\secondaudio'
    for v_path in [target_first_dir,target_second_dir]:
        if  not Path(v_path).exists():
            Path(v_path).mkdir()
        else:
            shutil.rmtree(v_path)
            Path(v_path).mkdir()
    spa=SeparateAudio(root_audio_dir=root_audio_dir,\
                      target_first_audio_dir=target_first_dir,\
                      target_second_audio_dir=target_second_dir)
    spa.separatefromaudio()
    pass
