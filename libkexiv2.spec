Name:		libkexiv2
Summary:	KDE4 wrapper around exiv2 library
Version:	4.8.97
Release:	1
Epoch:		2
Group:		System/Libraries
License:	GPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	automoc4
Conflicts:	%{mklibname kexiv2_ 9} < 2:4.6.90

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%doc AUTHORS COPYING NEWS README TODO
%{_kde_appsdir}/libkexiv2/data/topicset.iptc-subjectcode.xml

#--------------------------------------------------------------------

%define kexiv2_major 11
%define libkexiv2 %mklibname kexiv2_ %{kexiv2_major}

%package -n %{libkexiv2}
Summary:	%{name} library
Group:		System/Libraries
Obsoletes:	%{mklibname kexiv2_ 10} < 2:4.8.90

%description -n %{libkexiv2}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files -n %{libkexiv2}
%{_kde_libdir}/libkexiv2.so.%{kexiv2_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	pkgconfig(exiv2)
Requires:	%{libkexiv2} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.10

%description devel
This package contains header files needed if you wish to build applications
based on kdegraphics.

%files devel
%{_includedir}/libkexiv2
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

