# -*- coding: utf-8 -*-

import math
from PIL import Image
import random
import time
print(time.localtime())
RN = random.uniform
MIAN = math.isnan
MSN = math.sin
MPI = math.pi
MCS = math.cos
IMN = Image.new

class IFS(object):
    def __init__(self,Fn,Io):
        self.Fn = Fn
        self.Io = Io
        self.Inext = Io
    def __iter__(self):
        return self
    def next(self):
        if self.Fn:
            self.Inext = self.Fn(self.Inext)
        return self.Inext

def imgux(gray,fname):
    im = IMN('L',(len(gray[int(len(gray)/2)]),len(gray)))
    for c,i in enumerate(gray):
        for k,l in enumerate(i):
            if l == None:
                l= 0
            elif l > 255:
                l = 255
            elif l < 0:
                l = 0
            im.putpixel((c,k),l)
    im.save(open(fname,'wb'))

def imgux_ret(gray):
    im = IMN('L',(len(gray[int(len(gray)/2)]),len(gray)))
    for c,i in enumerate(gray):
        for k,l in enumerate(i):
            if l == None:
                l= 0
            elif l > 255:
                l = 255
            elif l < 0:
                l = 0
            im.putpixel((c,k),l)
    return im



def mandle5(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**5 + c
    except:
        j = complex(.0001,.0001)
    return [j,c]

def mandle4(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**4 + c
    except:
        j = complex(.0001,.0001)
    return [j,c]

def mandle6(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**6 + c
    except:
        j = complex(.0001,.0001)
    return [j,c]

def mandle7(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**7 + c
    except:
        j = complex(.0001,.0001)
    return [j,c]

def mandle8(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**8 + c
    except:
        j = complex(.0001,.0001)
    return [j,c]


mandle4_imag = [[0 for i in range(2048)] for j in range(2048)]
cathey_7 = [[0 for i in range(2048)] for j in range(2048)]
cathey_7div4 = [[0 for i in range(2048)] for j in range(2048)]
cathey_4minus4 = [[0 for i in range(2048)] for j in range(2048)]

for picnum in range(30):
    print(picnum,time.localtime(),end=',')
    for i in range(100):
        for j in range(100):
            rnum = complex(RN(-1.,1.),RN(-1.,1.))
            rnum2 = complex(RN(-1.,1.),RN(-1.,1.))
            mandle_not_IFS = IFS(mandle4,(rnum,rnum2))
            cathey_IFS = IFS(mandle6,(rnum,rnum2))
            for itercount in range(2048):
                cathey_nextnum = cathey_IFS.next()
                mandle4_nextnum = mandle_not_IFS.next()
                try:
                    cathey_4m7 =  mandle4_nextnum[0]-cathey_nextnum[0]
                except:
                    cathey_4m7 =  complex(.001,.001)
                if MIAN(cathey_4m7.real):
                    cathey_4m7 = complex(1.,cathey_4m7.imag)
                if MIAN(cathey_4m7.imag):
                    cathey_4m7 = complex(cathey_4m7.real,1.)
                if cathey_4m7.real > 1.:
                    cathey_4m7 = complex(1.,cathey_4m7.imag)
                elif cathey_4m7.real < -1.:
                    cathey_4m7 = complex(-1.,cathey_4m7.imag)
                if cathey_4m7.imag > 1.:
                    cathey_4m7 = complex(cathey_4m7.real,1.)
                elif cathey_4m7.imag < -1.:
                    cathey_4m7 = complex(cathey_4m7.real,-1)        
                
                if MIAN(mandle4_nextnum[0].real):
                    mandle4_nextnum[0] = complex(1.,mandle4_nextnum[0].imag)
                if MIAN(mandle4_nextnum[0].imag):
                    mandle4_nextnum[0] = complex(mandle4_nextnum[0].real,1.)
                if mandle4_nextnum[0].real > 1.:
                    mandle4_nextnum[0] = complex(1.,mandle4_nextnum[0].imag)
                elif mandle4_nextnum[0].real < -1.:
                    mandle4_nextnum[0] = complex(-1.,mandle4_nextnum[0].imag)
                if mandle4_nextnum[0].imag > 1.:
                    mandle4_nextnum[0] = complex(mandle4_nextnum[0].real,1.)
                elif mandle4_nextnum[0].imag < -1.:
                    mandle4_nextnum[0] = complex(mandle4_nextnum[0].real,-1)

                try:
                    cathey_7d4 = cathey_nextnum[0]/ mandle4_nextnum[0]
                except:
                    cathey_7d4 =  complex(.001,.001)
                if MIAN(cathey_7d4.real):
                    cathey_7d4 = complex(1.,cathey_7d4.imag)
                if MIAN(cathey_7d4.imag):
                    cathey_7d4 = complex(cathey_7d4.real,1.)
                if cathey_7d4.real > 1.:
                    cathey_7d4 = complex(1.,cathey_7d4.imag)
                elif cathey_7d4.real < -1.:
                    cathey_7d4 = complex(-1.,cathey_7d4.imag)
                if cathey_7d4.imag > 1.:
                    cathey_7d4 = complex(cathey_7d4.real,1.)
                elif cathey_7d4.imag < -1.:
                    cathey_7d4 = complex(cathey_7d4.real,-1)

                
                if cathey_nextnum[0].real > 1.:
                    cathey_nextnum[0] = complex(1.,cathey_nextnum[0].imag)
                elif cathey_nextnum[0].real < -1.:
                    cathey_nextnum[0] = complex(-1.,cathey_nextnum[0].imag)
                if cathey_nextnum[0].imag > 1.:
                    cathey_nextnum[0] = complex(cathey_nextnum[0].real,1.)
                elif cathey_nextnum[0].imag < -1.:
                    cathey_nextnum[0] = complex(cathey_nextnum[0].real,-1)
                
                cathey_4minus4[int(cathey_4m7.imag * 1024.)+ 1023][int(cathey_4m7.real * 1024.)+ 1023] += 10

                if cathey_4minus4[int(cathey_4m7.imag * 1024.)+ 1023][int(cathey_4m7.real * 1024.)+ 1023]  >255:
                    cathey_4minus4[int(cathey_4m7.imag * 1024.)+ 1023][int(cathey_4m7.real * 1024.+ 1023)]  = 128
                    
                cathey_7[int(cathey_nextnum[0].imag * 1024.)+ 1023][int(cathey_nextnum[0].real * 1024.)+ 1023] += 10
                if cathey_7[int(cathey_nextnum[0].imag * 1024.)+ 1023][int(cathey_nextnum[0].real * 1024.)+ 1023]  >255:
                    cathey_7[int(cathey_nextnum[0].imag * 1024.)+ 1023][int(cathey_nextnum[0].real * 1024.+ 1023)]  = 128
                    
                mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] += 10
                if mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)][int(mandle4_nextnum[0].real * 1024.)] >255:
                    mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] = 128
                    
                cathey_7div4[int(cathey_7d4.imag * 1024.)+ 1023][int(cathey_7d4.real * 1024.)+ 1023] += 10
                if cathey_7div4[int(cathey_7d4.imag * 1024.)+ 1023][int(cathey_7d4.real * 1024.)+ 1023] >255:
                    cathey_7div4[int(cathey_7d4.imag * 1024.)+ 1023][int(cathey_7d4.real * 1024.)+ 1023] = 128

    imgux(mandle4_imag,'/home/ttombbab/fiveplus/man_not4'+str(picnum)+'.png')
    imgux(cathey_4minus4,'/home/ttombbab/fiveplus/man_not4div7'+str(picnum)+'.png')
    imgux(cathey_7,'/home/ttombbab/fiveplus/man_not7'+str(picnum)+'.png')
    imgux(cathey_7div4,'/home/ttombbab/fiveplus/man_not4-7'+str(picnum)+'.png')
 

