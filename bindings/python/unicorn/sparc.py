
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import super
from future import standard_library
standard_library.install_aliases()

from . import unicorn
from . import unicorn_const
from . import sparc_const


class Base(unicorn.Uc):
    def __init__(self, mode=None):
        super().__init__(unicorn_const.UC_ARCH_SPARC, mode)


class sparc_32(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_32)


class sparc_64(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_64)

class Reg(unicorn.Registers):
    def __init__(self, mu):
        super().__init__()
        self.mu = mu

    ending = unicorn.Register(sparc_const.UC_SPARC_REG_ENDING)
    f0 = unicorn.Register(sparc_const.UC_SPARC_REG_F0)
    f1 = unicorn.Register(sparc_const.UC_SPARC_REG_F1)
    f10 = unicorn.Register(sparc_const.UC_SPARC_REG_F10)
    f11 = unicorn.Register(sparc_const.UC_SPARC_REG_F11)
    f12 = unicorn.Register(sparc_const.UC_SPARC_REG_F12)
    f13 = unicorn.Register(sparc_const.UC_SPARC_REG_F13)
    f14 = unicorn.Register(sparc_const.UC_SPARC_REG_F14)
    f15 = unicorn.Register(sparc_const.UC_SPARC_REG_F15)
    f16 = unicorn.Register(sparc_const.UC_SPARC_REG_F16)
    f17 = unicorn.Register(sparc_const.UC_SPARC_REG_F17)
    f18 = unicorn.Register(sparc_const.UC_SPARC_REG_F18)
    f19 = unicorn.Register(sparc_const.UC_SPARC_REG_F19)
    f2 = unicorn.Register(sparc_const.UC_SPARC_REG_F2)
    f20 = unicorn.Register(sparc_const.UC_SPARC_REG_F20)
    f21 = unicorn.Register(sparc_const.UC_SPARC_REG_F21)
    f22 = unicorn.Register(sparc_const.UC_SPARC_REG_F22)
    f23 = unicorn.Register(sparc_const.UC_SPARC_REG_F23)
    f24 = unicorn.Register(sparc_const.UC_SPARC_REG_F24)
    f25 = unicorn.Register(sparc_const.UC_SPARC_REG_F25)
    f26 = unicorn.Register(sparc_const.UC_SPARC_REG_F26)
    f27 = unicorn.Register(sparc_const.UC_SPARC_REG_F27)
    f28 = unicorn.Register(sparc_const.UC_SPARC_REG_F28)
    f29 = unicorn.Register(sparc_const.UC_SPARC_REG_F29)
    f3 = unicorn.Register(sparc_const.UC_SPARC_REG_F3)
    f30 = unicorn.Register(sparc_const.UC_SPARC_REG_F30)
    f31 = unicorn.Register(sparc_const.UC_SPARC_REG_F31)
    f32 = unicorn.Register(sparc_const.UC_SPARC_REG_F32)
    f34 = unicorn.Register(sparc_const.UC_SPARC_REG_F34)
    f36 = unicorn.Register(sparc_const.UC_SPARC_REG_F36)
    f38 = unicorn.Register(sparc_const.UC_SPARC_REG_F38)
    f4 = unicorn.Register(sparc_const.UC_SPARC_REG_F4)
    f40 = unicorn.Register(sparc_const.UC_SPARC_REG_F40)
    f42 = unicorn.Register(sparc_const.UC_SPARC_REG_F42)
    f44 = unicorn.Register(sparc_const.UC_SPARC_REG_F44)
    f46 = unicorn.Register(sparc_const.UC_SPARC_REG_F46)
    f48 = unicorn.Register(sparc_const.UC_SPARC_REG_F48)
    f5 = unicorn.Register(sparc_const.UC_SPARC_REG_F5)
    f50 = unicorn.Register(sparc_const.UC_SPARC_REG_F50)
    f52 = unicorn.Register(sparc_const.UC_SPARC_REG_F52)
    f54 = unicorn.Register(sparc_const.UC_SPARC_REG_F54)
    f56 = unicorn.Register(sparc_const.UC_SPARC_REG_F56)
    f58 = unicorn.Register(sparc_const.UC_SPARC_REG_F58)
    f6 = unicorn.Register(sparc_const.UC_SPARC_REG_F6)
    f60 = unicorn.Register(sparc_const.UC_SPARC_REG_F60)
    f62 = unicorn.Register(sparc_const.UC_SPARC_REG_F62)
    f7 = unicorn.Register(sparc_const.UC_SPARC_REG_F7)
    f8 = unicorn.Register(sparc_const.UC_SPARC_REG_F8)
    f9 = unicorn.Register(sparc_const.UC_SPARC_REG_F9)
    fcc0 = unicorn.Register(sparc_const.UC_SPARC_REG_FCC0)
    fcc1 = unicorn.Register(sparc_const.UC_SPARC_REG_FCC1)
    fcc2 = unicorn.Register(sparc_const.UC_SPARC_REG_FCC2)
    fcc3 = unicorn.Register(sparc_const.UC_SPARC_REG_FCC3)
    fp = unicorn.Register(sparc_const.UC_SPARC_REG_FP)
    g0 = unicorn.Register(sparc_const.UC_SPARC_REG_G0)
    g1 = unicorn.Register(sparc_const.UC_SPARC_REG_G1)
    g2 = unicorn.Register(sparc_const.UC_SPARC_REG_G2)
    g3 = unicorn.Register(sparc_const.UC_SPARC_REG_G3)
    g4 = unicorn.Register(sparc_const.UC_SPARC_REG_G4)
    g5 = unicorn.Register(sparc_const.UC_SPARC_REG_G5)
    g6 = unicorn.Register(sparc_const.UC_SPARC_REG_G6)
    g7 = unicorn.Register(sparc_const.UC_SPARC_REG_G7)
    i0 = unicorn.Register(sparc_const.UC_SPARC_REG_I0)
    i1 = unicorn.Register(sparc_const.UC_SPARC_REG_I1)
    i2 = unicorn.Register(sparc_const.UC_SPARC_REG_I2)
    i3 = unicorn.Register(sparc_const.UC_SPARC_REG_I3)
    i4 = unicorn.Register(sparc_const.UC_SPARC_REG_I4)
    i5 = unicorn.Register(sparc_const.UC_SPARC_REG_I5)
    i6 = unicorn.Register(sparc_const.UC_SPARC_REG_I6)
    i7 = unicorn.Register(sparc_const.UC_SPARC_REG_I7)
    icc = unicorn.Register(sparc_const.UC_SPARC_REG_ICC)
    invalid = unicorn.Register(sparc_const.UC_SPARC_REG_INVALID)
    l0 = unicorn.Register(sparc_const.UC_SPARC_REG_L0)
    l1 = unicorn.Register(sparc_const.UC_SPARC_REG_L1)
    l2 = unicorn.Register(sparc_const.UC_SPARC_REG_L2)
    l3 = unicorn.Register(sparc_const.UC_SPARC_REG_L3)
    l4 = unicorn.Register(sparc_const.UC_SPARC_REG_L4)
    l5 = unicorn.Register(sparc_const.UC_SPARC_REG_L5)
    l6 = unicorn.Register(sparc_const.UC_SPARC_REG_L6)
    l7 = unicorn.Register(sparc_const.UC_SPARC_REG_L7)
    o0 = unicorn.Register(sparc_const.UC_SPARC_REG_O0)
    o1 = unicorn.Register(sparc_const.UC_SPARC_REG_O1)
    o2 = unicorn.Register(sparc_const.UC_SPARC_REG_O2)
    o3 = unicorn.Register(sparc_const.UC_SPARC_REG_O3)
    o4 = unicorn.Register(sparc_const.UC_SPARC_REG_O4)
    o5 = unicorn.Register(sparc_const.UC_SPARC_REG_O5)
    o6 = unicorn.Register(sparc_const.UC_SPARC_REG_O6)
    o7 = unicorn.Register(sparc_const.UC_SPARC_REG_O7)
    pc = unicorn.Register(sparc_const.UC_SPARC_REG_PC)
    sp = unicorn.Register(sparc_const.UC_SPARC_REG_SP)
    xcc = unicorn.Register(sparc_const.UC_SPARC_REG_XCC)
    y = unicorn.Register(sparc_const.UC_SPARC_REG_Y)

