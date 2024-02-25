# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

#define gitdate 20230814
#define beta beta1

Summary:	A basic desktop integration tools for any Free Desktop
Name:		xdg-utils
Version:	1.2.1
Release:	%{?beta:0.%{beta}.}%{?gitdate:0.%{gitdate}.}1
License:	MIT
Url:		https://www.freedesktop.org/wiki/Software/xdg-utils/
Group:		System/Base
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# git archive --format=tar --prefix xdg-utils-1.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > xdg-utils-1.1.0-$(date +%Y%m%d).tar.xz
#Source0:	xdg-utils-%{version}-%{gitdate}.tar.xz
%if 0%{?gitdate:1}
Source0:	https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/master/xdg-utils-master.tar.bz2#/xdg-utils-%{gitdate}.tar.gz
%else
Source0:	https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/v%{version}%{?beta:-%{beta}}/xdg-utils-v%{version}%{?beta:-%{beta}}.tar.bz2
%endif
Patch1:		xdg-utils-1.1.3-falkon-otter-arora.patch
Patch2:		xdg-utils-1.1.0-enable-additional-scripts.patch
Patch3:		xdg-utils-find-kdesu6.patch

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
%autosetup -p1 -n %{name}-%{!?gitdate:v}%{?gitdate:master}%{!?gitdate:%{version}}%{?beta:-%{beta}}
sed -i -e 's,@LIBDIR@,%{_libdir},g' scripts/xdg-su.in

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
