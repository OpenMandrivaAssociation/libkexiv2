#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define major 5
%define oldlibname %mklibname KF5KExiv2_ %{major}
%define lib5name %mklibname KF5KExiv2
%define dev5name %mklibname KF5KExiv2 -d
%define libname %mklibname KExiv2Qt6
%define devname %mklibname KExiv2Qt6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_without qt5

Summary:	KDE wrapper around exiv2 library
Name:		libkexiv2
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/libkexiv2/-/archive/%{gitbranch}/libkexiv2-%{gitbranchd}.tar.bz2#/libkexiv2-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
%endif
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	pkgconfig(exiv2)
Requires:	%{lib5name} = %{EVRD}

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%{_datadir}/qlogging-categories5/libkexiv2.categories

#--------------------------------------------------------------------

%package -n %{lib5name}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{_lib}kexiv2_10 < 2:4.8.90
Obsoletes:	%{mklibname kexiv2_ 11} < 2:15.12.0
Obsoletes:	%{oldlibname} < 2:24.02.0
Requires:	%{name} = %{EVRD}

%description -n %{lib5name}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%if %{with qt5}
%files -n %{lib5name}
%{_libdir}/libKF5KExiv2.so.%{major}*
%{_libdir}/libKF5KExiv2.so.15*
%endif

#--------------------------------------------------------------------

%package -n %{dev5name}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	pkgconfig(exiv2)
Requires:	%{lib5name} = %{EVRD}
Obsoletes:	libkexiv2-devel < 2:4.12.1
Obsoletes:	%{mklibname kexiv2 -d} < 2:15.12.0

%description -n %{dev5name}
This package contains header files needed if you wish to build applications
based on libkexiv2.

%if %{with qt5}
%files -n %{dev5name}
%{_includedir}/KF5/KExiv2
%{_libdir}/libKF5KExiv2.so
%{_libdir}/cmake/KF5KExiv2
%endif

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	%{name} library for Qt 6
Group:		System/Libraries
Requires:	plasma6-%{name} = %{EVRD}

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

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on libkexiv2.

%files -n %{devname}
%{_includedir}/KExiv2Qt6
%{_libdir}/libKExiv2Qt6.so
%{_libdir}/cmake/KExiv2Qt6

#--------------------------------------------------------------------
%package -n plasma6-%{name}
Summary:	Logging configuration for %{name} for Qt 6
Group:		System/Libraries

%description -n plasma6-%{name}
Logging configuration for %{name} for Qt 6

%files -n plasma6-%{name}
%{_datadir}/qlogging-categories6/libkexiv2.categories

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n libkexiv2-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=6 \
        -G Ninja

%if %{with qt5}
cd ..
export CMAKE_BUILD_DIR=build-qt5
%cmake \
        -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
        -DQT_MAJOR_VERSION=5 \
        -G Ninja
%endif


%build
%ninja_build -C build

%if %{with qt5}
%ninja_build -C build-qt5
%endif

%install
%if %{with qt5}
%ninja_install -C build-qt5
%endif

%ninja_install -C build
