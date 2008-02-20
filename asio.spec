# asio only ships headers, so no debuginfo package is needed
%define debug_package %{nil}

Summary: A cross-platform C++ library for network programming
Name: asio
Version: 0.3.8
Release: 8%{?dist}
URL: http://sourceforge.net/projects/asio/
Source0: http://downloads.sourceforge.net/asio/asio-%{version}.tar.bz2
License: Boost
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: openssl-devel
BuildRequires: boost-devel

%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Group: Development/Libraries
Summary: Header files for asio
Requires: openssl-devel
Requires: boost-devel

%description devel
Header files you can use to develop applications with asio.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT nobase_includeHEADERS_INSTALL='install -D -p -m644'
find ./doc -type f -perm /a+x -print0 | xargs -0 chmod a-x

%check
make %{?_smp_mflags}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root,-)
%doc COPYING LICENSE_1_0.txt doc/*
%dir %{_includedir}/asio
%{_includedir}/asio/*
%{_includedir}/asio.hpp

%changelog
* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.8-8
- Autorebuild for GCC 4.3

* Sun Dec 02 2007 Marc Maurer <uwog@uwog.net> 0.3.8-7
- Rebuild to include a tarball with original timestamps

* Thu Nov 29 2007 Marc Maurer <uwog@uwog.net> 0.3.8-6
- Use release %%{?dist} tag
- Move BuildRequires to the main package
- Preserve timestamps
- Remove spurious executable permissions from documentation

* Wed Nov 28 2007 Marc Maurer <uwog@uwog.net> 0.3.8-5
- Don't require a nonexisting %%{name} package for -devel
- Add openssl-devel and boost-devel to the buildRequires list
- Remove unused post/postun sections for now
- Fix -devel description
- Use %%{version} in source URL
- Add COPYING to the doc section
- Preserve timestamps of installed files
- Use %%defattr(-,root,root,-)
- Include developer documentation
- Move the make call to the %%check section

* Sun Nov 25 2007 Marc Maurer <uwog@uwog.net> 0.3.8-4
- Don't use BA noarch

* Fri Nov 23 2007 Marc Maurer <uwog@uwog.net> 0.3.8-3
- Move the license file to the -devel package, so no
  main package will be created for now
- Added BuildArch: noarch

* Fri Nov 23 2007 Marc Maurer <uwog@uwog.net> 0.3.8-2
- Make BuildRoot fedora packaging standard compliant
- Disable building of debuginfo packages
- Include full source URL

* Wed Nov 21 2007 Marc Maurer <uwog@uwog.net> 0.3.8-1
- Initial spec file
