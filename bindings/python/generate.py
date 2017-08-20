from jinja2 import Template
import itertools

import unicorn

endianness = [('el', 'UC_MODE_LITTLE_ENDIAN'), ('eb', 'UC_MODE_BIG_ENDIAN')]
sizes = [('_32', 'UC_MODE_32'), ('_64', 'UC_MODE_64')]
x86_sizes = [('_16', 'UC_MODE_16')] + sizes
arm_modes = [('_arm', 'UC_MODE_ARM'), ('_thumb', 'UC_MODE_THUMB'), ('_mclass', 'UC_MODE_MCLASS')]
none = [('', '')]

arches = [(('arm', 'UC_ARCH_ARM'), endianness, arm_modes),
          (('arm64', 'UC_ARCH_ARM64'), endianness, arm_modes),
          (('mips', 'UC_ARCH_MIPS'), endianness, sizes),
          (('x86', 'UC_ARCH_X86'), x86_sizes),
          (('ppc', 'UC_ARCH_PPC'), [('','UC_MODE_PPC_64')], [('', 'UC_MODE_BIG_ENDIAN')]),
          (('sparc', 'UC_ARCH_SPARC'), sizes),
          (('m68k', 'UC_ARCH_M68K'), [('', 'UC_MODE_BIG_ENDIAN')])]

register_template = Template(
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import super
from future import standard_library
standard_library.install_aliases()

from . import unicorn
from . import unicorn_const
from . import {{ const_name }}


class Base(unicorn.Uc):
    def __init__(self, mode=None):
        super().__init__(unicorn_const.{{ arch_const }}, mode)
{% for mode in modes %}

class {{ arch_name }}{{ mode[0] }}(Base):
    def __init__(self):
        super().__init__({{ mode[1] }})
{% endfor %}
class Reg(unicorn.Registers):
    def __init__(self, mu):
        super().__init__()
        self.mu = mu
{% for reg in regs %}
    {{ reg[0] }} = unicorn.Register({{ const_name }}.{{ reg[1] }}){% endfor %}


""")

hook_template = Template(
"""
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
        self.mu = mu {% for hook in hooks %}
        self.{{ hook[0] }} = unicorn.HookAttr(self.mu, unicorn_const.{{ hook[1] }}) {% endfor %}


_hook_list = []
{% for hook in hooks %}
{{ hook[0] }} = unicorn.HookDecorator(_hook_list, unicorn_const.{{ hook[1] }}) {% endfor %}
""")

def generate_arch_file(arch_name, arch_const, modes):
    const_name = '{}_const'.format(arch_name)
    if not hasattr(unicorn, const_name):
        return None
    consts = getattr(unicorn, const_name)
    regs = registers_from_const(consts, arch_name)
#    modes = [(x.split('_', 2)[-1], x) for x in dir(unicorn) if x.startswith('UC_MODE')]
    mode_names = ["".join([y[0] for y in x]) for x in modes]
    mode_modes = ["|".join(["unicorn_const." + y[1] for y in x if y[1] != '']) for x in modes]
    modes = zip(mode_names, mode_modes)
    file_contents = register_template.render(const_name=const_name, regs=regs, arch_name=arch_name,
                                             arch_const=arch_const, modes=modes)
    with open('unicorn/{}.py'.format(arch_name), 'w') as f:
        f.write(file_contents)


def registers_from_const(consts, arch_name):
    regs = [x for x in dir(consts) if x.startswith('UC_{}_REG'.format(arch_name.upper()))]
    regs = [(x.split('_', 3)[-1].lower(), x) for x in regs]
    regs = [('_'+x[0], x[1]) if x[0].isdigit() else x for x in regs]
    return regs

def generate_hook_file():
    hooks = [x for x in dir(unicorn) if x.startswith('UC_HOOK_')]
    hooks = [(x.split('_', 2)[-1].lower(), x) for x in hooks]
    file_contents = hook_template.render(hooks=hooks)
    with open("unicorn/Hook.py", 'w') as f:
        f.write(file_contents)


for arch in arches:
    modes = list(itertools.product(*arch[1:]))
    generate_arch_file(arch[0][0], arch[0][1], modes)

generate_hook_file()
