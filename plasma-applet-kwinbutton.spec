%define oname kwinbutton
%define sname kwinbuttonapplet-improved
%define kdeid 143971

Summary:	Plasma applet that emulates a button from the window title of the active window
Name:		plasma-applet-%{oname}
Version:	0.6
Release:	2
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php/KWin+Button+applet+improved?content=%{kdeid}
Source0:	http://kde-apps.org/CONTENT/content-files/%{kdeid}-%{sname}-%{version}.tar.gz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description
Plasma applet that emulates a button from the window title of the active
window. This is forked ("improved") by Alberto Pajuelo Montes version.

%files
%doc COPYING
%{_kde_libdir}/kde4/plasma_applet_kwinbutton.so
%{_kde_services}/%{name}.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{sname}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

