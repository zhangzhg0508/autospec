#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nfv-client
Version  : 1
Release  : 1
URL      : file:///home/clear/tar/nfv-client.tgz
Source0  : file:///home/clear/tar/nfv-client.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: nfv-client-bin = %{version}-%{release}
Requires: nfv-client-python = %{version}-%{release}
Requires: nfv-client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package bin
Summary: bin components for the nfv-client package.
Group: Binaries

%description bin
bin components for the nfv-client package.


%package python
Summary: python components for the nfv-client package.
Group: Default
Requires: nfv-client-python3 = %{version}-%{release}

%description python
python components for the nfv-client package.


%package python3
Summary: python3 components for the nfv-client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nfv-client package.


%prep
%setup -q -n nfv-client

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566356247
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sw-manager

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
