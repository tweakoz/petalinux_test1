# petalinux_test1
petalinux-docker container test

to use:
1. install ork build tools @ https://github.com/tweakoz/ork.build
2. from OBT environment shell: install docker image with https://github.com/tweakoz/petalinux-docker
3. from OBT environment shell: ```./build.py``` - wait for build to complete
4. build products will appear in ```<this-repo-dir>/tftpboot/```

to regenerate xsa:
1. ```getbsp.py```
2. load up ```uz7ev_evcc_2019_2/hardware/UZ7EV_EVCC_2019_2/UZ7EV_EVCC.xpr``` in vivado
3. in tcl console, ```write_hw_platform -verbose -force -include_bit UZ7EV_EVCC.xsa```
