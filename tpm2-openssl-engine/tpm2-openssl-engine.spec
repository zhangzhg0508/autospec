#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tpm2-openssl-engine
Version  : 1.0
Release  : 2
URL      : file:///home/clr/stx-tar/tpm2-openssl-engine-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/tpm2-openssl-engine-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: tpm2-openssl-engine-bin = %{version}-%{release}
Requires: tpm2-openssl-engine-lib = %{version}-%{release}
Requires: tss2
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : tss2-dev

%description
No detailed description available

%package bin
Summary: bin components for the tpm2-openssl-engine package.
Group: Binaries

%description bin
bin components for the tpm2-openssl-engine package.


%package lib
Summary: lib components for the tpm2-openssl-engine package.
Group: Libraries

%description lib
lib components for the tpm2-openssl-engine package.


%prep
%setup -q -n tpm2-openssl-engine-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567747900
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
export SOURCE_DATE_EPOCH=1567747900
rm -rf %{buildroot}
make install ENGINEDIR=%{buildroot}/%{_libdir}/openssl/engines UTILDIR=%{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/create_tpm2_key

%files lib
%defattr(-,root,root,-)
/usr/lib64/openssl/engines/libtpm2.so
