# vim: shiftwidth=4 tabstop=4 autoindent expandtab:

%define release 1
Name:           cluster-tool
Version:        1.0.0
Release:        %{release}%{?dist}
Summary:        An EDF cluster setup tool.

License:        MPL2.0
URL:            http://www.edwinbuck.com/cluster-tool.html
Source0:        cluster-tool
Source1:        Makefile

BuildArch:      noarch
BuildRequires:  bash
Requires:       createrepo

%description
A tool to help EDF manual installations.


%prep
umask 022
# make build area
rm -rf ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}
mkdir ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}
# copy in sources 
install %SOURCE0 ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}
install %SOURCE1 ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}


%build
cd ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}
make all
make check

%install
rm -rf ${RPM_BUILD_ROOT}
cd ${RPM_BUILD_DIR}/${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}
%make_install PREFIX=/opt/cluster-tool


%files
#%license add-license-file-here
#%doc add-docs-here
%attr(0755,root,root) /opt/cluster-tool/bin/cluster-tool



%changelog
* Wed Feb 16 2022 Edwin Buck <edwbuck@gmail.com>
- 
