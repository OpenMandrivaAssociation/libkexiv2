#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define major 5
%define oldlibname %mklibname KF5KExiv2_ %{major}
%define libname %mklibname KExiv2Qt6
%define devname %mklibname KExiv2Qt6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE wrapper around exiv2 library
Name:		libkexiv2
Version:	25.12.0
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/libkexiv2/-/archive/%{gitbranch}/libkexiv2-%{gitbranchd}.tar.bz2#/libkexiv2-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	pkgconfig(exiv2)
Requires:	%{libname} = %{EVRD}
%rename plasma6-%{name}

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%{_datadir}/qlogging-categories6/libkexiv2.categories

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	%{name} library for Qt 6
Group:		System/Libraries
Requires:	plasma6-%{name} = %{EVRD}
# Not really the same, but we have to get rid of obsolete cruft at some point...
Obsoletes:	%{mklibname KF5Exiv2} < %{EVRD}

%description -n %{libname}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files -n %{libname}
%{_libdir}/libKExiv2Qt6.so.%{major}*
%{_libdir}/libKExiv2Qt6.so.0

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name} for Qt 6
Group:		Development/KDE and Qt
Requires:	pkgconfig(exiv2)
Requires:	%{libname} = %{EVRD}
Requires:	plasma6-%{name} = %{EVRD}
# Not really the same, but we have to get rid of obsolete cruft at some point...
Obsoletes:	%{mklibname -d KF5Exiv2} < %{EVRD}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on libkexiv2.

%files -n %{devname}
%{_includedir}/KExiv2Qt6
%{_libdir}/libKExiv2Qt6.so
%{_libdir}/cmake/KExiv2Qt6

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n libkexiv2-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=6 \
        -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
