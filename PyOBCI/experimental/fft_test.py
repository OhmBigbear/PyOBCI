from open_bci import *
import numpy as np
import numpy.fft as fft


def handle_sample(sample):
  #print(sample.channels)
  data = np.array(sample.channels)
  #print(data)
  spectrum = fft.fft(data)
  print(spectrum)


board = OpenBCIBoard()
board.print_register_settings()
board.start(handle_sample)

