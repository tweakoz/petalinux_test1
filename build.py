#!/usr/bin/env python3

import os
from ork import path
from ork.eda.xilinx import vivado

this_dir = path.Path(os.path.dirname(os.path.realpath(__file__)))
vctx = vivado.Context(hostdir=this_dir,
                      FPGAPART="xczu7ev-fbvb900-1-i")

dkey = str(this_dir/"hardware")
dval = "/data/hardware"
vctx.dirmaps[dkey]=dval
vctx.shell_command(["./_build_image.sh"])
