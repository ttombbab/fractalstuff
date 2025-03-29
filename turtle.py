#-*-coding:utf8;-*-
#qpy:console

print "This is console module"
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 06 11:41:17 2013

@author: Tom Babbitt
"""

import math
import numpy as np
import Image
import random
RN = random.uniform
MIAN = math.isnan
NPFS = np.fromstring
NP16 = np.int16
MSN = math.sin
NA = np.arange
NPA = np.array
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
    im.save(file(fname,'wb'))

def mandle(a1):
    j,c = a1[0],a1[1]
    try:
        j =  j**5 + c
        #l =  j**5  + j
        
    except:
        j = complex(.0001,.0001)
    return NPA([j,c])
    
def mandle9(a2):
    j,k,c = a2[0],a2[1],a2[2]
    try:
        j =  j**9 - 36 * j**7 *(k.real**2 + k.imag**2) + 126 * j**5 *(k.real**2 + k.imag**2)**2 - 84 * j**3 *(k.real**2 + k.imag**2)**3 + 9 * j *(k.real**2 + k.imag**2)**4 + c
    except:
        j = complex(.0001,.0001)
    return NPA([j,c,k])   
superimg = [[0 for i in range(2048)] for j in range(2048)]
superimg2 = [[0 for i in range(2048)] for j in range(2048)]
superimg4 = [[0 for i in range(2048)] for j in range(2048)]
su2 = [[0 for i in range(2048)] for j in range(2048)]


def mandle5(a3):
    j,l,c,k = a3[0],a3[1],a3[2],a3[3]
    try:
        j = j**5-10* j**3* k**2 + 5* j* k**4 + c
        #j =  j**5 + k
        l = l**5-10* l**3* j**2 + 5* l* j**4 + k
#        l = l**5-10* l**3* c**2 + 5* l* c**4 + k
#        j = j**5-10* j**3* l**2 + 5* j* l**4 + c
    except:
        j = complex(.0001,.0001)
        l = complex(.0001,.0001)
    return NPA([j,l,c,k])


for picnum in range(20):    
    for i in range(120):
        for j in range(120):
            complex_time2 = complex((i-60.)/ 60., (j-60.)/60.)
            rnum = complex(RN(-1.,1.),RN(-1.,1.))
            newIFS2 = IFS(mandle9,NPA([complex(RN(-1.,1.),RN(-1.,1.)),complex_time2,rnum]))
            newIFS3 = IFS(mandle,NPA([rnum,complex_time2]))
            newIFS = IFS(mandle,NPA([rnum,complex_time2]))
            for itercount in range(2048):
                nextnum = newIFS.next()
                nextnum2 = newIFS2.next()
                nextnum3 = newIFS3.next()
                try:
                    newvalc = nextnum3[0]/ nextnum[0]
                except:
                    newvalc =  complex(.001,.001)
                if MIAN(newvalc.real):
                    newvalc = complex(1.,newvalc.imag)
                if MIAN(newvalc.imag):
                    newvalc = complex(newvalc.real,1.)
                if newvalc.real > 1.:
                    newvalc = complex(1.,newvalc.imag)
                elif newvalc.real < -1.:
                    newvalc = complex(-1.,newvalc.imag)
                if newvalc.imag > 1.:
                    newvalc = complex(newvalc.real,1.)
                elif newvalc.imag < -1.:
                    newvalc = complex(newvalc.real,-1)            
                
               
                try:
                    newvalD =  nextnum[0]-nextnum3[0]
                except:
                    newvalD =  complex(.001,.001)
                if MIAN(newvalD.real):
                    newvalD = complex(1.,newvalD.imag)
                if MIAN(newvalD.imag):
                    newvalD = complex(newvalD.real,1.)
                if newvalD.real > 1.:
                    newvalD = complex(1.,newvalD.imag)
                elif newvalD.real < -1.:
                    newvalD = complex(-1.,newvalD.imag)
                if newvalD.imag > 1.:
                    newvalD = complex(newvalD.real,1.)
                elif newvalD.imag < -1.:
                    newvalD = complex(newvalD.real,-1)        
                
                if MIAN(nextnum[0].real):
                    nextnum[0] = complex(1.,nextnum[0].imag)
                if MIAN(nextnum[0].imag):
                    nextnum[0] = complex(nextnum[0].real,1.)
                if nextnum[0].real > 1.:
                    nextnum[0] = complex(1.,nextnum[0].imag)
                elif nextnum[0].real < -1.:
                    nextnum[0] = complex(-1.,nextnum[0].imag)
                if nextnum[0].imag > 1.:
                    nextnum[0] = complex(nextnum[0].real,1.)
                elif nextnum[0].imag < -1.:
                    nextnum[0] = complex(nextnum[0].real,-1)
                if nextnum2[0].real > 1.:
                    nextnum2[0] = complex(1.,nextnum2[0].imag)
                elif nextnum2[0].real < -1.:
                    nextnum2[0] = complex(-1.,nextnum2[0].imag)
                if nextnum2[0].imag > 1.:
                    nextnum2[0] = complex(nextnum2[0].real,1)
                elif nextnum2[0].imag < -1.:
                    nextnum2[0] = complex(nextnum2[0].real,-1)
                
                su2[int(newvalD.imag * 1024.)+ 1023][int(newvalD.real * 1024.)+ 1023] += 10
                if su2[int(newvalD.imag * 1024.)+ 1023][int(newvalD.real * 1024.)+ 1023]  >255:
                    su2[int(newvalD.imag * 1024.)+ 1023][int(newvalD.real * 1024.+ 1023)]  = 128
                superimg[int(nextnum2[0].imag * 1024.)+ 1023][int(nextnum2[0].real * 1024.)+ 1023] += 10
                if superimg[int(nextnum2[0].imag * 1024.)+ 1023][int(nextnum2[0].real * 1024.)+ 1023]  >255:
                    superimg[int(nextnum2[0].imag * 1024.)+ 1023][int(nextnum2[0].real * 1024.+ 1023)]  = 128
                superimg2[int(nextnum[0].imag * 1024.)+ 1023][int(nextnum[0].real * 1024.)+ 1023] += 10
                if superimg2[int(nextnum[0].imag * 1024.)][int(nextnum[0].real * 1024.)] >255:
                    superimg2[int(nextnum[0].imag * 1024.)+ 1023][int(nextnum[0].real * 1024.)+ 1023] = 128
                superimg4[int(newvalc.imag * 1024.)+ 1023][int(newvalc.real * 1024.)+ 1023] += 10
                if superimg4[int(newvalc.imag * 1024.)+ 1023][int(newvalc.real * 1024.)+ 1023] >255:
                    superimg4[int(newvalc.imag * 1024.)+ 1023][int(newvalc.real * 1024.)+ 1023] = 128
        
    
    imgux(superimg2,'c:\\python27\\tom\\lena169\\rawaudiotest'+str(picnum)+'.png')
    imgux(superimg4,'c:\\python27\\tom\\lena169\\rawaudioSUrat'+str(picnum)+'.png')
    imgux(superimg,'c:\\python27\\tom\\lena169\\rawaudiotestend'+str(picnum)+'.png')
    imgux(su2,'c:\\python27\\tom\\lena169\\rawaudioSU'+str(picnum)+'.png')
    su = [[abs(superimg2[j][k]- superimg[j][k])for j in range(2048)] for k in range(2048)]
    imgux(su,'c:\\python27\\tom\\lena169\\rawaudiodiff'+str(picnum)+'.png')