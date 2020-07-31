#!/usr/bin/env python3

import argparse, sys, os, platform, tempfile
from ork import deco, path, command
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

######################################################################

DISPLAY=os.environ["DISPLAY"]
HOME=path.Path(os.environ["HOME"])

osname = platform.system()

######################################################################

if osname=="Darwin":
 os.system("xhost + 127.0.0.1")
 DISPLAY="host.docker.internal:0"

xauth_host = str(HOME/".Xauthority")
xauth_cont = "/home/eda/.Xauthority"
######################################################################

temp_dir = path.Path(tempfile._get_default_tempdir())
temp_fname = temp_dir/next(tempfile._get_candidate_names())

######################################################################

dirmaps={}
dirmaps[this_dir/"hardware"]="/data/hardware"
dirmaps[this_dir/"tftpboot"]="/tftpboot"
dirmaps[this_dir/"local.conf"]="/data/local.conf"
dirmaps[cache_dir]="/hwdevinst"

cline =  ["docker","run","-it"]
cline += ["-h","EdaHost"]
cline += ["-e","DISPLAY=%s"%os.environ["DISPLAY"]]
cline += ["--net=host","--ipc=host"]
cline += ["-v","/tmp/.X11-unix:/tmp/.X11-unix"]
cline += ["-v","%s:%s"%(xauth_host,xauth_cont)]
#cline += ["-v","%s:%s"%(proj_host,proj_cont)]
cline += ["--cidfile=%s"%temp_fname]
for K in dirmaps.keys():
  V = dirmaps[K]
  cline += ["-v","%s:%s"%(str(K),str(V))]
cline += ["-w",this_dir]
cline += ["petalinux_test1"]
cline += ["/bin/bash"]

command.system(cline)

with open(temp_fname, 'r') as file:
  cid = file.read()
  command.system(["docker",
                  "commit",cid,
                  "petalinux_test1"])
