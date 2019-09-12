#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : initscripts
Version  : 9.49.46
Release  : 2
URL      : file:///home/clear/tar/initscripts-9.49.46.tar.gz
Source0  : file:///home/clear/tar/initscripts-9.49.46.tar.gz
Summary  : The inittab file and the /etc/init.d scripts
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: initscripts-bin = %{version}-%{release}
Requires: initscripts-config = %{version}-%{release}
Requires: initscripts-libexec = %{version}-%{release}
Requires: initscripts-locales = %{version}-%{release}
Requires: initscripts-man = %{version}-%{release}
Requires: initscripts-services = %{version}-%{release}
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : pkg-config
BuildRequires : popt-dev
BuildRequires : systemd
Patch1: support-interface-scriptlets.patch
Patch2: relocate-dhclient-leases-to-var-run.patch
Patch3: dhclient-restrict-interfaces-to-those-on-c.patch
Patch4: support-interface-promisc.patch
Patch5: 0001-dhclient-remove-1-arg.patch
Patch6: 0001-force-delay-check-link-down.patch
Patch7: run-ifdown-on-all-interfaces.patch
Patch8: sysconfig-affirmative-check-for-link-carrier.patch
Patch9: sysconfig-unsafe-usage-of-linkdelay-variable.patch
Patch10: ipv6-static-route-support.patch
Patch11: ifup-eth-stop-waiting-if-link-is-up.patch
Patch12: run-dhclient-as-daemon-for-ipv6.patch
Patch13: ifup-alias-scope.patch
Patch14: 0001-python2-upgrade-python3.patch

%description
The initscripts package contains basic system scripts used
during a boot of the system. It also contains scripts which
activate and deactivate most network interfaces.

%package bin
Summary: bin components for the initscripts package.
Group: Binaries
Requires: initscripts-libexec = %{version}-%{release}
Requires: initscripts-config = %{version}-%{release}
Requires: initscripts-services = %{version}-%{release}

%description bin
bin components for the initscripts package.


%package config
Summary: config components for the initscripts package.
Group: Default

%description config
config components for the initscripts package.


%package libexec
Summary: libexec components for the initscripts package.
Group: Default
Requires: initscripts-config = %{version}-%{release}

%description libexec
libexec components for the initscripts package.


%package locales
Summary: locales components for the initscripts package.
Group: Default

%description locales
locales components for the initscripts package.


%package man
Summary: man components for the initscripts package.
Group: Default

%description man
man components for the initscripts package.


%package services
Summary: services components for the initscripts package.
Group: Systemd services

%description services
services components for the initscripts package.


%prep
%setup -q -n initscripts-9.49.46
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568255952
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1568255952
rm -rf %{buildroot}
make ROOT=$RPM_BUILD_ROOT SUPERUSER=`id -un` SUPERGROUP=`id -gn` mandir=%{_mandir} install
%find_lang initscripts
## install_append content
%find_lang %{name}
rm -f $RPM_BUILD_ROOT/etc/sysconfig/init.s390
touch $RPM_BUILD_ROOT/etc/crypttab
chmod 600 $RPM_BUILD_ROOT/etc/crypttab
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/systemd/rhel-autorelabel
/usr/lib/systemd/rhel-configure
/usr/lib/systemd/rhel-dmesg
/usr/lib/systemd/rhel-domainname
/usr/lib/systemd/rhel-import-state
/usr/lib/systemd/rhel-loadmodules
/usr/lib/systemd/rhel-readonly
/usr/lib/udev/rename_device
/usr/lib/udev/udev-kvm-check
/var/log/btmp
/var/log/wtmp
/var/run/utmp

%files bin
%defattr(-,root,root,-)
/usr/bin/ipcalc
/usr/bin/usleep
/usr/sbin/consoletype
/usr/sbin/genhostid
/usr/sbin/ifdown
/usr/sbin/ifup
/usr/sbin/netreport
/usr/sbin/ppp-watch
/usr/sbin/service
/usr/sbin/sushell
/usr/sbin/sys-unconfig
/usr/sbin/usernetctl

%files config
%defattr(-,root,root,-)
/usr/lib/sysctl.d/00-system.conf
/usr/lib/tmpfiles.d/initscripts.conf
/usr/lib/udev/rules.d/60-net.rules
/usr/lib/udev/rules.d/81-kvm-rhel.rules

%files libexec
%defattr(-,root,root,-)
/usr/libexec/initscripts/brandbot

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/consoletype.1
/usr/share/man/man1/genhostid.1
/usr/share/man/man1/ipcalc.1
/usr/share/man/man1/netreport.1
/usr/share/man/man1/usleep.1
/usr/share/man/man8/ifdown.8
/usr/share/man/man8/ifup.8
/usr/share/man/man8/ppp-watch.8
/usr/share/man/man8/service.8
/usr/share/man/man8/sushell.8
/usr/share/man/man8/sys-unconfig.8
/usr/share/man/man8/usernetctl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/brandbot.path
/usr/lib/systemd/system/brandbot.service
/usr/lib/systemd/system/rhel-autorelabel-mark.service
/usr/lib/systemd/system/rhel-autorelabel.service
/usr/lib/systemd/system/rhel-configure.service
/usr/lib/systemd/system/rhel-dmesg.service
/usr/lib/systemd/system/rhel-domainname.service
/usr/lib/systemd/system/rhel-import-state.service
/usr/lib/systemd/system/rhel-loadmodules.service
/usr/lib/systemd/system/rhel-readonly.service

%files locales -f initscripts.lang
%defattr(-,root,root,-)

