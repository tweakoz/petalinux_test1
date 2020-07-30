#!/usr/bin/env python3

import argparse, sys, os
from ork import deco, path
from ork.eda.xilinx import vivado

deco = deco.Deco()

parser = argparse.ArgumentParser(description='build petalinux image')
parser.add_argument('--cachedir', help=deco.yellow('petalinux sstate cache downloads dir'))

_args = vars(parser.parse_args())

if len(sys.argv)==1:
    print(parser.format_usage())
    sys.exit(1)

cache_dir = None

if _args["cachedir"]:
  #see https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/60129817/Xilinx+Yocto+Builds+without+an+Internet+Connection
  cache_dir = path.Path(_args["cachedir"])


this_dir = path.Path(os.path.dirname(os.path.realpath(__file__)))
vctx = vivado.Context(hostdir=this_dir,
                      postremove=False,
                      FPGAPART="xczu7ev-fbvb900-1-i")

vctx.dirmaps[this_dir/"hardware"]="/data/hardware"
vctx.dirmaps[this_dir/"tftpboot"]="/tftpboot"
vctx.dirmaps[this_dir/"local.conf"]="/data/local.conf"
vctx.dirmaps[cache_dir]="/hwdevinst"
vctx.shell_command(["./_build_image.sh"],posttag="petalinux_test1")
