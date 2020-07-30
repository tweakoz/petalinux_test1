#!/usr/bin/env python3

import os
from ork import path
from ork.eda.xilinx import vivado

# todo - state cache mirror
#  see https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/60129817/Xilinx+Yocto+Builds+without+an+Internet+Connection

this_dir = path.Path(os.path.dirname(os.path.realpath(__file__)))
vctx = vivado.Context(hostdir=this_dir,
                      postremove=False,
                      FPGAPART="xczu7ev-fbvb900-1-i")

vctx.dirmaps[str(this_dir/"hardware")]="/data/hardware"
vctx.dirmaps[str(this_dir/"tftpboot")]="/tftpboot"
vctx.shell_command(["./_build_image.sh"],posttag="petalinux_test1")
