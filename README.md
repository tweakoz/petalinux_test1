# petalinux_test1
test petalinux docker image /  ork.build/eda

to regenerate xsa:
1. ```getbsp.py```
2. load up ```uz7ev_evcc_2019_2/hardware/UZ7EV_EVCC_2019_2/UZ7EV_EVCC.xpr``` in vivado
3. in tcl console, ```write_hw_platform -verbose -force -include_bit UZ7EV_EVCC.xsa```
