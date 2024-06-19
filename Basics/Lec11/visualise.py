import librosa
import librosa.display # for plotting waveplot
import matplotlib.pyplot as plt
import numpy as np




def visualise_waveform(signal):
    print( type(signal), type(sr) )
    print( len(signal) ) #661794 -> sr * T => Totally for 30 units of time -> 30 * 22050 samples

    librosa.display.waveshow(y=signal, sr=SR) # Trap is librosa.display.<waveshow>( y, sr )
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Waveform")
    plt.savefig('waveform.png')
#   plt.show()

def visualise_spectrum(signal):
    fft = np.fft.fft(signal)
    print( fft.shape )
    print( fft[0] ) # (-39.499053955078054-7.460698725481052e-14j) complex value for a sample
    magnitude = abs( fft )
    frequency = np.linspace( 0, SR, len(magnitude) )
    plt.plot( frequency, magnitude )
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Spectrum")
    plt.savefig('power_spectrum.png')
    #   plt.show()

def visualise_spectrum_halved(signal):
    fft = np.fft.fft(signal)
    print( fft.shape )
    print( fft[0] ) # (-39.499053955078054-7.460698725481052e-14j) complex value for a sample
    magnitude = abs( fft )
    frequency = np.linspace( 0, SR, len(magnitude) )

    magnitude = magnitude[ : len(frequency)//2 ]
    frequency = frequency[ : len(frequency)//2 ]

    plt.plot( frequency, magnitude )
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Spectrum")
    #   plt.show()
    plt.savefig('power_spectrum_halved.png')


def visualise_spectrogram(signal, sr, hop_length=512, n_fft=2048):
    '''
    n_fft: In a given interval, number of samples to choose
    hop_length: strides to make / window_size
    '''
    stft = librosa.core.stft(signal, n_fft=n_fft, hop_length=hop_length)
    spectrogram = np.abs(stft)

    # librosa.display.specshow(spectrogram, hop_length=hop_length, sr=sr) # seeing in linear-scale
    # Better way is viz in log-scale

    log_spectrogram = librosa.amplitude_to_db(spectrogram) # converting to decibels is log_spectrogram
    librosa.display.specshow(log_spectrogram, hop_length=hop_length, sr=sr) # seeing in linear-scale

    
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar() # for magnitude as heatwave
    plt.title("Log_Spectrogram")

    # Onservation: Initial window, let's fix that
    # we can see, smaller freq contribute more as the orange color-coding
    # And higher freq, contribute less, hence bluish 
    plt.savefig("log_spectrogram.png")


def visualise_mfcc(signal, sr, hop_length=512, n_fft=2048, n_mfcc=13):
    '''
        n_mfcc: number of coefficients in mfcc
    '''
    mfcc = librosa.feature.mfcc(y=signal, 
                                sr = sr,
                                hop_length=hop_length, 
                                n_fft=n_fft, 
                                n_mfcc=n_mfcc)
    
    librosa.display.specshow(mfcc, hop_length=hop_length, sr=sr) # seeing in linear-scale

    
    plt.xlabel("Time")
    plt.ylabel("MFCCs")
    plt.colorbar() # for magnitude as heatwave, magnitude of mfcc
    plt.title("MFCC")

    # Onservation: Initial window, let's fix that
    # we can see, smaller freq contribute more as the orange color-coding
    # And higher freq, contribute less, hence bluish 
    plt.savefig("MFCC_plot.png")




if __name__ == "__main__":
    SR = 22050 # sample rate is followed regularly
    filename = "./blues.00000.wav"
    signal, sr = librosa.load(filename, sr = SR)
    # visualise_waveform(signal)
    # visualise_spectrum(signal)
    # visualise_spectrum_halved(signal)
    # visualise_spectrogram(signal, sr = SR)

    visualise_mfcc(signal, sr=SR)