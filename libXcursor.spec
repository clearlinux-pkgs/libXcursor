#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libXcursor
Version  : 1.2.0
Release  : 20
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXcursor-1.2.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXcursor-1.2.0.tar.gz
Source1  : http://xorg.freedesktop.org/releases/individual/lib/libXcursor-1.2.0.tar.gz.sig
Summary  : X Cursor Library
Group    : Development/Tools
License  : HPND
Requires: libXcursor-lib = %{version}-%{release}
Requires: libXcursor-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32fixesproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xrender)
BuildRequires : pkgconfig(fixesproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrender)

%description
libXcursor - X Window System Cursor management library
------------------------------------------------------

%package dev
Summary: dev components for the libXcursor package.
Group: Development
Requires: libXcursor-lib = %{version}-%{release}
Provides: libXcursor-devel = %{version}-%{release}
Requires: libXcursor = %{version}-%{release}

%description dev
dev components for the libXcursor package.


%package dev32
Summary: dev32 components for the libXcursor package.
Group: Default
Requires: libXcursor-lib32 = %{version}-%{release}
Requires: libXcursor-dev = %{version}-%{release}

%description dev32
dev32 components for the libXcursor package.


%package lib
Summary: lib components for the libXcursor package.
Group: Libraries
Requires: libXcursor-license = %{version}-%{release}

%description lib
lib components for the libXcursor package.


%package lib32
Summary: lib32 components for the libXcursor package.
Group: Default
Requires: libXcursor-license = %{version}-%{release}

%description lib32
lib32 components for the libXcursor package.


%package license
Summary: license components for the libXcursor package.
Group: Default

%description license
license components for the libXcursor package.


%prep
%setup -q -n libXcursor-1.2.0
cd %{_builddir}/libXcursor-1.2.0
pushd ..
cp -a libXcursor-1.2.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604442509
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604442509
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXcursor
cp %{_builddir}/libXcursor-1.2.0/COPYING %{buildroot}/usr/share/package-licenses/libXcursor/922036fd1806bf5b46951520f13bcd83e4b2ca6d
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xcursor/Xcursor.h
/usr/lib64/libXcursor.so
/usr/lib64/pkgconfig/xcursor.pc
/usr/share/man/man3/Xcursor.3
/usr/share/man/man3/XcursorCursorsCreate.3
/usr/share/man/man3/XcursorCursorsDestroy.3
/usr/share/man/man3/XcursorFilenameLoad.3
/usr/share/man/man3/XcursorFilenameLoadAllImages.3
/usr/share/man/man3/XcursorFilenameLoadCursor.3
/usr/share/man/man3/XcursorFilenameLoadImage.3
/usr/share/man/man3/XcursorFilenameLoadImages.3
/usr/share/man/man3/XcursorFilenameSave.3
/usr/share/man/man3/XcursorFilenameSaveImages.3
/usr/share/man/man3/XcursorGetDefaultSize.3
/usr/share/man/man3/XcursorGetTheme.3
/usr/share/man/man3/XcursorImageCreate.3
/usr/share/man/man3/XcursorImageDestroy.3
/usr/share/man/man3/XcursorImagesCreate.3
/usr/share/man/man3/XcursorImagesDestroy.3
/usr/share/man/man3/XcursorLibraryLoadCursor.3
/usr/share/man/man3/XcursorLibraryLoadCursors.3
/usr/share/man/man3/XcursorLibraryLoadImage.3
/usr/share/man/man3/XcursorLibraryLoadImages.3
/usr/share/man/man3/XcursorSetDefaultSize.3
/usr/share/man/man3/XcursorSetTheme.3
/usr/share/man/man3/XcursorShapeLoadCursor.3
/usr/share/man/man3/XcursorShapeLoadCursors.3
/usr/share/man/man3/XcursorShapeLoadImage.3
/usr/share/man/man3/XcursorShapeLoadImages.3
/usr/share/man/man3/XcursorSupportsARGB.3
/usr/share/man/man3/XcursorXcFileLoad.3
/usr/share/man/man3/XcursorXcFileLoadAllImages.3
/usr/share/man/man3/XcursorXcFileLoadImage.3
/usr/share/man/man3/XcursorXcFileLoadImages.3
/usr/share/man/man3/XcursorXcFileSave.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXcursor.so
/usr/lib32/pkgconfig/32xcursor.pc
/usr/lib32/pkgconfig/xcursor.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXcursor.so.1
/usr/lib64/libXcursor.so.1.0.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXcursor.so.1
/usr/lib32/libXcursor.so.1.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXcursor/922036fd1806bf5b46951520f13bcd83e4b2ca6d
