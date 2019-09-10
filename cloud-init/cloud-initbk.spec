%define tis_patch_ver 4
%define _tis_build_type std
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?license: %global license %%doc}

# The only reason we are archful is because dmidecode is ExclusiveArch
# https://bugzilla.redhat.com/show_bug.cgi?id=1067089
%global debug_package %{nil}

Name:           cloud-init
Version:        0.7.9
Release:        24.el7.centos.1%{?_tis_dist}.%{tis_patch_ver}
Summary:        Cloud instance init scripts

Group:          System Environment/Base
License:        Apache-2.0
URL:            http://launchpad.net/cloud-init
Source0:        https://launchpad.net/cloud-init/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        cloud-init-rhel.cfg
Source2:        cloud-init-README.rhel
Source3:        cloud-init-tmpfiles.conf

# The following line stops 'rdopkg update-patches' from inserting Patch
# directives in the middle of our Source directives.
#
# patches_base=0.7.9
Patch0001: 0001-configuration-changes-for-RHEL-package.patch
Patch0002: 0002-do-not-use-git-to-determine-version.patch
Patch0003: 0003-util-teach-write_file-about-copy_mode-option.patch
Patch0004: 0004-Do-not-write-NM_CONTROLLED-no-in-generated-interface.patch
Patch0005: 0005-url_helper-fail-gracefully-if-oauthlib-is-not-availa.patch
Patch0006: 0006-rsyslog-replace-with-stop.patch
Patch0007: 0007-OpenStack-Use-timeout-and-retries-from-config-in-get.patch
Patch0008: 0008-correct-errors-in-cloudinit-net-sysconfig.py.patch
Patch0009: 0009-net-do-not-raise-exception-for-3-nameservers.patch
Patch0010: 0010-net-support-both-ipv4-and-ipv6-gateways-in-sysconfig.patch
Patch0011: 0011-systemd-replace-generator-with-unit-conditionals.patch
Patch0012: 0012-OpenStack-add-dvs-to-the-list-of-physical-link-types.patch
Patch0013: 0013-Bounce-network-interface-for-Azure-when-using-the-bu.patch
Patch0014: 0014-limit-permissions-on-def_log_file.patch
Patch0015: 0015-remove-tee-command-from-logging-configuration.patch
Patch0016: 0016-add-power-state-change-module-to-cloud_final_modules.patch
Patch0017: 0017-sysconfig-Raise-ValueError-when-multiple-default-gat.patch
Patch0018: 0018-Fix-dual-stack-IPv4-IPv6-configuration-for-RHEL.patch
Patch0019: 0019-Add-missing-sysconfig-unit-test-data.patch
Patch0020: 0020-Fix-ipv6-subnet-detection.patch
# Not applied to work around additional issues related to rhbz#1474226
#Patch0021: 0021-azure-ensure-that-networkmanager-hook-script-runs.patch
Patch0022: 0022-RHEL-CentOS-Fix-default-routes-for-IPv4-IPv6-configu.patch
Patch0023: 0023-DatasourceEc2-add-warning-message-when-not-on-AWS.patch
Patch0024: 0024-Identify-Brightbox-as-an-Ec2-datasource-user.patch
Patch0025: 0025-AliYun-Enable-platform-identification-and-enable-by-.patch
Patch0026: 0026-Fix-alibaba-cloud-unit-tests-to-work-with-0.7.9.patch
Patch0027: 0027-Fix-eni-rendering-of-multiple-IPs-per-interface.patch
Patch0028: 0028-systemd-create-run-cloud-init-enabled.patch
Patch0029: 0029-support-loopback-as-a-device-type.patch
Patch0030: 0030-sysconfig-include-GATEWAY-value-if-set-in-subnet.patch
Patch0031: 0031-rh_subscription-Perform-null-checks-for-enabled-and-.patch
Patch0032: 0032-net-Allow-for-NetworkManager-configuration.patch
Patch0033: 0033-Render-DNS-and-DOMAIN-lines-for-sysconfig.patch
Patch0034: 0034-Start_cloud_init_after_dbus.patch
Patch0035: 0035-sysconfig-Render-IPV6_DEFAULTGW-correctly.patch
Patch0036: 0036-sysconfig-Don-t-write-BOOTPROTO-dhcp-for-ipv6-dhcp.patch
Patch0037: 0037-sysconfig-Fix-traceback.patch
Patch0038: 0038-Fix-bug-that-resulted-in-an-attempt-to-rename-bonds.patch
Patch0039: 0039-azure-Fix-publishing-of-hostname.patch
# For bz#1568717 - Add patch to bounce NICs in Azure/update DNS [rhel-7.5.z]
Patch40: ci-Revert-azure-Fix-publishing-of-hostname.patch
# For bz#1568717 - Add patch to bounce NICs in Azure/update DNS [rhel-7.5.z]
Patch41: ci-DataSourceAzure.py-use-hostnamectl-to-set-hostname.patch
# For bz#1578702 - cloud-init-0.7.9-9.el7_4.6 breaks IPv4/IPv6 dual-stack EC2 instances in AWS [rhel-7.5.z]
Patch42: ci-sysconfig-Don-t-disable-IPV6_AUTOCONF.patch

Patch0999: cloud-init-add-centos-os.patch

# WRS patches
Patch2000: cloud-init-interactive-parted.patch

# Deal with noarch -> arch
# https://bugzilla.redhat.com/show_bug.cgi?id=1067089
Obsoletes:      cloud-init < 0.7.5-3

BuildRequires:  python-dev
BuildRequires:  setuptools
BuildRequires:  systemd
BuildRequires:  git

%ifarch %{?ix86} x86_64 ia64
Requires:       dmidecode
%endif
Requires:       e2fsprogs
Requires:       iproute
Requires:       libselinux-python
Requires:       net-tools
Requires:       policycoreutils-python
Requires:       procps
Requires:       python-configobj
Requires:       python-jinja2
Requires:       python-jsonpatch
Requires:       python-prettytable
Requires:       python-requests
Requires:       python-setuptools
Requires:       PyYAML
Requires:       pyserial
Requires:       shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.


%prep
# on el7, autosetup -S git was failing with patches that
# create new files.  rpm 4.11.3 and later has -S git_am, but
# el7 only has 4.11.1.
%autosetup -p1 -n %{name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Don't ship the tests
rm -r $RPM_BUILD_ROOT%{python_sitelib}/tests

mkdir -p $RPM_BUILD_ROOT/var/lib/cloud

# /run/cloud-init needs a tmpfiles.d entry
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p rhel/cloud-init-tmpfiles.conf $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf

# We supply our own config file since our software differs from Ubuntu's.
cp -p rhel/cloud.cfg $RPM_BUILD_ROOT/%{_sysconfdir}/cloud/cloud.cfg

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf

# Make installed NetworkManager hook name less generic
mv $RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d/hook-network-manager \
   $RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d/cloud-init-azure-hook

# Install our own systemd units (rhbz#1440831)
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp rhel/systemd/* $RPM_BUILD_ROOT%{_unitdir}/


%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    # Enabled by default per "runs once then goes away" exception
    /bin/systemctl enable cloud-config.service     >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-final.service      >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-init.service       >/dev/null 2>&1 || :
    /bin/systemctl enable cloud-init-local.service >/dev/null 2>&1 || :
elif [ $1 -eq 2 ]; then
    # Upgrade. If the upgrade is from a version older than 0.7.9-8,
    # there will be stale systemd config
    /bin/systemctl is-enabled cloud-config.service >/dev/null 2>&1 &&
      /bin/systemctl reenable cloud-config.service >/dev/null 2>&1 || :

    /bin/systemctl is-enabled cloud-final.service >/dev/null 2>&1 &&
      /bin/systemctl reenable cloud-final.service >/dev/null 2>&1 || :

    /bin/systemctl is-enabled cloud-init.service >/dev/null 2>&1 &&
      /bin/systemctl reenable cloud-init.service >/dev/null 2>&1 || :

    /bin/systemctl is-enabled cloud-init-local.service >/dev/null 2>&1 &&
      /bin/systemctl reenable cloud-init-local.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable cloud-config.service >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-final.service  >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-init.service   >/dev/null 2>&1 || :
    /bin/systemctl --no-reload disable cloud-init-local.service >/dev/null 2>&1 || :
    # One-shot services -> no need to stop
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
# One-shot services -> no need to restart


%files
%license LICENSE
%doc ChangeLog rhel/README.rhel
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg
%dir               %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d/*.cfg
%doc               %{_sysconfdir}/cloud/cloud.cfg.d/README
%dir               %{_sysconfdir}/cloud/templates
%config(noreplace) %{_sysconfdir}/cloud/templates/*
%{_unitdir}/cloud-config.service
%{_unitdir}/cloud-config.target
%{_unitdir}/cloud-final.service
%{_unitdir}/cloud-init-local.service
%{_unitdir}/cloud-init.service
%{_tmpfilesdir}/%{name}.conf
%{python_sitelib}/*
%{_libexecdir}/%{name}
%{_bindir}/cloud-init*
%doc %{_datadir}/doc/%{name}
%dir /run/cloud-init
%dir /var/lib/cloud
/etc/NetworkManager/dispatcher.d/cloud-init-azure-hook
%{_udevrulesdir}/66-azure-ephemeral.rules

%dir %{_sysconfdir}/rsyslog.d
%config(noreplace) %{_sysconfdir}/rsyslog.d/21-cloudinit.conf

%changelog
#* Tue Jun 25 2018 Johnny Hughes <johnny@centos.org> - 0.7.9-24.el7_5.1
#- Manual CentOS Debranding

* Thu May 17 2018 Miroslav Rezanina <mrezanin@redhat.com> - 0.7.9-24.el7_5.1
- ci-Revert-azure-Fix-publishing-of-hostname.patch [bz#1568717]
- ci-DataSourceAzure.py-use-hostnamectl-to-set-hostname.patch [bz#1568717]
- ci-sysconfig-Don-t-disable-IPV6_AUTOCONF.patch [bz#1578702]
- Resolves: bz#1568717
  (Add patch to bounce NICs in Azure/update DNS [rhel-7.5.z])
- Resolves: bz#1578702
  (cloud-init-0.7.9-9.el7_4.6 breaks IPv4/IPv6 dual-stack EC2 instances in AWS [rhel-7.5.z])

* Tue Feb 13 2018 Ryan McCabe <rmccabe@redhat.com> 0.7.9-24
- Set DHCP_HOSTNAME on Azure to allow for the hostname to be
  published correctly when bouncing the network.
  Resolves: rhbz#1434109

* Mon Jan 15 2018 Ryan McCabe <rmccabe@redhat.com> 0.7.9-23
- Fix a bug tha caused cloud-init to fail as a result of trying
  to rename bonds.
  Resolves: rhbz#1512247

* Mon Jan 15 2018 Ryan McCabe <rmccabe@redhat.com> 0.7.9-22
- Apply patch from -21
  Resolves: rhbz#1489270

* Mon Jan 15 2018 Ryan McCabe <rmccabe@redhat.com> 0.7.9-21
- sysconfig: Fix a potential traceback introduced in the
  0.7.9-17 build
  Resolves: rhbz#1489270

* Sun Dec 17 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-20
- sysconfig: Correct rendering for dhcp on ipv6
  Resolves: rhbz#1519271

* Thu Nov 30 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-19
- sysconfig: Fix rendering of default gateway for ipv6
  Resolves: rhbz#1492726

* Fri Nov 24 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-18
- Start the cloud-init init local service after the dbus socket is created
  so that the hostnamectl command works.
  Resolves: rhbz#1450521

* Tue Nov 21 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-17
- Correctly render DNS and DOMAIN for sysconfig
  Resolves: rhbz#1489270

* Mon Nov 20 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-16
- Disable NetworkManager management of resolv.conf if nameservers
  are specified by configuration.
  Resolves: rhbz#1454491

* Mon Nov 13 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-15
- Fix a null reference error in the rh_subscription module
  Resolves: rhbz#1498974

* Mon Nov 13 2017 Ryan McCabe <rmccabe@redhat.com> 0-7.9-14
- Include gateway if it's included in subnet configration
  Resolves: rhbz#1492726

* Sun Nov 12 2017 Ryan McCabe <rmccabe@redhat.com> 0-7.9-13
- Do proper cleanup of systemd units when upgrading from versions
  0.7.9-3 through 0.7.9-8.
  Resolves: rhbz#1465730

* Thu Nov 09 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-12
- Prevent Azure NM and dhclient hooks from running when cloud-init is
  disabled (rhbz#1474226)

* Tue Oct 31 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-11
- Fix rendering of multiple static IPs per interface file
  Resolves: rhbz#bz1497954

* Tue Sep 26 2017 Ryan McCabe <rmccabe@redhat.com> 0.7.9-10
- AliCloud: Add support for the Alibaba Cloud datasource (rhbz#1482547)

* Thu Jun 22 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-9
- RHEL/CentOS: Fix default routes for IPv4/IPv6 configuration. (rhbz#1438082)
- azure: ensure that networkmanager hook script runs (rhbz#1440831 rhbz#1460206)
- Fix ipv6 subnet detection (rhbz#1438082)

* Tue May 23 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-8
- Update patches

* Mon May 22 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-7
- Add missing sysconfig unit test data (rhbz#1438082)
- Fix dual stack IPv4/IPv6 configuration for RHEL (rhbz#1438082)
- sysconfig: Raise ValueError when multiple default gateways are present. (rhbz#1438082)
- Bounce network interface for Azure when using the built-in path. (rhbz#1434109)
- Do not write NM_CONTROLLED=no in generated interface config files (rhbz#1385172)

* Wed May 10 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-6
- add power-state-change module to cloud_final_modules (rhbz#1252477)
- remove 'tee' command from logging configuration (rhbz#1424612)
- limit permissions on def_log_file (rhbz#1424612)
- Bounce network interface for Azure when using the built-in path. (rhbz#1434109)
- OpenStack: add 'dvs' to the list of physical link types. (rhbz#1442783)

* Wed May 10 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-5
- systemd: replace generator with unit conditionals (rhbz#1440831)

* Thu Apr 13 2017 Charalampos Stratakis <cstratak@redhat.com> 0.7.9-4
- Import to RHEL 7
Resolves: rhbz#1427280

* Tue Mar 07 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-3
- fixes for network config generation
- avoid dependency cycle at boot (rhbz#1420946)

* Tue Jan 17 2017 Lars Kellogg-Stedman <lars@redhat.com> 0.7.9-2
- use timeout from datasource config in openstack get_data (rhbz#1408589)

* Thu Dec 01 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.9-1
- Rebased on upstream 0.7.9.
- Remove dependency on run-parts

* Wed Jan 06 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-8
- make rh_subscription plugin do nothing in the absence of a valid
  configuration [RH:1295953]
- move rh_subscription module to cloud_config stage

* Wed Jan 06 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-7
- correct permissions on /etc/ssh/sshd_config [RH:1296191]

* Thu Sep 03 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-6
- rebuild for ppc64le

* Tue Jul 07 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-5
- bump revision for new build

* Tue Jul 07 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-4
- ensure rh_subscription plugin is enabled by default

* Wed Apr 29 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-3
- added dependency on python-jinja2 [RH:1215913]
- added rhn_subscription plugin [RH:1227393]
- require pyserial to support smartos data source [RH:1226187]

* Fri Jan 16 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.6-2
- Rebased RHEL version to Fedora rawhide
- Backported fix for https://bugs.launchpad.net/cloud-init/+bug/1246485
- Backported fix for https://bugs.launchpad.net/cloud-init/+bug/1411829

* Fri Nov 14 2014 Colin Walters <walters@redhat.com> - 0.7.6-1
- New upstream version [RH:974327]
- Drop python-cheetah dependency (same as above bug)
