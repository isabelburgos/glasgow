from amaranth import *

from ..gateware.registers import Registers
from ..platform.all import *


__all__ = ["GlasgowSimulationTarget"]


class GlasgowSimulationTarget(Elaboratable):
    sys_clk_freq = 30e6

    def __init__(self, revision, multiplexer_cls=None):
        if revision in ("A0", "B0"):
            self.platform = GlasgowPlatformRevAB()
            self.sys_clk_freq = 30e6
        elif revision in "C0":
            self.platform = GlasgowPlatformRevC0()
            self.sys_clk_freq = 48e6
        elif revision in ("C1", "C2", "C3"):
            self.platform = GlasgowPlatformRevC123()
            self.sys_clk_freq = 48e6
        else:
            raise ValueError("Unknown revision")

        try:
            self.platform.request("unused")
        except ResourceError:
            pass

        self.registers = Registers()
        if multiplexer_cls is not None:
            self.multiplexer = multiplexer_cls()
        else:
            self.multiplexer = None
        self._submodules = []

    def add_submodule(self, sub):
        self._submodules.append(sub)

    def elaborate(self, platform):
        m = Module()

        m.submodules.registers = self.registers
        if self.multiplexer is not None:
            m.submodules.multiplexer = self.multiplexer
        m.submodules += self._submodules

        return m
