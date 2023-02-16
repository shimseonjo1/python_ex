import glob,os

path = os.path.dirname(__file__)
result = glob.glob(path+'/01*.*')
print(result)