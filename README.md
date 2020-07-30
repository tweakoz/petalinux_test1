# petalinux_test1
Xilinx-PetaLinux-2020.1 docker container test.

Tested on following docker hosts:
 1. macos-catalina
 2. ubuntu 20.04 

to use:
1. install ork build tools @ https://github.com/tweakoz/ork.build
2. from OBT environment shell: install docker image with https://github.com/tweakoz/petalinux-docker
3. from OBT environment shell: ```./build.py``` - wait for build to complete (it will be a while)
4. build products will appear in ```<this-repo-dir>/tftpboot/```

to regenerate xsa:
1. ```getbsp.py```
2. load up ```uz7ev_evcc_2019_2/hardware/UZ7EV_EVCC_2019_2/UZ7EV_EVCC.xpr``` in vivado
3. in tcl console, ```write_hw_platform -verbose -force -include_bit UZ7EV_EVCC.xsa```
