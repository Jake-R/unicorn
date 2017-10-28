
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import super
from future import standard_library
standard_library.install_aliases()

from . import unicorn
from . import unicorn_const

class Hooks_instance(object):
    def __init__(self, mu):
        self.mu = mu 
        self.block = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_BLOCK) 
        self.code = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_CODE) 
        self.insn = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_INSN) 
        self.intr = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_INTR) 
        self.mem_fetch = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_FETCH) 
        self.mem_fetch_invalid = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_FETCH_INVALID) 
        self.mem_fetch_prot = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_FETCH_PROT) 
        self.mem_fetch_unmapped = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_FETCH_UNMAPPED) 
        self.mem_invalid = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_INVALID) 
        self.mem_prot = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_PROT) 
        self.mem_read = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_READ) 
        self.mem_read_after = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_READ_AFTER) 
        self.mem_read_invalid = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_READ_INVALID) 
        self.mem_read_prot = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_READ_PROT) 
        self.mem_read_unmapped = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_READ_UNMAPPED) 
        self.mem_unmapped = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_UNMAPPED) 
        self.mem_valid = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_VALID) 
        self.mem_write = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_WRITE) 
        self.mem_write_invalid = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_WRITE_INVALID) 
        self.mem_write_prot = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_WRITE_PROT) 
        self.mem_write_unmapped = unicorn.HookAttr(self.mu, unicorn_const.UC_HOOK_MEM_WRITE_UNMAPPED) 