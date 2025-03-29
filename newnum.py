# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:51:30 2017

@author: tbabb
https://pastebin.com/04dFRaDa
"""
import math,numbers,cmath,array,random

class Fd(numbers.Complex):
    """(real,imag,funk) A number that represents i as the _imag part and -i as the _funk part"""
    def __init__(self,*args):
        if len(args) < 3:
            if len(args) == 2:
                if isinstance(args[0], complex):
                    _real = args[0].real
                    _imag = args[0].imag
                    if isinstance(args[1], complex):
                        _funk = args[1].imag
                    else:
                        _funk = args[1]
                else:
                    _real = args[0]
                    if isinstance(args[1], complex):
                        _imag = args[1].real
                        _funk = args[1].imag
                    else:
                        _imag = args[1]
                        _funk = 0.
            if len(args) == 1:
                if isinstance(args[0], complex):
                #if type(args[0]) == complex:
                    _real = args[0].real
                    _imag = args[0].imag
                    _funk = 0.
                else:
                    _real = args[0]
                    _imag = 0.
                    _funk = 0.
        else:
            _real = args[0]
            _imag = args[1]
            _funk = args[2]

        self._real = float(_real)
        self._imag = float(_imag)
        self._funk = float(_funk)


    def imag(self):
        return self._imag

    def real(self):
        return self._real

    def funk(self):
        return self._funk

    def __abs__(self):
        return complex(abs(complex(self._real,(self._imag+self._funk)/2.)),abs(complex(self._imag,self._funk)))

    def __complex__(self):
        return self.__abs__()

    def __eq__(self,fd1):
        if isinstance(fd1, Fd):
            if (self._real, self._imag, self._funk) == (fd1._real, fd1._imag, fd1._funk):
                return True
            else:
                return False
        elif isinstance(fd1, complex) and self._funk==0.:
            if (self._real, self._imag) == (fd1.real, fd1.imag):
                return True
            else:
                return False
        elif isinstance(fd1,( float, int)) and (self._funk==0 and self._imag==0):
            if self._real == float(fd1):
                return True
            else:
                return False
        return False

    def __pos__(self):
        return Fd(abs(self._real), abs(self._imag), abs(self._funk))

    def __neg__(self):
        return Fd(-self._real, -self._imag, -self._funk)

    def distance__real(self):
        if (-self._funk**2 - 2*self._imag*self._funk - self._imag**2) < 0.:
            return Fd(math.sqrt(abs(-self._funk**2 - 2*self._imag*self._funk - self._imag**2)),.33333,.33333)
        else:
            return Fd(math.sqrt(-self._funk**2 - 2*self._imag*self._funk - self._imag**2),0.,0.)

    def distance__imag(self):
        if (-self._funk**2 - 2*self._real*self._funk + self._real**2) < 0.:
            return Fd(0.,math.sqrt(abs(-self._funk**2 - 2*self._real*self._funk + self._real**2)),.33333)
        else:
            return Fd(0.,math.sqrt(-self._funk**2 - 2*self._real*self._funk + self._real**2),0.)

    def distance__funk(self):
        if (-self._imag**2 - 2*self._real*self._imag + self._real**2) < 0.:
            return Fd(0.,.33333,math.sqrt(abs(-self._imag**2 - 2*self._real*self._imag + self._real**2)))
        else:
            return Fd(0.,0.,math.sqrt(-self._imag**2 - 2*self._real*self._imag + self._real**2))

    def distance(self):
        a = self.distance__real()
        b = a + self.distance__imag()
        c = b + self.distance__funk()
        return c

    def __radd__(self, Fd2):
        return self.__add__(Fd2)

    def __add__(self, Fd2):
        if isinstance(Fd2, Fd):
            return self.do_my_adding_stuff(Fd2)
        elif isinstance(Fd2, complex):
            return self.do_my_complex_adding_stuff( Fd2)
        elif isinstance(Fd2, float):
            return self.do_my_float_adding_stuff( Fd2)
        elif isinstance(Fd2, int):
            return self.do_my_int_adding_stuff( Fd2)
        else:
            return NotImplemented

    def do_my_adding_stuff(self,Fd2):
        _real = self._real + Fd2._real
        _imag = self._imag + Fd2._imag
        _funk = self._funk + Fd2._funk
        return Fd(_real,_imag,_funk)

    def do_my_complex_adding_stuff(self,Fd2):
        _real = self._real + Fd2.real
        _imag = self._imag + Fd2.imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def do_my_float_adding_stuff(self,Fd2):
        _real = self._real + Fd2
        _imag = self._imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def do_my_int_adding_stuff(self,Fd2):
        _real = self._real + Fd2
        _imag = self._imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def __bool__(self):
        if [self._real,self._imag,self._funk] == [0.,0.,0.]:
            return False
        else:
            return True
    def __rsub__(self, Fd2):
        return self.__sub__(Fd2)

    def __sub__(self, Fd2):
        if isinstance(Fd2, Fd):
            return self.do_my_subtraction_stuff(Fd2)
        elif isinstance(Fd2, complex):
            return self.do_my_complex_subtraction_stuff(Fd2)
        elif isinstance(Fd2, float):
            return self.do_my_float_subtraction_stuff(Fd2)
        elif isinstance(Fd2, int):
            return self.do_my_int_subtraction_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_subtraction_stuff(self,Fd2):
        _real = self._real - Fd2._real
        _imag = self._imag - Fd2._imag
        _funk = self._funk - Fd2._funk
        return Fd(_real,_imag,_funk)

    def do_my_complex_subtraction_stuff(self,Fd2):
        _real = self._real - Fd2.real
        _imag = self._imag - Fd2.imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def do_my_float_subtraction_stuff(self,Fd2):
        _real = self._real - Fd2
        _imag = self._imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def do_my_int_subtraction_stuff(self,Fd2):
        _real = self._real - Fd2
        _imag = self._imag
        _funk = self._funk
        return Fd(_real,_imag,_funk)

    def __rmul__(self, Fd2):
        return self.__mul__(Fd2)

    def __mul__(self, Fd2):
        if isinstance(Fd2, Fd):
            return self.do_my_multipication_stuff(Fd2)
        elif isinstance(Fd2, complex):
            return self.do_my_complex_multipication_stuff(Fd2)
        elif isinstance(Fd2, float):
            return self.do_my_float_multipicationn_stuff(Fd2)
        elif isinstance(Fd2, int):
            return self.do_my_int_multipication_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_multipication_stuff(self,Fd2):
        a,b,c = self._real,self._imag,self._funk
        d,e,f = Fd2._real,Fd2._imag,Fd2._funk
        if (a,b,c) == (0.,0.,0.):
            return Fd(0.,e+d,f+d)
        elif (d,e,f) == (0.,0.,0.):
            return Fd(0.,a+b,a+c)

        _real = (a*d) - (b*e) - (c*f) + abs((b*f) + (c*e))
        _imag = (a*e) + (b*d)
        _funk = (a*f) + (c*d)
        return Fd(_real,_imag,_funk)

    def do_my_complex_multipication_stuff(self,Fd2):
        a,b,c = self._real,self._imag,self._funk
        d,e = Fd2.real,Fd2.imag


        _real = (a*d) - (b*e) + abs(c*e)
        _imag = (b*d) + (b*d)
        _funk = (c*d)
        return Fd(_real,_imag,_funk)

    def do_my_float_multipicationn_stuff(self,Fd2):
        a,b,c = self._real,self._imag,self._funk
        d = Fd2
        _real = (a*d)
        _imag = (b*d)
        _funk = (c*d)

        return Fd(_real,_imag,_funk)

    def do_my_int_multipication_stuff(self,Fd2):
        a,b,c = self._real,self._imag,self._funk
        d = Fd2
        _real = (a*d)
        _imag = (b*d)
        _funk = (c*d)

        return Fd(_real,_imag,_funk)

    def conjugate(self):
        _real = self._real
        _imag = -self._imag
        _funk = -self._funk
        return Fd(_real,_imag,_funk)

    def Reciprocal(self,fd2):
        Fdr = Fd(fd2._real,-fd2._imag,-fd2._funk)
        divisor = fd2._real**2 - fd2._imag**2 - fd2._funk**2
        try:
            return Fd(Fdr._real/divisor , Fdr._imag/divisor , Fdr._funk/divisor)
        except ZeroDivisionError:
            return Fd(1.,0.,0.)

    def __rtruediv__(self, Fd2):
        return self.__truediv__(Fd2)

    def __truediv__(self, Fd2):
        if isinstance(Fd2, Fd):
            return self.do_my_division_stuff(Fd2)
        elif isinstance(Fd2, complex):
            return self.do_my_complex_division_stuff( Fd2)
        elif isinstance(Fd2, float):
            return self.do_my_float_division_stuff( Fd2)
        elif isinstance(Fd2, int):
            return self.do_my_int_division_stuff( Fd2)

        else:
            return NotImplemented

    def do_my_division_stuff(self,Fd2):
        a,b,c = self._real, self._imag, self._funk
        d,e,f = Fd2._real, Fd2._imag, Fd2._funk
        if [d,e,f] == [0,0,0]:
            raise ZeroDivisionError

        elif [e,f] == [0,0]:
            return self.do_my_float_division_stuff(Fd2._real)
        elif e == 0 or f == 0:
            if e ==0:
                cfd = complex(d,f)
                ll =  self.do_my_complex_division_stuff(cfd)
                return Fd(ll._real,ll._funk, ll._imag)
            else:
                cfd = complex(d,e)
                return self.do_my_complex_division_stuff(cfd)
        else:
            real = (a/d) + (b/e) - (b/f) - (c/e) + (c/f)
            imag = (a/e) + (b/d)
            funk = (a/f) + (c/d)
            return Fd(real, imag,funk)

    def do_my_complex_division_stuff(self,Fd2):
        a = self._real/Fd2
        b = self._imag/Fd2
        c = self._funk/Fd2
        real = a.real - b.imag + c.imag
        imag = a.imag + b.real
        funk = c.real
        return Fd(real, imag,funk)

    def do_my_float_division_stuff(self,Fd2):
        return Fd(self._real/Fd2,self._imag/Fd2,self._funk/Fd2)

    def do_my_int_division_stuff(self,Fd2):
        return Fd(self._real/Fd2,self._imag/Fd2,self._funk/Fd2)

    def __rpow__(self, Fd2):
        return self.__pow__(Fd2)

    def __pow__(self,n_pow):
        if isinstance(n_pow, int):
            if n_pow == 0:
                return Fd(1.,0.,0.)
            elif n_pow == 1:
                return Fd(self._real,self._imag,self._funk)
            Fd2 = self.__mul__(Fd(self._real,self._imag,self._funk))
            if n_pow == 2:
                return Fd2
            else:
                for i in range(n_pow-2):
                    Fd2 = self.__mul__(Fd2)
                return Fd2
        else:
            return NotImplemented
        
    def __round__(self,dig):
        return Fd(round(self._real, dig), round(self._imag, dig), round(self._funk, dig))

    def Absolute(self,Fd1):
        return math.sqrt(Fd1._real**2 - Fd1._imag**2 - Fd1._funk**2)

    def __hash__(self):
        return hash((self._real, self._imag, self._funk))

    def __repr__(self):
        return '(' + str(self._real) + '+' + str(self._imag) + 'j+' + str(self._funk) + 'k)'

    def __str__(self):
        return self.__repr__()

    def __bytes__(self):
        return bytes(self._real) + bytes(self._imag) + bytes(self._funk)

    def sqrt(self):
        first_root = cmath.sqrt(complex(self._real,self._imag))
        second_root = cmath.sqrt(complex(self._real,self._funk))
        return Fd(first_root.real,(first_root.imag + second_root.imag),(first_root.imag + second_root.imag))

    def colapse(self):
        return complex(self._real,(self._imag - self._funk))

    def __nantoinf__(self,Fd1):
        if math.isnan(Fd1._real) or math.isnan(Fd1._imag) or math.isnan(Fd1._funk):
            if math.isnan(Fd1._real):
                Fd1 = Fd(0. , float('inf') * Fd1._imag , float('inf') * Fd1._funk)
            if math.isnan(Fd1._imag):
                Fd1 = Fd(Fd1._real , float('inf') * Fd1._imag , float('-inf') * Fd1._funk)
            if math.isnan(Fd1._funk):
                Fd1 = Fd(Fd1._real , float('-inf') * Fd1._imag , float('inf') * Fd1._funk)
        return Fd1


class mandel(numbers.Complex):
    """mandel number (c,j,d,sp)"""
    def __init__(self,*args):
        self.bufferptr = 0
        self._part_solel_real = memoryview(array.array('f', [0.]*16384))
        self._part_solel_imag = memoryview(array.array('f', [0.]*16384))
        self._part_solel_funk = memoryview(array.array('f', [0.]*16384))
        self._aura = False
        """(c of mandel function,imag,funk) A number that represents i as the _imag part and -i as the _funk part"""
        if isinstance(args[0], Fd):
            _Fd_c = args[0]
        elif isinstance(args[0], complex):
            _Fd_c = Fd(args[0],0.)
        elif isinstance(args[0], float) or isinstance(args[0], int):
            _Fd_c = Fd(args[0],0.,0.)
        if isinstance(args[1], Fd):
            _Fd_z = args[1]
        elif isinstance(args[1], complex):
            _Fd_z = Fd(args[1],0.)
        elif isinstance(args[1], float) or isinstance(args[1], int):
            _Fd_z = Fd(args[1],0.,0.)
        self._dim = args[2]
        self._soulp = args[3]
        self._Fd_c = _Fd_c
        self._Fd_z = _Fd_z
        if self._Fd_z != 0:
            self._aura = True
        self.ifs = self.IFS_gen(self._mandel,self._Fd_z)
        if self._soulp > 0:
            for i in range(self._soulp + 16384):
                fdret = next(self.ifs)
                if i > self._soulp:
                    self._part_solel_real[i-self._soulp] = fdret.real()
                    self._part_solel_imag[i-self._soulp] = fdret.imag()
                    self._part_solel_funk[i-self._soulp] = fdret.funk()
        else:
            for i in range(16384):
                fdret = next(self.ifs)
                self._part_solel_real[i] = fdret.real()
                self._part_solel_imag[i] = fdret.imag()
                self._part_solel_funk[i] = fdret.funk()

    def _mandel(self,z):
        """input Z output Z**_dim + c"""
        z = z**self._dim + self._Fd_c
        return (z)

    def IFS_gen(self,funct, initinp):
        Inext = initinp
        while 1:
            yield Inext
            Inext = funct(Inext)

    def imag(self):
        return self.C()._imag

    def real(self):
        return self.C()._real

    def funk(self):
        return self.C()._funk

    def Z(self):
        return self._Fd_z

    def C(self):
        return self._Fd_c

    def dim(self):
        return self._dim

    def sp(self):
        return self._soulp

    def aura(self):
        return self._aura

    def __pos__(self):
        return mandel(self._Fd_c, self._Fd_z, self._dim, self._soulp)

    def __neg__(self):
        Z = Fd(abs(-self.Z()._real), -abs(self.Z()._imag), -abs(self.Z()._funk))
        c = Fd(abs(-self.C()._real), -abs(self.C()._imag), -abs(self.C()._funk))
        return mandel(c,Z,self._dim,self._soulp)

    def __abs__(self):
        return mandel(abs(self._Fd_c),abs(self._Fd_z),self._dim, self._soulp)

    def __complex__(self):
        return complex(self._Fd_z.real(),self._Fd_z.imag())

    def __eq__(self,fd1):
        if isinstance(fd1, mandel):
            if fd1._aura:
                return False
            else:
                if fd1._Fd_c == self._Fd_c:
                    return True

        elif isinstance(fd1, complex) and self.funk()==0.:
            if fd1 == self.__complex__():
                return True
            else:
                return False
        elif (isinstance(fd1, float) or isinstance(fd1, int)) and (self.funk()==0 and self.imag()==0):
            if self.real() == float(fd1):
                return True
            else:
                return False
        else:
            return False

    def is_root(self):
        if not self._aura:
            return True
        
        tempmandel = self.IFS_gen(self._mandel,Fd(0.,0.,0.))
        for i in range(self._soulp + 5):            
            tempm = next(tempmandel)
            #print(round(tempm,7) , round(self._Fd_z,7),end='~~/n')
            if round(tempm,6) == round(self._Fd_z,6):
                self._aura = False
                self._soulp = i
                return True
        return False

    def cenetrbuffer(self):
        self._part_solel_real[0:8192] = self._part_solel_real[8192:]
        self._part_solel_imag[0:8192] = self._part_solel_imag[8192:]
        self._part_solel_funk[0:8192] = self._part_solel_funk[8192:]
        for i in range(8192):
            fdret = next(self.ifs)
            self._part_solel_real[i+4096] = fdret.real()
            self._part_solel_imag[i+4096] = fdret.imag()
            self._part_solel_funk[i+4096] = fdret.funk()

    def increment_sp(self):
        self._soulp = self._soulp + 1
        self.bufferptr = self.bufferptr + 1
        if self.bufferptr < 12288:
            self._Fd_z = Fd(self._part_solel_real[self.bufferptr],
                            self._part_solel_imag[self.bufferptr],
                            self._part_solel_funk[self.bufferptr])
            self.ifs = self.IFS_gen(self._mandel,self._Fd_z)
        else:
            self.cenetrbuffer()
#            self._part_solel_real[0:8192] = self._part_solel_real[8192:]
#            self._part_solel_imag[0:8192] = self._part_solel_imag[8192:]
#            self._part_solel_funk[0:8192] = self._part_solel_funk[8192:]
#            for i in range(8192):
#                fdret = next(self.ifs)
#                self._part_solel_real[i+4096] = fdret.real()
#                self._part_solel_imag[i+4096] = fdret.imag()
#                self._part_solel_funk[i+4096] = fdret.funk()
            self.bufferptr = self.bufferptr - 4096
            self._Fd_z = Fd(self._part_solel_real[self.bufferptr],
                            self._part_solel_imag[self.bufferptr],
                            self._part_solel_funk[self.bufferptr])
            self.ifs = self.IFS_gen(self._mandel,self._Fd_z)

    def deincrement_sp(self):
        self._soulp = self._soulp - 1
        self.bufferptr = self.bufferptr - 1
        if self.bufferptr > 0:

            self._Fd_z = Fd(self._part_solel_real[self.bufferptr],
                            self._part_solel_imag[self.bufferptr],
                            self._part_solel_funk[self.bufferptr])
            self.ifs = self.IFS_gen(self._mandel,self._Fd_z)
        elif self._dim == 2:
            #self.bufferptr = self.bufferptr + 1
            tempfd = self._Fd_z - self._Fd_c
            self._Fd_z = tempfd.sqrt()
        else:
            #self.bufferptr = self.bufferptr + 1
            if self._aura == False or self.is_root():
                tempifs = self.IFS_gen(self._mandel,Fd(0.,0.,0.))
                tempfd = Fd(0.,0.,0.)
                for i in range(self._soulp-1):
                    tempfd = next(tempifs)
                self._Fd_z = tempfd
                self._aura = False                
                return True
            else:
                self.bufferptr = self.bufferptr + 1
                print('not implemented')
                def qrt(x):
                    z = .001
                    while math.sqrt(math.sqrt(z**12)) < x:
                        z = z + .001
                    return z
                return False

    def genrandomaura(self):
        rnum = Fd(random.uniform(-1.,1.),random.uniform(-1.,1.),random.uniform(-1.,1.))
        return mandel(self.C(), rnum, self._dim, self._soulp)

    def __radd__(self, Fd2):
        return self.__add__(Fd2)

    def __add__(self, Fd2):
        if isinstance(Fd2, mandel):
            return self.do_my_adding_stuff(Fd2)
        elif isinstance(Fd2, (Fd, complex, float, int)):
            return self.do_my_other_adding_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_adding_stuff(self, Fd2):        
        addret_c = self._Fd_c + Fd2.C()
        addret_z = self._Fd_z + Fd2.Z()        
        addret_dim = min([self._dim, Fd2._dim])
        addret_sp = max([self._soulp, Fd2._soulp])
        addret = mandel(addret_c,addret_z,addret_dim,addret_sp)
        if addret.Z() == Fd(0.,0.,0.):
            addret._aura = False
        else:
            addret._aura = True
        addret.ifs = addret.IFS_gen(addret._mandel,addret._Fd_z)
        addret.bufferptr = 0
        for i in range(16384):
            fdret = next(addret.ifs)
            addret._part_solel_real[i] = fdret.real()
            addret._part_solel_imag[i] = fdret.imag()
            addret._part_solel_funk[i] = fdret.funk()
        return addret

    def do_my_other_adding_stuff(self, Fd2):
        addret_c = self._Fd_c + Fd2
        addret_z = self._Fd_z + Fd2
        addret_dim = self._dim
        addret_sp =self._soulp
        addret = mandel(addret_c,addret_z,addret_dim,addret_sp)
        if addret.Z() == Fd(0.,0.,0.):
            addret._aura = False
        else:
            addret._aura = True
        addret.bufferptr= 0
        addret.ifs = addret.IFS_gen(addret._mandel,addret._Fd_z)
        for i in range(16384):
            fdret = next(addret.ifs)
            addret._part_solel_real[i] = fdret.real()
            addret._part_solel_imag[i] = fdret.imag()
            addret._part_solel_funk[i] = fdret.funk()
        return addret

    def __rsub__(self,Fd2):
        return self.__sub__(Fd2)

    def __sub__(self, Fd2):
        if isinstance(Fd2, mandel):
            return self.do_my_subtraction_stuff(Fd2)
        elif isinstance(Fd2, (Fd, complex, float, int)):
            return self.do_my_other_subtraction_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_subtraction_stuff(self,Fd2):
        addret_c = self._Fd_c - Fd2.C()
        addret_z = self._Fd_z - Fd2.Z()        
        addret_dim = min([self._dim, Fd2._dim])
        addret_sp = max([self._soulp, Fd2._soulp])
        addret = mandel(addret_c,addret_z,addret_dim,addret_sp)
        if addret.Z() == Fd(0.,0.,0.):
            addret._aura = False
        else:
            addret._aura = True
        addret.ifs = addret.IFS_gen(addret._mandel,addret._Fd_z)
        addret.bufferptr = 0
        for i in range(16384):
            fdret = next(addret.ifs)
            addret._part_solel_real[i] = fdret.real()
            addret._part_solel_imag[i] = fdret.imag()
            addret._part_solel_funk[i] = fdret.funk()
        return addret

    def do_my_other_subtraction_stuff(self,Fd2):
        addret_c = self._Fd_c - Fd2
        addret_z = self._Fd_z - Fd2
        addret_dim = self._dim
        addret_sp =self._soulp
        addret = mandel(addret_c,addret_z,addret_dim,addret_sp)
        if addret.Z() == Fd(0.,0.,0.):
            addret._aura = False
        else:
            addret._aura = True
        addret.bufferptr= 0
        addret.ifs = addret.IFS_gen(addret._mandel,addret._Fd_z)
        for i in range(16384):
            fdret = next(addret.ifs)
            addret._part_solel_real[i] = fdret.real()
            addret._part_solel_imag[i] = fdret.imag()
            addret._part_solel_funk[i] = fdret.funk()
        return addret

    def __mul__(self, Fd2):
        if isinstance(Fd2, mandel):
            return self.do_my_multipication_stuff(Fd2)
        elif isinstance(Fd2,(Fd, complex, float, int)):
            return self.do_my_other_multipication_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_multipication_stuff(self, Fd2):        
        multiret_c = self._Fd_c * Fd2.C()
        multiret_z = self._Fd_z * Fd2.Z()        
        multiret_dim = max([self._dim, Fd2._dim])
        multiret_sp = max([self._soulp, Fd2._soulp])
        multiret = mandel(multiret_c,multiret_z,multiret_dim,multiret_sp)
        if multiret_z == Fd(0.,0.,0.):
            multiret._aura = True
            multiret._soulp = 0
        else:
            multiret._aura = True
        multiret.ifs = multiret.IFS_gen(multiret._mandel,multiret._Fd_z)
        for i in range(16384):
            fdret = next(multiret.ifs)
            multiret._part_solel_real[i] = fdret.real()
            multiret._part_solel_imag[i] = fdret.imag()
            multiret._part_solel_funk[i] = fdret.funk()
        return multiret

    def do_my_other_multipication_stuff(self, Fd2):
        multiret_c = self._Fd_c * Fd2
        multiret_z = self._Fd_z * Fd2        
        multiret_dim = self._dim
        multiret_sp = self._soulp
        multiret = mandel(multiret_c,multiret_z,multiret_dim,multiret_sp)
        if multiret.Z() == Fd(0.,0.,0.):
            multiret._aura = False
            multiret._soulp = 0
        else:
            multiret._aura = True
        multiret.ifs = multiret.IFS_gen(multiret._mandel,multiret._Fd_z)
        for i in range(16384):
            fdret = next(multiret.ifs)
            multiret._part_solel_real[i] = fdret.real()
            multiret._part_solel_imag[i] = fdret.imag()
            multiret._part_solel_funk[i] = fdret.funk()
        return multiret

    def __pow__(self,npow):
        return NotImplemented

    def __rmul__(self,Fd2):
        return self.__mul__(Fd2)

    def __rpow__(self,Fd2):
        return NotImplemented

    def __rtruediv__(self,Fd2):
        return self.__truediv__(Fd2)

    def __truediv__(self,Fd2):
        if isinstance(Fd2, mandel):
            return self.do_my_division_stuff(Fd2)
        elif isinstance(Fd2,( Fd, complex, float, int)):
            return self.do_my_other_division_stuff(Fd2)
        else:
            return NotImplemented

    def do_my_division_stuff(self,Fd2):
        multiret_c = self._Fd_c / Fd2.C()
        try:
            multiret_z = self._Fd_z / Fd2.Z()
            multiret_aura = True
            multiret_sp = max([self._soulp, Fd2._soulp])
        except ZeroDivisionError:
            multiret_z = Fd(0.,0.,0.)
            multiret_aura = False
            multiret_sp = 0
        multiret_dim = max([self._dim, Fd2._dim])        
        multiret = mandel(multiret_c,multiret_z,multiret_dim,multiret_sp)
        multiret._aura = multiret_aura        
        multiret.ifs = multiret.IFS_gen(multiret._mandel,multiret._Fd_z)
        for i in range(16384):
            fdret = next(multiret.ifs)
            multiret._part_solel_real[i] = fdret.real()
            multiret._part_solel_imag[i] = fdret.imag()
            multiret._part_solel_funk[i] = fdret.funk()
        return multiret
        
        
    def do_my_other_division_stuff(self,Fd2):
        multiret_c = self._Fd_c / Fd2
        multiret_z = self._Fd_z / Fd2        
        multiret_dim = self._dim
        multiret_sp = self._soulp
        multiret = mandel(multiret_c,multiret_z,multiret_dim,multiret_sp)
        if multiret.Z() == Fd(0.,0.,0.):
            multiret._aura = False
        else:
            multiret._aura = True
        multiret.ifs = multiret.IFS_gen(multiret._mandel,multiret._Fd_z)
        for i in range(16384):
            fdret = next(multiret.ifs)
            multiret._part_solel_real[i] = fdret.real()
            multiret._part_solel_imag[i] = fdret.imag()
            multiret._part_solel_funk[i] = fdret.funk()
        return multiret
            
    def conjugate(self):
        return NotImplemented

    def __str__(self):
        return f'C : {self.C()}\nZ : {self.Z()}\nDim : {self.dim()}\nSoulp : {self.sp()}\nAura : {self.aura()}'

    def info(self):
        """print(info)"""
        info = """mandel is defined as Z**d + C.
        The infinite number list generated is called the Sole line.
        The pointer of sole itereations is called the Sole Sointer (_soulp).
        When Z starts a zero the Sole Line is said to be root (_aura = False).
        Whe Z starts on any number off the root it is said to be an aura (_aura = True).
        Special math rules:
            c plays nice with other numbers.
            after any operation, Sole Pointer will bex maximum.
            j*0. or j/0. sets _soulp = 0. and _aura = False and Z = 0.
            All other opeations on j set _aura = True.
            *See is_root() function to reclame _aura.
            Addition or subtraction of dimentions gives the lowest dimention (_dim).
            Multiplication or division of dimentions gives the highest dimention.
            powers add dimentions."""
        print(info)