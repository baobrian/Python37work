from pydub import AudioSegment
import wave



# 操作函数
def get_wav_make(dataDir):
    f=wave.open(dataDir)
    rate = f.getframerate()
    frames = f.getnframes()
    sound = AudioSegment.from_wav(dataDir)
    duration = sound.duration_seconds * 1000  # 音频时长（ms）
    step=1
    for i in range(int(duration/3000)):
        begin = (i*3)*1000
        end = (i+1)*3*1000
        cut_wav = sound[begin:end]  # 以毫秒为单位截取[begin, end]区间的音频
        cut_wav.export('test_00'+str(step)+'.wav', format='wav')  # 存储新的wav文件
        step=step+1


def main():
    







if __name__ == '__main__':
    main()
    print('数据预处理加工完成')