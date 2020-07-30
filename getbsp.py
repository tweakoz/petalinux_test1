#!/usr/bin/env python3

import os
from ork import wget, command, path

this_dir = path.Path(os.path.dirname(os.path.realpath(__file__)))

url = "http://downloads.element14.com/downloads/zedboard/ultra96-v2/uz7ev_evcc_2019_2.bsp.zip"
wget.wget(urls=[url],output_name="uz7ev_evcc_2019_2.bsp.zip",md5val="dc0b9cc8561a94861f2a02f11ee5f07a")

os.chdir(this_dir)
command.system(["unzip","-o",path.downloads()/"uz7ev_evcc_2019_2.bsp.zip"])
