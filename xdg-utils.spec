Name:		xdg-utils
Version:	1.0.2
Release:	%mkrel 3
Summary:	Interfaces and Tools to allow all applications to easily integrate with the free desktop configuration
License:	GPL
Url:		http://portland.freedesktop.org/wiki/
Group:		System/Base
Source0:	http://portland.freedesktop.org/download/%{name}-%version.tar.bz2
# (fc) 1.0.1-3mdv fix default applications for mimetype detection
Patch0:		xdg-utils-1.0.1-fixdefault.patch
# (mrl) 1.0.2-3mdv fix xdg-email looping. #32535
Patch1:		xdg-utils-1.0.2-email_loop.patch
BuildRequires:	libxslt-proc
Requires:       xprop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This version of xdg-utils contains the following commands:
xdg-desktop-menu:	command line tool for (un)installing 
			desktop menu items
xdg-desktop-icon:	command line tool for (un)installing 
			icons to the desktop
xdg-mime:	        command line tool for querying information 
			about file type handling and adding 
			descriptions for new file types
xdg-icon-resource:	command line tool for (un)installing icon resources
xdg-open:	        opens a file or URL in the user's preferred 
			application
xdg-email:	        command line tool for sending mail using the user's 
			preferred 
			e-mail composer
xdg-su:	                run a program as root after prompting for the root 
			password
xdg-screensaver:	command line tool for controlling the screensaver

Testsuite for xdg-utils is available from http://portland.freedesktop.org/wiki/TestSuite

%files
%defattr(-,root,root,-)
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_mandir}/man1/xdg-desktop-icon.*
%{_mandir}/man1/xdg-desktop-menu.*
%{_mandir}/man1/xdg-email.*
%{_mandir}/man1/xdg-icon-resource.*
%{_mandir}/man1/xdg-mime.*
%{_mandir}/man1/xdg-open.*
%{_mandir}/man1/xdg-screensaver.*

#-------------------------------------------------------------------------------#


%prep
%setup -q 
%patch0 -p1 -b .fixdefault
#%patch1 -p1 -b .email_loop

%build
%configure2_5x

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}
