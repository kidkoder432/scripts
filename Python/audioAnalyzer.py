from scipy.io import wavfile
import winsound

def freq(file, start_time, end_time):
    sample_rate, data = wavfile.read(file)
    start_point = int(sample_rate * start_time / 1000)
    end_point = int(sample_rate * end_time / 1000)
    length = (end_time - start_time) / 1000
    counter = 0
    for i in range(start_point, end_point):
        if data[i] < 0 and data[i+1] > 0:
            counter += 1
    return [counter/length, counter, length]  
# def clip(n, min_, max_):
#     return max(min_, min(n, max_))
# def freq(f, tempo):
#     sr, data = wavfile.read(f)
#     dt = []
#     for i in range(len(data)):
#         dt.append(clip(data[i], -1000, 1000))
#     tempo = int((60 / tempo) * sr)
#     for i in range(int(len(data) / tempo)):
#         print(i)
#         count = 0
#         dmod = dt[i:i+tempo]
#         for d in dmod:
#             h = -10000
#             l = 10000
#             if d > h:
#                 h = d
#             if d < l:
#                 l = d

#         print(h, l, d)
#         for d in dmod:
#             if d == h:
#                 count += 1
#         print(count)


        
         
# freq('Python/scale.wav', 120)
print(freq('scale.wav', 0, 499), freq('scale.wav', 501, 999))