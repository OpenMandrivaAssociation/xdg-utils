# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

%define gitdate 20150415

Summary:	A basic desktop integration tools for any Free Desktop
Name:		xdg-utils
Version:	1.1.1
Release:	5
License:	MIT
Url:		http://portland.freedesktop.org/wiki/
Group:		System/Base
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# git archive --format=tar --prefix xdg-utils-1.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > xdg-utils-1.1.0-$(date +%Y%m%d).tar.xz
#Source0:	xdg-utils-%{version}-%{gitdate}.tar.xz
Source0:	http://portland.freedesktop.org/download/%{name}-%{version}.tar.gz
Patch1:		xdg-utils-1.1.0-lxqt.patch
Patch2:		xdg-utils-1.1.0-enable-additional-scripts.patch
# (tpg) patches from upstream git
Patch3:		0000-Check-for-WAYLAND_DISPLAY-as-well-as-DISPLAY.patch
Patch4:		0001-xdg-utils-common-bump-version-number.patch
Patch5:		0002-ChangeLog-tag-current-version-as-unreleased.patch
Patch6:		0003-xdg-open-improve-fallbacks-add-open_generic-almost-e.patch
Patch7:		0004-xdg-open-standardize-output-redirection-style.patch
Patch8:		0005-xdg-screensaver-Add-cinnamon-screensaver-D-Bus-API-s.patch
Patch9:		0006-add-changelog-for-prior-commit.patch
Patch10:	0007-xdg-mime-support-for-KDE-Frameworks-5.6.patch
Patch11:	0008-changelog-for-prior-commit.patch
Patch12:	0009-xdg-mime-does-not-write-the-file-it-reads-in-a-query.patch
Patch13:	0010-xdg-mime-ensure-check_mimeapps_list-returns-only-pri.patch
Patch14:	0011-xdg-open-prefer-open_generic_xdg_x_scheme_handler-ov.patch

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

%files
%{_bindir}/xdg-*
%{_mandir}/man1/xdg*.*
