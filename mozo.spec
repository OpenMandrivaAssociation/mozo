%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname	mate-menu-editor

Summary:	Simple menu editor for MATE
Name:		mozo
Version:	1.18.0
Release:	1
Group:		System/Configuration/Other
License:	LGPLv2+
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool 
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(pygobject-3.0)

Requires:	typelib(Gtk)
Requires:	python2-mate-menus >= %{url_ver}

%rename %{oname}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

Mozo is a menu editor for MATE using the freedesktop.org menu specification.

%files -f %{name}.lang
%doc README AUTHORS COPYING
%{py2_puresitedir}/*
%{_bindir}/*
%{_datadir}/applications/*
%dir %{_datadir}/mozo
%{_datadir}/mozo/*
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/mozo.1*

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

