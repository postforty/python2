buffer_size = 1024
file_path = r'C:\Users\ITPS\Desktop\python2\section19\Figure_1.png'
with open(file_path, 'rb') as src:
    with open(r'C:\Users\ITPS\Desktop\python2\section14\new_chart.png', 'wb') as copy:
        while True:
            buffer = src.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
