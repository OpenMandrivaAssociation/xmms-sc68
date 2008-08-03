%define	name	xmms-sc68
%define	version	2.1.0
%define release	%mkrel 8
%define oname xmms68

Summary:	SC68 - Atari ST and Amiga music player
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
Url:		http://sc68.atari.org/
Source:		http://prdownloads.sourceforge.net/sc68/%{oname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	xmms
BuildRequires:	libxmms-devel
BuildRequires:	libsc68-devel

%description
sc68 is an Atari ST and Amiga music player.  It can play special files
(.sc68). This file encapsulates orgininal music files and possibly the
program to play it.  You can find a very large collection of this file
on sc68 official web site <http://sashipa.ben.free.fr/sc68>.

This package contains an input plugin for XMMS.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/*a

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%_libdir/xmms/Input/libxmms68.so


