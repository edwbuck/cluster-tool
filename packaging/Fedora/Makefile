RPMSPEC_FILE := cluster-tool.spec

SHELL := /usr/bin/bash

PACKAGE_ARCH=$(shell rpm $(SRPM_DEFS) -q --qf '%{ARCH}' --specfile $(RPMSPEC_FILE))
PACKAGE_NAME=$(shell rpm $(SRPM_DEFS) -q --qf '%{NAME}' --specfile $(RPMSPEC_FILE))
ifeq ($(shell rpm ${SRPM_DEFS} -q --qf '%{NOSOURCE}' --specfile $(RPMSPEC_FILE)),'(none)')
  PACKAGE_NOSOURCE=$(shell rpm $(SRPM_DEFS) -q --qf '%{NOSOURCE}' --specfile $(RPMSPEC_FILE))
endif
PACKAGE_VERSION=$(shell rpm $(SRPM_DEFS) -q --qf '%{VERSION}' --specfile $(RPMSPEC_FILE))
PACKAGE_RELEASE=$(shell rpm $(SRPM_DEFS) -q --qf '%{RELEASE}' --specfile $(RPMSPEC_FILE))

RPM_FLAG_DEBUG_PACKAGE_DEF=--define='debug_package %{nil}'

SRPM_TOPDIR=$(patsubst %/,%, $(dir $(abspath  $(lastword $(MAKEFILE_LIST)))))/srpm
SRPM_TOPDIR_DEF=--define='_topdir $(SRPM_TOPDIR)'
SRPM_DEFS=$(RPM_FLAG_DEBUG_PACKAGE_DEF) $(SRPM_TOPDIR_DEF)

SRPM_RPMDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_rpmdir}")
SRPM_SRCDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_sourcedir}")
SRPM_SPECDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_specdir}")
SRPM_SRPMDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_srcrpmdir}")
SRPM_BUILDDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_builddir}")
SRPM_BUILDROOTDIR=$(shell rpm $(SRPM_DEFS) --eval "%{_buildrootdir}")
SRPM_RPMBUILD_DIRS=$(SRPM_RPMDIR) $(SRPM_SRCDIR) $(SRPM_SPECDIR) $(SRPM_SRPMDIR) $(SRPM_BUILDDIR) $(SRPM_BUILDROOTDIR)


SRPM_PACKAGE=$(shell rpm --define 'NAME $(PACKAGE_NAME)' --define 'VERSION $(PACKAGE_VERSION)' --define 'RELEASE $(PACKAGE_RELEASE)' --eval '%{NAME}-%{VERSION}-%{RELEASE}.$(if $(PACKAGE_NOSOURCE),nosrc.rpm,src.rpm)')


RPM_TOPDIR=$(patsubst %/,%, $(dir $(abspath  $(lastword $(MAKEFILE_LIST)))))/rpm
RPM_TOPDIR_DEF=--define='_topdir $(RPM_TOPDIR)'
RPM_DEFS=$(RPM_FLAG_DEBUG_PACKAGE_DEF) $(RPM_TOPDIR_DEF)

RPM_RPMDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_rpmdir}")
RPM_SRCDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_sourcedir}")
RPM_SPECDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_specdir}")
RPM_SRPMDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_srcrpmdir}")
RPM_BUILDDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_builddir}")
RPM_BUILDROOTDIR=$(shell rpm ${RPM_TOPDIR_DEF} --eval "%{_buildrootdir}")
RPM_RPMBUILD_DIRS=$(RPM_RPMDIR) $(RPM_SRCDIR) $(RPM_SPECDIR) $(RPM_SRPMDIR) $(RPM_BUILDDIR) $(RPM_BUILDROOTDIR)

RPM_PACKAGE=$(shell rpm --define 'NAME $(PACKAGE_NAME)' --define 'VERSION $(PACKAGE_VERSION)' --define 'RELEASE $(PACKAGE_RELEASE)' --define 'ARCH $(PACKAGE_ARCH)' --eval '%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm')
package: $(RPM_PACKAGE) $(SRPM_PACKAGE)

$(RPM_PACKAGE): $(SRPM_PACKAGE)
	mkdir -p $(RPM_RPMBUILD_DIRS)
	rpm $(RPM_DEFS) --install $(SRPM_PACKAGE)
	rpmbuild $(RPM_DEFS) -bb $(RPM_SPECDIR)/$(RPMSPEC_FILE)
	cp $(RPM_RPMDIR)/$(PACKAGE_ARCH)/$(RPM_PACKAGE) $(RPM_PACKAGE)

$(SRPM_PACKAGE): $(RPMSPEC_FILE) ../../cluster-tool build-Makefile
	mkdir -p $(SRPM_RPMBUILD_DIRS)
	cp $(RPMSPEC_FILE) $(SRPM_SPECDIR)/$(RPMSPEC_FILE)
	cp ../../cluster-tool $(SRPM_SRCDIR)/cluster-tool
	cp ./build-Makefile $(SRPM_SRCDIR)/Makefile
	rpmbuild -bs $(SRPM_TOPDIR_DEF) $(SRPM_SPECDIR)/$(RPMSPEC_FILE)
	cp $(SRPM_SRPMDIR)/$(SRPM_PACKAGE) $(SRPM_PACKAGE)
	
clean:
	rm -rf $(RPM_TOPDIR) $(SRPM_TOPDIR) *.rpm
