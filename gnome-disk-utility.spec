Summary:	GNOME disk utility
Name:		gnome-disk-utility
Version:	3.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-disk-utility/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	ff6e0a50a3a6aa9a8d9aa8b19d304485
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libpwquality-devel
BuildRequires:	libtool
BuildRequires:	udisks2-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	hicolor-icon-theme
Requires:	udisks2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
gnome-disk-utility provides libraries and applications for dealing
with storage devices.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en@shaw

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-disk-image-mounter
%attr(755,root,root) %{_bindir}/gnome-disks
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/gnome-disk-utility
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gnome-disk-image-mounter.1*
%{_mandir}/man1/gnome-disks.1*

