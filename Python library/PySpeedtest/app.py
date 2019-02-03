import pyspeedtest


print(dir(pyspeedtest.SpeedTest))
st = pyspeedtest.SpeedTest()
ping = st.ping()
print(ping)

download = st.download()
print(download)

upload = st.upload()
print(upload)