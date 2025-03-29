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
eligus_7 = [[0 for i in range(2048)] for j in range(2048)]
eligus_7div4 = [[0 for i in range(2048)] for j in range(2048)]
eligus_4minus4 = [[0 for i in range(2048)] for j in range(2048)]

for picnum in range(30):
    print(picnum,time.localtime(),end=',')
    for i in range(100):
        for j in range(100):
            rnum = complex(RN(-1.,1.),RN(-1.,1.))
            rnum2 = complex(RN(-1.,1.),RN(-1.,1.))
            mandle_not_IFS = IFS(mandle4,(rnum,rnum2))
            eligus_IFS = IFS(mandle7,(rnum,rnum2))
            for itercount in range(2048):
                eligus_nextnum = eligus_IFS.next()
                mandle4_nextnum = mandle_not_IFS.next()
                
                try:
                    eligus_4m7 =  mandle4_nextnum[0]-eligus_nextnum[0]
                except:
                    eligus_4m7 =  complex(.001,.001)
                if MIAN(eligus_4m7.real):
                    eligus_4m7 = complex(1.,eligus_4m7.imag)
                if MIAN(eligus_4m7.imag):
                    eligus_4m7 = complex(eligus_4m7.real,1.)
                if eligus_4m7.real > 1.:
                    eligus_4m7 = complex(1.,eligus_4m7.imag)
                elif eligus_4m7.real < -1.:
                    eligus_4m7 = complex(-1.,eligus_4m7.imag)
                if eligus_4m7.imag > 1.:
                    eligus_4m7 = complex(eligus_4m7.real,1.)
                elif eligus_4m7.imag < -1.:
                    eligus_4m7 = complex(eligus_4m7.real,-1)        
                
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
                    eligus_7d4 = eligus_nextnum[0]/ mandle4_nextnum[0]
                except:
                    eligus_7d4 =  complex(.001,.001)
                if MIAN(eligus_7d4.real):
                    eligus_7d4 = complex(1.,eligus_7d4.imag)
                if MIAN(eligus_7d4.imag):
                    eligus_7d4 = complex(eligus_7d4.real,1.)
                if eligus_7d4.real > 1.:
                    eligus_7d4 = complex(1.,eligus_7d4.imag)
                elif eligus_7d4.real < -1.:
                    eligus_7d4 = complex(-1.,eligus_7d4.imag)
                if eligus_7d4.imag > 1.:
                    eligus_7d4 = complex(eligus_7d4.real,1.)
                elif eligus_7d4.imag < -1.:
                    eligus_7d4 = complex(eligus_7d4.real,-1)

                
                if eligus_nextnum[0].real > 1.:
                    eligus_nextnum[0] = complex(1.,eligus_nextnum[0].imag)
                elif eligus_nextnum[0].real < -1.:
                    eligus_nextnum[0] = complex(-1.,eligus_nextnum[0].imag)
                if eligus_nextnum[0].imag > 1.:
                    eligus_nextnum[0] = complex(eligus_nextnum[0].real,1.)
                elif eligus_nextnum[0].imag < -1.:
                    eligus_nextnum[0] = complex(eligus_nextnum[0].real,-1)
                
                eligus_4minus4[int(eligus_4m7.imag * 1024.)+ 1023][int(eligus_4m7.real * 1024.)+ 1023] += 10

                if eligus_4minus4[int(eligus_4m7.imag * 1024.)+ 1023][int(eligus_4m7.real * 1024.)+ 1023]  >255:
                    eligus_4minus4[int(eligus_4m7.imag * 1024.)+ 1023][int(eligus_4m7.real * 1024.+ 1023)]  = 128
                    
                eligus_7[int(eligus_nextnum[0].imag * 1024.)+ 1023][int(eligus_nextnum[0].real * 1024.)+ 1023] += 10
                if eligus_7[int(eligus_nextnum[0].imag * 1024.)+ 1023][int(eligus_nextnum[0].real * 1024.)+ 1023]  >255:
                    eligus_7[int(eligus_nextnum[0].imag * 1024.)+ 1023][int(eligus_nextnum[0].real * 1024.+ 1023)]  = 128
                    
                mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] += 10
                if mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)][int(mandle4_nextnum[0].real * 1024.)] >255:
                    mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] = 128
                    
                eligus_7div4[int(eligus_7d4.imag * 1024.)+ 1023][int(eligus_7d4.real * 1024.)+ 1023] += 10
                if eligus_7div4[int(eligus_7d4.imag * 1024.)+ 1023][int(eligus_7d4.real * 1024.)+ 1023] >255:
                    eligus_7div4[int(eligus_7d4.imag * 1024.)+ 1023][int(eligus_7d4.real * 1024.)+ 1023] = 128

    imgux(mandle4_imag,'/home/ttombbab/fiveplus/man_not4'+str(picnum)+'.png')
    imgux(eligus_4minus4,'/home/ttombbab/fiveplus/man_not4div7'+str(picnum)+'.png')
    imgux(eligus_7,'/home/ttombbab/fiveplus/man_not7'+str(picnum)+'.png')
    imgux(eligus_7div4,'/home/ttombbab/fiveplus/man_not4-7'+str(picnum)+'.png')
 

