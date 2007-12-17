%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

%define	name tapiocaui
%define	version 0.3.0
%define	release %mkrel 3

Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)		
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/tapioca-voip/%{name}-%{version}.tar.bz2
Requires: 	libfarsight
BuildRequires: gtk2-devel 
BuildRequires: glib2-devel 
BuildRequires: dbus-devel 
BuildRequires: hal-devel 
BuildRequires: farsight-devel 
BuildRequires: tapioca-devel
BuildRequires: libxml-devel

%description

Tapioca is a framework for Voice over IP (VoIP) and 
Instant Messaging (IM). Its main goal is to provide 
an easy way for developing and using VoIP and IM 
services in any kind of application. It was designed 
to be cross-platform, lightweight, thread-safe, having 
mobile devices and applications in mind.

	Tapioca's main goals are:
	
 * Create a solution that integrates all components 
used by VoIP and IM applications in a single, reliable 
and easy to use framework, which is able to work on different 
platforms.

 * Spare resources, providing central services for multiple 
applications. Eg.: The control of all incoming and outgoing SIP 
requests are managed by the SIP service, avoiding the creation of
 one SIP stack and allocation of a network port for each SIP-based 
application.

 * Reduce the overhead of control layers and library dependencies. 

%files
%defattr(-,root,root)
%{_bindir}/tapiocaui
%{_datadir}/applications/tapiocaui.desktop
%{_datadir}/pixmaps/tapiocaui.png
%{_datadir}/pixmaps/tapiocaui/call.png
%{_datadir}/pixmaps/tapiocaui/call_end.png
%{_datadir}/pixmaps/tapiocaui/call_hold.png
%{_datadir}/pixmaps/tapiocaui/call_over.png
%{_datadir}/pixmaps/tapiocaui/call_unhold.png
%{_datadir}/pixmaps/tapiocaui/icon_add_contact.png
%{_datadir}/pixmaps/tapiocaui/icon_close.png
%{_datadir}/pixmaps/tapiocaui/icon_delete.png
%{_datadir}/pixmaps/tapiocaui/icon_edit_contact.png
%{_datadir}/pixmaps/tapiocaui/icon_mic.png
%{_datadir}/pixmaps/tapiocaui/icon_search.png
%{_datadir}/pixmaps/tapiocaui/icon_sound.png
%{_datadir}/pixmaps/tapiocaui/icon_status.png
%{_datadir}/pixmaps/tapiocaui/tapioca_icon_small.png
%{_datadir}/pixmaps/tapiocaui/tapioca_title.png
%{_datadir}/pixmaps/tapiocaui/volume_off.png
%{_datadir}/pixmaps/tapiocaui/volume_on.png
%{_datadir}/tapiocaui/communication-window.glade
%{_datadir}/tapiocaui/main-window.glade
%{_datadir}/tapiocaui/new-account-dialog.glade
%{_datadir}/tapiocaui/new-buddy-dialog.glade

#--------------------------------------------------------------------

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}


%clean
rm -rf $RPM_BUILD_ROOT

