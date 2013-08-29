%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-menu-editor

Summary:       Simple menu editor for MATE
Name:          mozo
Version:       1.6.0
Release:       2
Group:         System/Configuration/Other
License:       LGPLv2+
Url:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
BuildArch:     noarch

BuildRequires: pkgconfig(mate-doc-utils) >= 1.6.0
BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: pkgconfig(libmate-menu)
BuildRequires: pkgconfig(pygtk-2.0)

Requires:	pygtk2.0 >= 2.8.0
Requires:	python-mate-menus >= 1.6.0

%rename %{oname}

%description
Mozo is a menu editor for MATE that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q -n %{oname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %oname --all-name


%files -f %{oname}.lang
%doc README AUTHORS COPYING
%{py_puresitedir}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mozo
%{_iconsdir}/hicolor/*/*/*

