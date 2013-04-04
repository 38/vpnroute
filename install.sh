#!/bin/sh
install(){
	target_dir=`dirname $2`
	if [ ! -e ${target_dir} ]; then
		mkdir -p ${target_dir}
	fi
	if [ -e $2 ]; then
		cp $2 $2.bak
	fi
	cp $1 $2
}
install ip-pre-up ${PREFIX}/etc/ppp/ip-pre-up
install 9999del-route ${PREFIX}/etc/ppp/ip-down.d/9999del-route
install update_vpnroute ${PREFIX}/usr/bin
install read_vpn_blacklist.py ${PREFIX}/etc/ppp/read_vpn_blacklist.py
install vpn_blacklist ${PREFIX}/etc/ppp/vpn_blacklist
install user.conf ${PREFIX}/etc/ppp/vpnroute.d/user.conf
touch ${PREFIX}/etc/ppp/vpnroute.d/china.conf
update_vpnroute
