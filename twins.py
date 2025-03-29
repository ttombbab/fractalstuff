# -*- coding: utf-8 -*-

import random,math,time
import time
from PIL import Image
from FD import Fd
#import numpy as np
#from numpy.random import default_rng
#c = default_rng()
from random import uniform as RU


#RU = random.uniform
#sup1 =  Image.new('L',(4098,4098))#.effect_noise((256,256), .02)
#sup2 =  Image.new('L',(4098,4098))#.effect_noise((256,256), .02)
#sup3 =  Image.new('L',(4098,4098))#.effect_noise((256,256), .02)

def Sinc(x):
    x1,x2,x3 = x[1].real(),x[1].imag(),x[1].funk()
    if x== Fd(0.,0.,0.):
        return [Fd(0,0,0),Fd(1.,1.,1.)]
    try:
        return [Fd(0,0,0),Fd(math.sin(x1)/x1,math.sin(x2)/x2,math.sin(x3)/x3)]
    except ZeroDivisionError:
        return [Fd(0,0,0),Fd(1.,1.,1.)]

#superimg1.effect_noise((256,256), .02)

def mandle(a1):
    j,c = a1[0],a1[1]
    j = j**5 + c
    return ([j,c])

def IFS_gen(Fn,Io):
    Fn = Fn
    Io = Io
    Inext = Io
    while 1:
        yield Inext
        Inext = Fn(Inext)

def checkval(nextnum):
    try:
        imag = int(nextnum[0].imag() * 2048.)+ 2047
        funk = int(nextnum[0].funk() * 2048.)+ 2047
        real = int(nextnum[0].real() * 2048.)+ 2047
        if (real<0)or(imag<0)or(funk<0):
            real=abs(real)
            imag=abs(imag)
            funk=abs(funk)
        if (real>4097) or (imag>4097) or (funk>4097):
            if (real>4097):
                real = 2047
            if (imag>4097):
                imag = 2047
            if (funk>4097):
                funk = 2047
        return(real,imag,funk)
    except:
        return(2047,2047,2047)
#     if math.isnan(Valu2._real):
#         Valu2._real = 1.
#     if math.isnan(Valu2._imag):
#         Valu2._imag = 1.
#     if math.isnan(Valu2._funk):
#         Valu2._funk = 1.
#     if Valu2._real > 1.:
#         Valu2._real = 1.
#     elif Valu2._real < -1.:
#         Valu2._real = -1.
#     if Valu2._imag > 1.:
#         Valu2._imag = 1.
#     elif Valu2._imag < -1.:
#         Valu2._imag = -1.
#     if Valu2._funk > 1.:
#         Valu2._funk = 1.
#     elif Valu2._funk < -1.:
#         Valu2._funk = -1.
#     return Valu2
# 

#superimg = np.zeros((4098,4098), dtype=np.int8)
#superimg2 = np.zeros((4098,4098), dtype=np.int8)
#superimg3 = np.zeros((4098,4098), dtype=np.int8)

#superimg = c.integers(2, size=(4098,4098))
#superimg2 = c.integers(2, size=(4098,4098))
#superimg3 = c.integers(2, size=(4098,4098)) 
# 
superimg = [[0. for i in range(4098)] for j in range(4098)]
superimg2 = [[0. for i in range(4098)] for j in range(4098)]
superimg3 = [[0. for i in range(4098)] for j in range(4098)]

def imgux(gray,fname):
    #im = Image.fromarray(gray,mode = 'L')
    im = Image.new('L',(len(gray[int(len(gray)/2)]),len(gray)))
    [[im.putpixel((c,k),int(l)) for k,l in enumerate(i)] for c,i in enumerate(gray)]
    im.save(fname)

t = time.time()
RR =range(100)#(-10000,10000,8333)
IHH = range(2)
NHH = range(300)

#pp1 = sup1.putpixel
#gp1 = sup1.getpixel

#pp2 = sup2.putpixel
#gp2 = sup2.getpixel

#pp3 = sup3.putpixel
#gp3 = sup3.getpixel

def RSNN(IFS):
        rs = checkval(next(IFS))
        superimg[rs[1]][rs[0]] += 64#superimg[real_to_screen[1]][real_to_screen[0]] + 50#random.choice([-10,10])
        #pp1((rs[1],rs[0]),gp1((rs[1],rs[0]))+64)
        superimg2[rs[2]][rs[0]] += 64#superimg2[real_to_screen[2]][real_to_screen[0]] + 50#random.choice([-10,10])
        #pp2((rs[2],rs[0]),gp2((rs[2],rs[0]))+64)
        superimg3[rs[2]][rs[1]] += 64#superimg3[real_to_screen[2]][real_to_screen[1]] + 50#random.choice([-10,10]')

def FDSS(FD):
    #rnum = Fd(RU(-1.,1.),RU(-1.,1.),RU(-1.,1.))
    rnum = Fd(0.,0.,0.)
    IFS = IFS_gen(mandle,[rnum,FD])
    [RSNN(IFS) for k in NHH]

for preFD in RR:#range(-10000,10000,833):#range(-10000,10000,666)
    #print('extraitir',preFD)
    print( time.time()-t)
    t = time.time()
    #imgux(superimg,'realimag30' +str(preFD)+'.png')
    #imgux(superimg2,'realfunk30'+str(preFD)+'.png')
    #imgux(superimg3,'realreal30'+str(preFD)+'.png')
    
    for reFD in RR:#range(-10000,10000,833):#range(-10000,10000,666)
        for eFD in RR:
            FD = Fd(preFD/100.,reFD/100.,eFD/100.)
            #FD = Fd(0.45205,0.45205,0.45205)
            [FDSS(FD) for x in IHH]

#             for extraitir in IHH:            
#                 #rnum = Fd(0.,0.,0.)
#                 rnum = Fd(RU(-1.,1.),RU(-1.,1.),RU(-1.,1.))
#                 IFS = IFS_gen(mandle,[rnum,FD])
#                 [RSNN(IFS) for k in NHH]
#                 for itercount in NHH:
#                     #nn = next(IFS)
#                     #rs = checkval(nn)
#                     rs = checkval(next(IFS))
#                     superimg[rs[1]][rs[0]] += 64#superimg[real_to_screen[1]][real_to_screen[0]] + 50#random.choice([-10,10])
#                     #pp1((rs[1],rs[0]),gp1((rs[1],rs[0]))+64)
#                     superimg2[rs[2]][rs[0]] += 64#superimg2[real_to_screen[2]][real_to_screen[0]] + 50#random.choice([-10,10])
#                     #pp2((rs[2],rs[0]),gp2((rs[2],rs[0]))+64)
#                     superimg3[rs[2]][rs[1]] += 64#superimg3[real_to_screen[2]][real_to_screen[1]] + 50#random.choice([-10,10]')
#                     #pp3((rs[2],rs[1]),gp3((rs[2],rs[1]))+64)


    #                  superimg[int(nextnum[0]._imag * 2048.)+ 2047][int(nextnum[0]._real * 2048.)+ 2047] = superimg[int(nextnum[0]._imag * 2048.)+ 2047][int(nextnum[0]._real * 2048.)+ 2047] + 50#random.choice([-10,10])
    #                  superimg2[int(nextnum[0]._funk * 2048.)+ 2047][int(nextnum[0]._real * 2048.)+ 2047] = superimg2[int(nextnum[0]._funk * 2048.)+ 2047][int(nextnum[0]._real * 2048.)+ 2047] + 50#random.choice([-10,10])
    #                  superimg3[int(nextnum[0].funk()*2048.)+2047][int(nextnum[0].imag()*2048.)+2047] = superimg3[(int(nextnum[0].funk()*2048.))+2047][(int(nextnum[0].imag()*2048.))+2047] + 50#random.choice([-10,10]')
    # 
imgux(superimg,'realimag31.png')
#sup1.save('realimag27.b.png')
imgux(superimg2,'realfunk31.png')
#sup2.save('realfunk27.b.png')ssxds
imgux(superimg3,'realreal31.png')
#sup3.save('realreal27.b.png')
