from glasgow.applet import GlasgowAppletV2TestCase, synthesis_test
from . import VGAOutputApplet


class VGAOutputAppletTestCase(GlasgowAppletV2TestCase, applet=VGAOutputApplet):
    @synthesis_test
    def test_build(self):
        self.assertBuilds()
