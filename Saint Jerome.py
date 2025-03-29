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
jerome_7 = [[0 for i in range(2048)] for j in range(2048)]
jerome_7div4 = [[0 for i in range(2048)] for j in range(2048)]
jerome_4minus4 = [[0 for i in range(2048)] for j in range(2048)]

for picnum in range(30):
    print(picnum,time.localtime(),end=',')
    for i in range(100):
        for j in range(100):
            rnum = complex(RN(-1.,1.),RN(-1.,1.))
            rnum2 = complex(RN(-1.,1.),RN(-1.,1.))
            mandle_not_IFS = IFS(mandle4,(rnum,rnum2))
            jerome_IFS = IFS(mandle5,(rnum,rnum2))
            for itercount in range(2048):
                jerome_nextnum = jerome_IFS.next()
                mandle4_nextnum = mandle_not_IFS.next()
                try:
                    jerome_4m7 =  mandle4_nextnum[0]-jerome_nextnum[0]
                except:
                    jerome_4m7 =  complex(.001,.001)
                if MIAN(jerome_4m7.real):
                    jerome_4m7 = complex(1.,jerome_4m7.imag)
                if MIAN(jerome_4m7.imag):
                    jerome_4m7 = complex(jerome_4m7.real,1.)
                if jerome_4m7.real > 1.:
                    jerome_4m7 = complex(1.,jerome_4m7.imag)
                elif jerome_4m7.real < -1.:
                    jerome_4m7 = complex(-1.,jerome_4m7.imag)
                if jerome_4m7.imag > 1.:
                    jerome_4m7 = complex(jerome_4m7.real,1.)
                elif jerome_4m7.imag < -1.:
                    jerome_4m7 = complex(jerome_4m7.real,-1)        
                
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
                    jerome_7d4 = jerome_nextnum[0]/ mandle4_nextnum[0]
                except:
                    jerome_7d4 =  complex(.001,.001)
                if MIAN(jerome_7d4.real):
                    jerome_7d4 = complex(1.,jerome_7d4.imag)
                if MIAN(jerome_7d4.imag):
                    jerome_7d4 = complex(jerome_7d4.real,1.)
                if jerome_7d4.real > 1.:
                    jerome_7d4 = complex(1.,jerome_7d4.imag)
                elif jerome_7d4.real < -1.:
                    jerome_7d4 = complex(-1.,jerome_7d4.imag)
                if jerome_7d4.imag > 1.:
                    jerome_7d4 = complex(jerome_7d4.real,1.)
                elif jerome_7d4.imag < -1.:
                    jerome_7d4 = complex(jerome_7d4.real,-1)

                
                if jerome_nextnum[0].real > 1.:
                    jerome_nextnum[0] = complex(1.,jerome_nextnum[0].imag)
                elif jerome_nextnum[0].real < -1.:
                    jerome_nextnum[0] = complex(-1.,jerome_nextnum[0].imag)
                if jerome_nextnum[0].imag > 1.:
                    jerome_nextnum[0] = complex(jerome_nextnum[0].real,1.)
                elif jerome_nextnum[0].imag < -1.:
                    jerome_nextnum[0] = complex(jerome_nextnum[0].real,-1)
                
                jerome_4minus4[int(jerome_4m7.imag * 1024.)+ 1023][int(jerome_4m7.real * 1024.)+ 1023] += 10

                if jerome_4minus4[int(jerome_4m7.imag * 1024.)+ 1023][int(jerome_4m7.real * 1024.)+ 1023]  >255:
                    jerome_4minus4[int(jerome_4m7.imag * 1024.)+ 1023][int(jerome_4m7.real * 1024.+ 1023)]  = 128
                    
                jerome_7[int(jerome_nextnum[0].imag * 1024.)+ 1023][int(jerome_nextnum[0].real * 1024.)+ 1023] += 10
                if jerome_7[int(jerome_nextnum[0].imag * 1024.)+ 1023][int(jerome_nextnum[0].real * 1024.)+ 1023]  >255:
                    jerome_7[int(jerome_nextnum[0].imag * 1024.)+ 1023][int(jerome_nextnum[0].real * 1024.+ 1023)]  = 128
                    
                mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] += 10
                if mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)][int(mandle4_nextnum[0].real * 1024.)] >255:
                    mandle4_imag[int(mandle4_nextnum[0].imag * 1024.)+ 1023][int(mandle4_nextnum[0].real * 1024.)+ 1023] = 128
                    
                jerome_7div4[int(jerome_7d4.imag * 1024.)+ 1023][int(jerome_7d4.real * 1024.)+ 1023] += 10
                if jerome_7div4[int(jerome_7d4.imag * 1024.)+ 1023][int(jerome_7d4.real * 1024.)+ 1023] >255:
                    jerome_7div4[int(jerome_7d4.imag * 1024.)+ 1023][int(jerome_7d4.real * 1024.)+ 1023] = 128

    imgux(mandle4_imag,'/home/ttombbab/fiveplus/man_not4'+str(picnum)+'.png')
    imgux(jerome_4minus4,'/home/ttombbab/fiveplus/man_not4div7'+str(picnum)+'.png')
    imgux(jerome_7,'/home/ttombbab/fiveplus/man_not7'+str(picnum)+'.png')
    imgux(jerome_7div4,'/home/ttombbab/fiveplus/man_not4-7'+str(picnum)+'.png')
 

