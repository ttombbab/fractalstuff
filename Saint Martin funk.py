# -*- coding: utf-8 -*-
import random,math
from PIL import Image
from newnumber import Fd

def mandle2(a1):
    j,c = a1[0],a1[1]
    j = j**2 + c
    return ([j,c])

def IFS_gen(Fn,Io):
    Fn = Fn
    Io = Io
    Inext = Io
    while 1:
        yield Inext
        Inext = Fn(Inext)

def checkval(Valu2):
    if math.isnan(Valu2._real):
        Valu2._real = 1.
    if math.isnan(Valu2._imag):
        Valu2._imag = 1.
    if math.isnan(Valu2._funk):
        Valu2._funk = 1.
    if Valu2._real > 1.:
        Valu2._real = 1.
    elif Valu2._real < -1.:
        Valu2._real = -1.
    if Valu2._imag > 1.:
        Valu2._imag = 1.
    elif Valu2._imag < -1.:
        Valu2._imag = -1.
    if Valu2._funk > 1.:
        Valu2._funk = 1.
    elif Valu2._funk < -1.:
        Valu2._funk = -1.
    return Valu2

superimg = [[0. for i in range(2048)] for j in range(2048)]
superimg2 = [[0. for i in range(2048)] for j in range(2048)]
superimg_7 = [[0. for i in range(2048)] for j in range(2048)]
superimg2_7 = [[0. for i in range(2048)] for j in range(2048)]

def imgux(gray,fname):
    im = Image.new('L',(len(gray[int(len(gray)/2)]),len(gray)))
    [[im.putpixel((c,k),int(l)) for k,l in enumerate(i)] for c,i in enumerate(gray)]
    im.save(fname)

for page in range(200):
    print(page)
    rnuma =  Fd(random.uniform(-1.,1.),random.uniform(-1.,1.),0.8)# 4./5. ID jerome, 4./6. is catherine, 4/7 is eligus, 4./8. is Martin
    rnumb =  Fd(random.uniform(-1.,1.),random.uniform(-1.,1.),-0.8)# Jerome
    for extraitir in range(600):
        rnum = Fd(random.uniform(-1.,1.),random.uniform(-1.,1.),random.uniform(-1.,1.))#,random.uniform(-1.,1.))
        newIFS = IFS_gen(mandle2,[rnum,rnuma])
        newIFS7 = IFS_gen(mandle2,[rnum,rnumb])
        for itercount in range(200):
            nextnum = next(newIFS)
            nextnum7 = next(newIFS7)
            nextnum[0] = checkval(nextnum[0])
            nextnum7[0] = checkval(nextnum7[0])
            
            superimg[int(nextnum[0]._imag * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023]  += 10
            if superimg[int(nextnum[0]._imag * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023] >255:
                superimg[int(nextnum[0]._imag * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023]  =120
                
            superimg2[int(nextnum[0]._funk * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023] += 10
            if superimg2[int(nextnum[0]._funk * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023] > 255:
                superimg2[int(nextnum[0]._funk * 1024.)+ 1023][int(nextnum[0]._real * 1024.)+ 1023] = 120
 
            superimg_7[int(nextnum7[0]._imag * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023]  += 10
            if superimg_7[int(nextnum7[0]._imag * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023] >255:
                superimg_7[int(nextnum7[0]._imag * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023]  =120
                
            superimg2_7[int(nextnum7[0]._funk * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023] += 10
            if superimg2_7[int(nextnum7[0]._funk * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023] > 255:
                superimg2_7[int(nextnum7[0]._funk * 1024.)+ 1023][int(nextnum7[0]._real * 1024.)+ 1023] = 120
 
 
    imgux(superimg,'/home/ttombbab/herotwins2/realimag4'+str(page)+'.png')
    imgux(superimg2,'/home/ttombbab/herotwins2/realfunk4'+str(page)+'.png')
    imgux(superimg_7,'/home/ttombbab/herotwins2/realimag7'+str(page)+'.png')
    imgux(superimg2_7,'/home/ttombbab/herotwins2/realfunk7'+str(page)+'.png')

