%define tis_patch_ver 7
%define _tis_build_type std
%define local_etc_pmond      %{_sysconfdir}/pmon.d
%define local_etc_goenabledd %{_sysconfdir}/goenabled.d

%define debug_package %{nil}

Name: mtce-compute
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
Summary: Compute Node Maintenance Package

Group: base
License: Apache-2.0
Packager: Wind River <info@windriver.com>
URL: unknown

Source0: %{name}-%{version}.tar.gz

BuildRequires: systemd
BuildRequires: systemd-devel
Requires: bash
Requires: /bin/systemctl
Requires: qemu-kvm-ev

%description
Maintenance support files for compute-only node type

%prep
%setup

%build

%install
make install buildroot=%{buildroot} _sysconfdir=%{_sysconfdir} _unitdir=%{_unitdir} _datarootdir=%{_datarootdir}

%post
/bin/systemctl enable goenabled-worker.service
/bin/systemctl enable qemu_clean.service

%files
%defattr(-,root,root,-)

%{_sysconfdir}/init.d/goenabledWorker
%{local_etc_goenabledd}/virt-support-goenabled.sh
%{_unitdir}/goenabled-worker.service

%license %{_datarootdir}/licenses/mtce-compute-1.0/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT
