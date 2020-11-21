%define major 5
%define libname %mklibname KF5KExiv2_ %{major}
%define devname %mklibname KF5KExiv2 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE wrapper around exiv2 library
Name:		libkexiv2
Version:	20.11.80
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(exiv2)
Conflicts:	%{_lib}kexiv2_9 < 2:4.6.90
Obsoletes:	libkexiv2 < 2:15.12.0
Requires:	%{libname} = %{EVRD}

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%{_datadir}/qlogging-categories5/libkexiv2.categories

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{_lib}kexiv2_10 < 2:4.8.90
Obsoletes:	%{mklibname kexiv2_ 11} < 2:15.12.0
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files -n %{libname}
%{_libdir}/libKF5KExiv2.so.%{major}*
%{_libdir}/libKF5KExiv2.so.15*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	pkgconfig(exiv2)
Requires:	%{libname} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.10
Conflicts:	libkexiv2-devel < 2:4.12.1
Obsoletes:	libkexiv2-devel < 2:4.12.1
Obsoletes:	%{mklibname kexiv2 -d} < 2:15.12.0

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on libkexiv2.

%files -n %{devname}
%{_includedir}/KF5/KExiv2
%{_includedir}/KF5/libkexiv2_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5KExiv2

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
