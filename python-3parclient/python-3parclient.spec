#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-3parclient
Version  : 3parclient.4.2.3
Release  : 1
URL      : file:///home/clr/stx-tar/python-3parclient-4.2.3.tar.gz
Source0  : file:///home/clr/stx-tar/python-3parclient-4.2.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: python-3parclient-python = %{version}-%{release}
Requires: python-3parclient-python3 = %{version}-%{release}
Requires: eventlet
Requires: paramiko
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : paramiko
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/python-3parclient.svg
:target: https://pypi.python.org/pypi/python-3parclient
:alt: Latest Version

%package python
Summary: python components for the python-3parclient package.
Group: Default
Requires: python-3parclient-python3 = %{version}-%{release}

%description python
python components for the python-3parclient package.


%package python3
Summary: python3 components for the python-3parclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-3parclient package.


%prep
%setup -q -n python-3parclient-4.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567649259
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
