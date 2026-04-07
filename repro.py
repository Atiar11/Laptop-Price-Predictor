import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))
ndf = pickle.load(open('ndf.pkl', 'rb'))

# Sample query based on ndf's first row (omitting Price_euros)
# Company, TypeName, Inches, Ram, OpSys, Weight, Touchscreen, IPS, Processor, SSD, HDD, FlashStorage, Graphics, DisplayArea
query = np.array(['Apple', 'Ultrabook', 13.3, 8, 'Mac', 1.37, 0, 1, 'Intel Core i5', 128, 0, 0, 'Intel', 4096000])
query = query.reshape(1, 14)

try:
    prediction = np.exp(pipe.predict(query))
    print(f"Prediction success: {prediction}")
except Exception as e:
    import traceback
    traceback.print_exc()
