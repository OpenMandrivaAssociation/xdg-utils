# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

%define gitdate 20150415

Summary:	A basic desktop integration tools for any Free Desktop
Name:		xdg-utils
Version:	1.1.0
Release:	1
License:	MIT
Url:		http://portland.freedesktop.org/wiki/
Group:		System/Base
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# git archive --format=tar --prefix xdg-utils-1.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > xdg-utils-1.1.0-$(date +%Y%m%d).tar.xz
#Source0:	xdg-utils-%{version}-%{gitdate}.tar.xz
Source0:	http://portland.freedesktop.org/download/%{name}-%{version}.tar.gz
Patch1:		xdg-utils-1.1.0-lxqt.patch
Patch2:		xdg-utils-1.1.0-enable-additional-scripts.patch
BuildArch:	noarch
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gawk
BuildRequires:	lynx
BuildRequires:	xmlto
BuildRequires:	xsltproc
Requires:	desktop-file-utils
Requires:	xprop
Requires:	xset

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

Testsuite for xdg-utils is available from
http://portland.freedesktop.org/wiki/TestSuite

%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
%configure

%if %{gitdate}
%make scripts-clean -C scripts
%make man scripts -C scripts
%endif

%make
%make -C scripts

%install
%makeinstall_std
sed -i -e "s,_LIBDIR_,%{_libdir}/kde4/libexec,g" %{buildroot}/%{_bindir}/xdg-email

%files
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings
%{_bindir}/xdg-terminal
%{_mandir}/man1/xdg*.*
