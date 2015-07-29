# asio only ships headers, so no debuginfo package is needed
%define debug_package %{nil}

%global commit c466dc46d55755d38ee1831e95207d6b329c4976

Summary: A cross-platform C++ library for network programming
Name: asio
Version: 1.10.6
Release: 2%{?dist}
URL: https://think-async.com
Source0: https://github.com/chriskohlhoff/asio/archive/%{commit}/asio-%{commit}.tar.gz
License: Boost
Group: System Environment/Libraries
BuildRequires: autoconf
BuildRequires: automake
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
%setup -qn %{name}-%{commit}/%{name}

%build
./autogen.sh
%configure

%install
make install DESTDIR=$RPM_BUILD_ROOT nobase_includeHEADERS_INSTALL='install -D -p -m644'

%check
make %{?_smp_mflags}

%files devel
%defattr(-,root,root,-)
%doc COPYING LICENSE_1_0.txt src/doc/*
%dir %{_includedir}/asio
%{_includedir}/asio/*
%{_includedir}/asio.hpp

%changelog
* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sun Jul 26 2015 Fabio Alessandro Locati <fabio@locati.cc> -1.10.6-1
- Update to 1.10.6 version

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.10.4-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.10.4-3
- Rebuild for boost 1.57.0

* Sat Oct 11 2014 Fabio Alessandro Locati <fabiolocati@gmail.com> - 1.10.4-2
- Forgot to update the commit id

* Sat Oct 11 2014 Fabio Alessandro Locati <fabiolocati@gmail.com> - 1.10.4-1
- Update to 1.10.4 version

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Fabio Alessandro Locati <fabiolocati@gmail.com> - 1.10.3-1
- Update to 1.10.3 version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4.8-8
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.4.8-6
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.4.8-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.4.8-4
- Rebuild for Boost-1.53.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug  3 2011 Peter Robinson <pbrobinson@gmail.com> - 1.4.8-1
- Update to 1.4.8 bugfix release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Dan Horák <dan[at]danny.cz> 1.4.1-3
- fix FTBFS #538893 and #599857 (patch by Petr Machata)

* Mon Jul 27 2009 Marc Maurer <uwog@uwog.net> 1.4.1-2
- The tarball is now a gzip archive

* Mon Jul 27 2009 Marc Maurer <uwog@uwog.net> 1.4.1-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Marc Maurer <uwog@uwog.net> 1.2.0-1
- New upstream release

* Sun Apr 06 2008 Marc Maurer <uwog@uwog.net> 1.0.0-2
- Upstream removed the executable permissions on the docs

* Sun Apr 06 2008 Marc Maurer <uwog@uwog.net> 1.0.0-1
- New upstream release

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
