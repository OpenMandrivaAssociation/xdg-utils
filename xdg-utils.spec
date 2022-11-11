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
Release:	6
License:	MIT
Url:		https://www.freedesktop.org/wiki/Software/xdg-utils/
Group:		System/Base
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# git archive --format=tar --prefix xdg-utils-1.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > xdg-utils-1.1.0-$(date +%Y%m%d).tar.xz
#Source0:	xdg-utils-%{version}-%{gitdate}.tar.xz
Source0:	https://portland.freedesktop.org/download/xdg-utils-%{version}.tar.gz
Patch1:		xdg-utils-1.1.3-falkon-otter-arora.patch
Patch2:		xdg-utils-1.1.0-enable-additional-scripts.patch

# (tpg) patches from upstream
Patch10:	0000-open-for-post-1.1.3-development.patch
Patch11:	0001-xdg-open-better-pcmanfm-check-BR106636-BR106161.patch
Patch12:	0002-xdg-email-Support-for-Deepin.patch
Patch13:	0003-Restore-matching-of-older-deepin-names.patch
Patch14:	0004-xdg-open-handle-file-localhost.patch
Patch15:	0005-test-lib.sh-run-eat-xdg-open-s-exit-code.patch
Patch16:	0006-Fix-a-bug-when-xdg-terminal-needs-gsettings-to-get-t.patch
Patch17:	0007-Fixes-x-argument-which-is-the-default-for-gnome-mate.patch
Patch18:	0008-xdg-screensaver-Sanitise-window-name-before-sending-.patch
Patch19:	0009-xdg-su-fix-some-easy-TODOs.patch
Patch20:	0010-xdg-open-fix-comment-typo.patch
Patch21:	0011-Enable-cinnamon-screensaver-for-xdg-aware-desktop-en.patch
Patch22:	0012-support-digits-in-uri-scheme-regex.patch
Patch23:	0013-xdg-mime-return-correct-exit-code-for-GNOME.patch
Patch24:	0014-fixed-166-xdg-open-dose-not-search-correctly-in-dire.patch
Patch25:	0015-Fix-xdg-settings-support-for-default-web-browser-for.patch
Patch26:	0016-xdg-email-fails-on-kde-with-desktop-files-187.patch
Patch27:	0017-kill-off-whitespace-errors.patch
Patch28:	0018-remove-bashisms-from-POSIX-sh-script.patch
Patch29:	0019-command_exec-run-external-command-using-env-instead-.patch
Patch30:	0020-Replace-all-remaining-usage-of-non-portable-which-wi.patch

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
%autosetup -p1

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
