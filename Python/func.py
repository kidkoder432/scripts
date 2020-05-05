import pyaudio
import math
def playTone( freq , length): 
    bit_rate = 16000 #number of frames per second/frameset.      
    frequency = freq #in Hz, waves per second
    play_time = length #in seconds to play sound
    if frequency > bit_rate:
        bit_rate = frequency+100
    num_frames = int(bit_rate * play_time)
    total_frames = num_frames % bit_rate
    wave_info = ''    
    for x in xrange(num_frames):
     wave_info = wave_info+chr(int(math.sin(x/((bit_rate/frequency)/math.pi))*127+128))    
    for x in xrange(total_frames): 
     wave_info = wave_info+chr(128)
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = bit_rate, 
                    output = True)
    stream.write(wave_info)
    stream.stop_stream()
    stream.close()
    p.terminate()
if __name__ == '__main__':
    frequency = 1500 #Hz
    duration = 2 #seconds
    PyAudio = pyaudio.PyAudio

    playTone(frequency , duration)
