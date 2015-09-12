%define major 11
%define libname %mklibname kexiv2_ %{major}
%define devname %mklibname kexiv2 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE4 wrapper around exiv2 library
Name:		libkexiv2
Version:	15.08.0
Release:	2
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
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
