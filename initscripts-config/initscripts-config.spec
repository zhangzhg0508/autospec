#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : initscripts-config
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/initscripts-config-1.0.tar.gz
Source0  : file:///home/clear/tar/initscripts-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: initscripts-config-data = %{version}-%{release}
Requires: initscripts-config-services = %{version}-%{release}
Patch1: 0001-add_makefile.patch

%description
No detailed description available

%package data
Summary: data components for the initscripts-config package.
Group: Data

%description data
data components for the initscripts-config package.


%package services
Summary: services components for the initscripts-config package.
Group: Systemd services

%description services
services components for the initscripts-config package.


%prep
%setup -q -n initscripts-config-1.0
%patch1 -p1

%build
## build_prepend content
%define _sysconfdir /usr/local/etc
%define _unitdir /usr/lib/systemd/system/
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568281402
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
export SOURCE_DATE_EPOCH=1568281402
rm -rf %{buildroot}
%{__install} -d  644 %{buildroot}%{_datadir}/starlingx/
## install_append content
%{__install} -d  644 %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -d  755 %{buildroot}%{_initddir}
%{__install} -d  644 %{buildroot}%{_unitdir}
%{__install} -m  644 sysctl.conf              %{buildroot}%{_datadir}/starlingx/stx.sysctl.conf
%{__install} -m  644 sysconfig-network.conf   %{buildroot}%{_sysconfdir}/sysconfig/network
%{__install} -m  755 mountnfs.sh              %{buildroot}%{_initddir}/mountnfs
%{__install} -m  644 mountnfs.service         %{buildroot}%{_unitdir}/mountnfs.service
%post
if [ $1 -eq 1 ] ; then
cp -f %{_datadir}/starlingx/stx.sysctl.conf %{_sysconfdir}/sysctl.conf
chmod 644 %{_sysconfdir}/sysctl.conf
fi
%{_bindir}/systemctl enable mountnfs.service  > /dev/null 2>&1 || :
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/rc.d/init.d/mountnfs
/usr/local/etc/sysconfig/network

%files data
%defattr(-,root,root,-)
/usr/share/starlingx/stx.sysctl.conf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/mountnfs.service
