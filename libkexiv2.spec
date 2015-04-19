%define major 11
%define libname %mklibname kexiv2_ %{major}
%define devname %mklibname kexiv2 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE4 wrapper around exiv2 library
Name:		libkexiv2
Version:	15.04.0
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	automoc4
Conflicts:	%{_lib}kexiv2_9 < 2:4.6.90

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%doc AUTHORS COPYING NEWS README TODO
%{_kde_appsdir}/libkexiv2/data/topicset.iptc-subjectcode.xml

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{_lib}kexiv2_10 < 2:4.8.90
Requires:	%{name}

%description -n %{libname}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files -n %{libname}
%{_kde_libdir}/libkexiv2.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	pkgconfig(exiv2)
Requires:	%{libname} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.10
Conflicts:	libkexiv2-devel < 2:4.12.1
Obsoletes:	libkexiv2-devel < 2:4.12.1

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on libkexiv2.

%files -n %{devname}
%{_includedir}/libkexiv2
%{_libdir}/cmake/libkexiv2-*/*.cmake
%{_libdir}/pkgconfig/libkexiv2.pc
%{_libdir}/libkexiv2.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:14.12.0-1
- New version 14.12.0

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1
- Rename devel package according to our policy
- Update files

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- Library should require main package

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97
- Update summary

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95
- New library major 11

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 762492
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762492
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758081
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744560
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739315
- New upstream tarball $NEW_VERSION

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 732315
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80

* Tue Aug 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 696279
- New version 4.7.41

* Sun Jul 31 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.40-1
+ Revision: 692506
- Fix BR
- import libkexiv2


* Sun Mar 04 2007 Angelo Naselli <anaselli@mandriva.org> 0.1.1-2mdv2007.0
+ Revision: 132340
- rebuilt for new libexiv2

* Sat Feb 24 2007 Angelo Naselli <anaselli@mandriva.org> 0.1.1-1mdv2007.1
+ Revision: 125441
- readded kdebase-devel
- removed kdebase-devel dependency
- new version 0.1.1

* Wed Feb 14 2007 Angelo Naselli <anaselli@mandriva.org> 0.1.0-2mdv2007.1
+ Revision: 120793
- wrong libname changed
- added right Povides field

* Mon Feb 12 2007 Angelo Naselli <anaselli@mandriva.org> 0.1.0-1mdv2007.1
+ Revision: 118993
- Import libkexiv2

* Mon Feb 12 2007 Angelo Naselli <anaselli@mandriva.org> 0.1.0mdv2007.1
- built mdk version

