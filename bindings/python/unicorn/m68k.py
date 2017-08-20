
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import super
from future import standard_library
standard_library.install_aliases()

from . import unicorn
from . import unicorn_const
from . import m68k_const


class Base(unicorn.Uc):
    def __init__(self, mode=None):
        super().__init__(unicorn_const.UC_ARCH_M68K, mode)
        self.reg = Reg_m68k(self)


class m68k(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_BIG_ENDIAN)

class Reg_m68k(unicorn.Registers):

    a0 = unicorn.Register(m68k_const.UC_M68K_REG_A0)
    a1 = unicorn.Register(m68k_const.UC_M68K_REG_A1)
    a2 = unicorn.Register(m68k_const.UC_M68K_REG_A2)
    a3 = unicorn.Register(m68k_const.UC_M68K_REG_A3)
    a4 = unicorn.Register(m68k_const.UC_M68K_REG_A4)
    a5 = unicorn.Register(m68k_const.UC_M68K_REG_A5)
    a6 = unicorn.Register(m68k_const.UC_M68K_REG_A6)
    a7 = unicorn.Register(m68k_const.UC_M68K_REG_A7)
    d0 = unicorn.Register(m68k_const.UC_M68K_REG_D0)
    d1 = unicorn.Register(m68k_const.UC_M68K_REG_D1)
    d2 = unicorn.Register(m68k_const.UC_M68K_REG_D2)
    d3 = unicorn.Register(m68k_const.UC_M68K_REG_D3)
    d4 = unicorn.Register(m68k_const.UC_M68K_REG_D4)
    d5 = unicorn.Register(m68k_const.UC_M68K_REG_D5)
    d6 = unicorn.Register(m68k_const.UC_M68K_REG_D6)
    d7 = unicorn.Register(m68k_const.UC_M68K_REG_D7)
    ending = unicorn.Register(m68k_const.UC_M68K_REG_ENDING)
    invalid = unicorn.Register(m68k_const.UC_M68K_REG_INVALID)
    pc = unicorn.Register(m68k_const.UC_M68K_REG_PC)
    sr = unicorn.Register(m68k_const.UC_M68K_REG_SR)

    def __init__(self, mu):
        self.mu = mu