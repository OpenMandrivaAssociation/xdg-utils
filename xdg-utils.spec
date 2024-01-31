Summary:	A basic desktop integration tools for any Free Desktop
Name:		xdg-utils
Version:	1.2.0
Release:	1
License:	MIT
Url:		https://www.freedesktop.org/wiki/Software/xdg-utils/
Group:		System/Base
Source0:	https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/v%{version}/xdg-utils-v%{version}.bz2
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
Requires:	sed
Requires:	procps
Requires:	gawk
Requires:	grep
Requires:	xprop
Requires:	xset
Requires:	coreutils
Requires:	/bin/sh

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
%autosetup -p1 -n %{name}-v%{version}}

%build
%configure

make scripts-clean -C scripts
make man scripts -C scripts
%make_build

%install
%make_install

%files
%{_bindir}/xdg-*
%doc %{_mandir}/man1/xdg*.*
