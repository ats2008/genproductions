#! /bin/env python

import os, shutil, subprocess

h4znames =["0_00023824", "0_00004765", "0_00002382", "0_00001191", "0_00000596", "0_00000298", "0_00000149", "0_00000030", "0_00000000", "n0_00000030", "n0_00000149", "n0_00000298", "n0_00000596", "n0_00001191", "n0_00002382", "n0_00004765", "n0_00023824"]
h3znames =["n0_0044671", "n0_0029781", "n0_0014890", "n0_0007445", "n0_0003723","n0_0001861", "n0_0000620", "n0_0000124", "0_0000000", "0_0000124","0_0000620", "0_0001861", "0_0003723", "0_0007445", "0_0014890","0_0029781", "0_0044671"]
h3anames =["0_0032892", "0_0021928", "0_0032892", "0_0007309", "0_0003655","0_0001827", "0_0000609", "0_0000122", "0_0000000", "n0_0000122","n0_0000609", "n0_0001827", "n0_0003655", "n0_0007309", "n0_0014619","n0_0021928", "n0_0032892"]

h4zs = ["0.0002382400", "0.0000476490", "0.0000238240", "0.0000119120", "0.0000059561","0.0000029781", "0.0000014890", "0.0000002978", "0.0000000000", "-0.0000002978","-0.0000014890", "-0.0000029781", "-0.0000059561", "-0.0000119120", "-0.0000238240","-0.0000476490", "-0.0002382400"]
h3zs =["-0.0044671000", "-0.0029781000", "-0.0014890000", "-0.0007445100", "-0.0003722600","-0.0001861300", "-0.0000620430", "-0.0000124090", "0.0000000000", "0.0000124090","0.0000620430", "0.0001861300", "0.0003722600", "0.0007445100", "0.0014890000","0.0029781000", "0.0044671000"]
h3as =["0.0032892000", "0.0021928000", "0.0032892000", "0.0007309300", "0.0003654700","0.0001827300", "0.0000609110", "0.0000121820", "0.0000000000", "-0.0000121820","-0.0000609110", "-0.0001827300", "-0.0003654700", "-0.0007309300", "-0.0014619000","-0.0021928000", "-0.0032892000"]


f=open("ZGtoLLG01j_5f_LO_mlm_old_reweight_card.dat","w")
a = 0
f.write("change rwgt_dir ./rwgt\n\n")
for h4z in h4zs:
	a += 1
	f.write("launch --rwgt_name=ZG_h4z_%s_%s\nset f4Z 0.0\nset f5a 0.0\nset f5Z 0.0\nset h1a 0.0\nset h1Z 0.0\nset h3a 0.0\nset h3Z 0.0\nset h2a 0.0\nset h2Z 0.0\nset h4a 0.0\nset h4Z %s\n\n" % (str(a),str(h4znames[a-1]),str(h4z)))
a = 0
for h3z in h3zs:
	a += 1
	f.write("launch --rwgt_name=ZG_h3z_%s_%s\nset f4Z 0.0\nset f5a 0.0\nset f5Z 0.0\nset h1a 0.0\nset h1Z 0.0\nset h3a 0.0\nset h3Z %s\nset h2a 0.0\nset h2Z 0.0\nset h4a 0.0\nset h4Z 0.0\n\n" % (str(a),str(h3znames[a-1]),str(h3z)))
a = 0
for h3a in h3as:
	a += 1
	f.write("launch --rwgt_name=ZG_h3a_%s_%s\nset f4Z 0.0\nset f5a 0.0\nset f5Z 0.0\nset h1a 0.0\nset h1Z 0.0\nset h3a %s\nset h3Z 0.0\nset h2a 0.0\nset h2Z 0.0\nset h4a 0.0\nset h4Z 0.0\n\n" % (str(a),str(h3anames[a-1]),str(h3a)))
f.close

