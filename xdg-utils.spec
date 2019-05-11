# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

%define gitdate %{nil}

Summary:	A basic desktop integration tools for any Free Desktop
Name:		xdg-utils
Version:	1.1.3
Release:	3
License:	MIT
Url:		https://www.freedesktop.org/wiki/Software/xdg-utils/
Group:		System/Base
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# git archive --format=tar --prefix xdg-utils-1.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > xdg-utils-1.1.0-$(date +%Y%m%d).tar.xz
#Source0:	xdg-utils-%{version}-%{gitdate}.tar.xz
Source0:	https://portland.freedesktop.org/download/xdg-utils-%{version}.tar.gz
Patch1:		xdg-utils-1.1.3-falkon-otter-arora.patch
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

%prep
%autosetup -p1

%build
%configure

%make scripts-clean -C scripts
%make man scripts -C scripts

%make
%make -C scripts

%install
%makeinstall_std

%files
%{_bindir}/xdg-*
%{_mandir}/man1/xdg*.*
