
from . import unicorn
from . import unicorn_const
from . import arm_const


class Base(unicorn.Uc):
    def __init__(self, mode=None):
        super().__init__(unicorn_const.UC_ARCH_ARM, mode)
        self.reg = Reg_arm(self)


class armel_arm(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_LITTLE_ENDIAN|unicorn_const.UC_MODE_ARM)


class armel_thumb(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_LITTLE_ENDIAN|unicorn_const.UC_MODE_THUMB)


class armel_mclass(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_LITTLE_ENDIAN|unicorn_const.UC_MODE_MCLASS)


class armeb_arm(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_BIG_ENDIAN|unicorn_const.UC_MODE_ARM)


class armeb_thumb(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_BIG_ENDIAN|unicorn_const.UC_MODE_THUMB)


class armeb_mclass(Base):
    def __init__(self):
        super().__init__(unicorn_const.UC_MODE_BIG_ENDIAN|unicorn_const.UC_MODE_MCLASS)

class Reg_arm(unicorn.Registers):

    apsr = unicorn.Register(arm_const.UC_ARM_REG_APSR)
    apsr_nzcv = unicorn.Register(arm_const.UC_ARM_REG_APSR_NZCV)
    c13_c0_2 = unicorn.Register(arm_const.UC_ARM_REG_C13_C0_2)
    c13_c0_3 = unicorn.Register(arm_const.UC_ARM_REG_C13_C0_3)
    c1_c0_2 = unicorn.Register(arm_const.UC_ARM_REG_C1_C0_2)
    cpsr = unicorn.Register(arm_const.UC_ARM_REG_CPSR)
    d0 = unicorn.Register(arm_const.UC_ARM_REG_D0)
    d1 = unicorn.Register(arm_const.UC_ARM_REG_D1)
    d10 = unicorn.Register(arm_const.UC_ARM_REG_D10)
    d11 = unicorn.Register(arm_const.UC_ARM_REG_D11)
    d12 = unicorn.Register(arm_const.UC_ARM_REG_D12)
    d13 = unicorn.Register(arm_const.UC_ARM_REG_D13)
    d14 = unicorn.Register(arm_const.UC_ARM_REG_D14)
    d15 = unicorn.Register(arm_const.UC_ARM_REG_D15)
    d16 = unicorn.Register(arm_const.UC_ARM_REG_D16)
    d17 = unicorn.Register(arm_const.UC_ARM_REG_D17)
    d18 = unicorn.Register(arm_const.UC_ARM_REG_D18)
    d19 = unicorn.Register(arm_const.UC_ARM_REG_D19)
    d2 = unicorn.Register(arm_const.UC_ARM_REG_D2)
    d20 = unicorn.Register(arm_const.UC_ARM_REG_D20)
    d21 = unicorn.Register(arm_const.UC_ARM_REG_D21)
    d22 = unicorn.Register(arm_const.UC_ARM_REG_D22)
    d23 = unicorn.Register(arm_const.UC_ARM_REG_D23)
    d24 = unicorn.Register(arm_const.UC_ARM_REG_D24)
    d25 = unicorn.Register(arm_const.UC_ARM_REG_D25)
    d26 = unicorn.Register(arm_const.UC_ARM_REG_D26)
    d27 = unicorn.Register(arm_const.UC_ARM_REG_D27)
    d28 = unicorn.Register(arm_const.UC_ARM_REG_D28)
    d29 = unicorn.Register(arm_const.UC_ARM_REG_D29)
    d3 = unicorn.Register(arm_const.UC_ARM_REG_D3)
    d30 = unicorn.Register(arm_const.UC_ARM_REG_D30)
    d31 = unicorn.Register(arm_const.UC_ARM_REG_D31)
    d4 = unicorn.Register(arm_const.UC_ARM_REG_D4)
    d5 = unicorn.Register(arm_const.UC_ARM_REG_D5)
    d6 = unicorn.Register(arm_const.UC_ARM_REG_D6)
    d7 = unicorn.Register(arm_const.UC_ARM_REG_D7)
    d8 = unicorn.Register(arm_const.UC_ARM_REG_D8)
    d9 = unicorn.Register(arm_const.UC_ARM_REG_D9)
    ending = unicorn.Register(arm_const.UC_ARM_REG_ENDING)
    fp = unicorn.Register(arm_const.UC_ARM_REG_FP)
    fpexc = unicorn.Register(arm_const.UC_ARM_REG_FPEXC)
    fpinst = unicorn.Register(arm_const.UC_ARM_REG_FPINST)
    fpinst2 = unicorn.Register(arm_const.UC_ARM_REG_FPINST2)
    fpscr = unicorn.Register(arm_const.UC_ARM_REG_FPSCR)
    fpscr_nzcv = unicorn.Register(arm_const.UC_ARM_REG_FPSCR_NZCV)
    fpsid = unicorn.Register(arm_const.UC_ARM_REG_FPSID)
    invalid = unicorn.Register(arm_const.UC_ARM_REG_INVALID)
    ip = unicorn.Register(arm_const.UC_ARM_REG_IP)
    itstate = unicorn.Register(arm_const.UC_ARM_REG_ITSTATE)
    lr = unicorn.Register(arm_const.UC_ARM_REG_LR)
    mvfr0 = unicorn.Register(arm_const.UC_ARM_REG_MVFR0)
    mvfr1 = unicorn.Register(arm_const.UC_ARM_REG_MVFR1)
    mvfr2 = unicorn.Register(arm_const.UC_ARM_REG_MVFR2)
    pc = unicorn.Register(arm_const.UC_ARM_REG_PC)
    q0 = unicorn.Register(arm_const.UC_ARM_REG_Q0)
    q1 = unicorn.Register(arm_const.UC_ARM_REG_Q1)
    q10 = unicorn.Register(arm_const.UC_ARM_REG_Q10)
    q11 = unicorn.Register(arm_const.UC_ARM_REG_Q11)
    q12 = unicorn.Register(arm_const.UC_ARM_REG_Q12)
    q13 = unicorn.Register(arm_const.UC_ARM_REG_Q13)
    q14 = unicorn.Register(arm_const.UC_ARM_REG_Q14)
    q15 = unicorn.Register(arm_const.UC_ARM_REG_Q15)
    q2 = unicorn.Register(arm_const.UC_ARM_REG_Q2)
    q3 = unicorn.Register(arm_const.UC_ARM_REG_Q3)
    q4 = unicorn.Register(arm_const.UC_ARM_REG_Q4)
    q5 = unicorn.Register(arm_const.UC_ARM_REG_Q5)
    q6 = unicorn.Register(arm_const.UC_ARM_REG_Q6)
    q7 = unicorn.Register(arm_const.UC_ARM_REG_Q7)
    q8 = unicorn.Register(arm_const.UC_ARM_REG_Q8)
    q9 = unicorn.Register(arm_const.UC_ARM_REG_Q9)
    r0 = unicorn.Register(arm_const.UC_ARM_REG_R0)
    r1 = unicorn.Register(arm_const.UC_ARM_REG_R1)
    r10 = unicorn.Register(arm_const.UC_ARM_REG_R10)
    r11 = unicorn.Register(arm_const.UC_ARM_REG_R11)
    r12 = unicorn.Register(arm_const.UC_ARM_REG_R12)
    r13 = unicorn.Register(arm_const.UC_ARM_REG_R13)
    r14 = unicorn.Register(arm_const.UC_ARM_REG_R14)
    r15 = unicorn.Register(arm_const.UC_ARM_REG_R15)
    r2 = unicorn.Register(arm_const.UC_ARM_REG_R2)
    r3 = unicorn.Register(arm_const.UC_ARM_REG_R3)
    r4 = unicorn.Register(arm_const.UC_ARM_REG_R4)
    r5 = unicorn.Register(arm_const.UC_ARM_REG_R5)
    r6 = unicorn.Register(arm_const.UC_ARM_REG_R6)
    r7 = unicorn.Register(arm_const.UC_ARM_REG_R7)
    r8 = unicorn.Register(arm_const.UC_ARM_REG_R8)
    r9 = unicorn.Register(arm_const.UC_ARM_REG_R9)
    s0 = unicorn.Register(arm_const.UC_ARM_REG_S0)
    s1 = unicorn.Register(arm_const.UC_ARM_REG_S1)
    s10 = unicorn.Register(arm_const.UC_ARM_REG_S10)
    s11 = unicorn.Register(arm_const.UC_ARM_REG_S11)
    s12 = unicorn.Register(arm_const.UC_ARM_REG_S12)
    s13 = unicorn.Register(arm_const.UC_ARM_REG_S13)
    s14 = unicorn.Register(arm_const.UC_ARM_REG_S14)
    s15 = unicorn.Register(arm_const.UC_ARM_REG_S15)
    s16 = unicorn.Register(arm_const.UC_ARM_REG_S16)
    s17 = unicorn.Register(arm_const.UC_ARM_REG_S17)
    s18 = unicorn.Register(arm_const.UC_ARM_REG_S18)
    s19 = unicorn.Register(arm_const.UC_ARM_REG_S19)
    s2 = unicorn.Register(arm_const.UC_ARM_REG_S2)
    s20 = unicorn.Register(arm_const.UC_ARM_REG_S20)
    s21 = unicorn.Register(arm_const.UC_ARM_REG_S21)
    s22 = unicorn.Register(arm_const.UC_ARM_REG_S22)
    s23 = unicorn.Register(arm_const.UC_ARM_REG_S23)
    s24 = unicorn.Register(arm_const.UC_ARM_REG_S24)
    s25 = unicorn.Register(arm_const.UC_ARM_REG_S25)
    s26 = unicorn.Register(arm_const.UC_ARM_REG_S26)
    s27 = unicorn.Register(arm_const.UC_ARM_REG_S27)
    s28 = unicorn.Register(arm_const.UC_ARM_REG_S28)
    s29 = unicorn.Register(arm_const.UC_ARM_REG_S29)
    s3 = unicorn.Register(arm_const.UC_ARM_REG_S3)
    s30 = unicorn.Register(arm_const.UC_ARM_REG_S30)
    s31 = unicorn.Register(arm_const.UC_ARM_REG_S31)
    s4 = unicorn.Register(arm_const.UC_ARM_REG_S4)
    s5 = unicorn.Register(arm_const.UC_ARM_REG_S5)
    s6 = unicorn.Register(arm_const.UC_ARM_REG_S6)
    s7 = unicorn.Register(arm_const.UC_ARM_REG_S7)
    s8 = unicorn.Register(arm_const.UC_ARM_REG_S8)
    s9 = unicorn.Register(arm_const.UC_ARM_REG_S9)
    sb = unicorn.Register(arm_const.UC_ARM_REG_SB)
    sl = unicorn.Register(arm_const.UC_ARM_REG_SL)
    sp = unicorn.Register(arm_const.UC_ARM_REG_SP)
    spsr = unicorn.Register(arm_const.UC_ARM_REG_SPSR)

    def __init__(self, mu):
        self.mu = mu