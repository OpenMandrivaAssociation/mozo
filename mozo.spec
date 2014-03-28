%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-menu-editor

Summary:	Simple menu editor for MATE
Name:		mozo
Version:	1.8.0
Release:	1
Group:		System/Configuration/Other
License:	LGPLv2+
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(pygtk-2.0)
Requires:	pygtk2.0 >= 2.8.0
Requires:	python-mate-menus >= 1.6.0
%rename %{oname}

%description
Mozo is a menu editor for MATE that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README AUTHORS COPYING
%{py_puresitedir}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mozo
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/mozo.1*

