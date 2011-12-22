%define old_libkexiv2 %mklibname kexiv2_ 9

Name: libkexiv2
Summary: Wrapper around exiv2 library
Version: 4.7.95
Release: 1
Epoch: 2
Group: System/Libraries
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libexiv-devel
BuildRequires: automoc4
Conflicts: %{old_libkexiv2} < 2:4.6.90

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files
%doc AUTHORS COPYING NEWS README TODO
%{_kde_appsdir}/libkexiv2/data/topicset.iptc-subjectcode.xml

#--------------------------------------------------------------------

%define kexiv2_major 10
%define	libkexiv2 %mklibname kexiv2_ %kexiv2_major

%package -n %{libkexiv2}
Summary: %{name} library
Group: System/Libraries

%description -n %{libkexiv2}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP.

%files -n %{libkexiv2}
%{_kde_libdir}/libkexiv2.so.%{kexiv2_major}*

#--------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: libexiv-devel
Requires: %libkexiv2 = %epoch:%version-%release
Conflicts: kdegraphics4-devel < 2:4.6.10

%description devel
This package contains header files needed if you wish to build applications
based on kdegraphics.

%files devel
%_includedir/libkexiv2
%_libdir/pkgconfig/libkexiv2.pc
%_libdir/libkexiv2.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

