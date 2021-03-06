#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-ironicclient
Version  : 2.7.0
Release  : 1
URL      : file:///home/clr/stx-tar/python-ironicclient-2.7.0.tar.gz
Source0  : file:///home/clr/stx-tar/python-ironicclient-2.7.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: python-ironicclient-bin = %{version}-%{release}
Requires: python-ironicclient-python = %{version}-%{release}
Requires: python-ironicclient-python3 = %{version}-%{release}
Requires: PyYAML
Requires: appdirs >= 1.3.0
Requires: dogpile.cache >= 0.6.2
Requires: jsonschema
Requires: keystoneauth1 >= 3.4.0
Requires: osc-lib >= 1.10.0
Requires: oslo.i18n >= 3.15.3
Requires: oslo.serialization >= 2.18.0
Requires: oslo.utils >= 3.33.0
Requires: pbr
Requires: pbr >= 2.0.0
Requires: prettytable
Requires: requests
Requires: six >= 1.10.0
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pbr >= 2.0.0
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
==================================
Python bindings for the Ironic API
==================================

%package bin
Summary: bin components for the python-ironicclient package.
Group: Binaries

%description bin
bin components for the python-ironicclient package.


%package python
Summary: python components for the python-ironicclient package.
Group: Default
Requires: python-ironicclient-python3 = %{version}-%{release}

%description python
python components for the python-ironicclient package.


%package python3
Summary: python3 components for the python-ironicclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-ironicclient package.


%prep
%setup -q -n python-ironicclient-2.7.0

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569392909
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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
echo "dont need check"
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export PBR_VERSION=%{version}
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ironic

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
