# sources from upstream git
#
# git clone git://anongit.freedesktop.org/xdg/xdg-utils
# cd xdg-utils
# git archive --format=tar --prefix=xdg-utils-20121008/ master | xz > ../xdg-utils-20121008.tar.xz
#

%define gitdate 20130218

Name:		xdg-utils
Version:	1.1.0
Release:	0.%{gitdate}.1
Summary:	A basic desktop integration tools for any Free Desktop
License:	MIT
Url:		http://portland.freedesktop.org/wiki/
Group:		System/Base
Source0:	xdg-utils-%{gitdate}.tar.xz
#Source0:	http://portland.freedesktop.org/download/xdg-utils-%{version}%{?beta:-%{beta}}.tar.gz
Patch0:		xdg-utils-1.0.2-email_loop.patch
Patch1:		xdg-utils-1.0.2-email_silent_errors.patch
Patch2:		xdg-utils-1.0.3-enable-xdg-terminal.patch
BuildRequires:	libxslt-proc
BuildRequires:	gawk
BuildRequires:	xmlto
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
Requires:	desktop-file-utils
Requires:	xprop
Requires:	xset
BuildArch:	noarch

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
%setup -qn %{name}-%{gitdate}

%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%configure2_5x

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
%{_mandir}/man1/xdg-desktop-icon.*
%{_mandir}/man1/xdg-desktop-menu.*
%{_mandir}/man1/xdg-email.*
%{_mandir}/man1/xdg-icon-resource.*
%{_mandir}/man1/xdg-mime.*
%{_mandir}/man1/xdg-open.*
%{_mandir}/man1/xdg-screensaver.*
%{_mandir}/man1/xdg-terminal.*


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1.0.3-0.20100204.5mdv2011.0
+ Revision: 672353
- add br
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Feb 25 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-0.20100204.3mdv2011.0
+ Revision: 511100
- add missing requires on xset (#55101)

* Thu Feb 04 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.3-0.20100204.2mdv2010.1
+ Revision: 500941
- readd accidentally removed (rediffed) patch 1
- renumber actual p1 to p2

* Thu Feb 04 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.3-0.20100204.1mdv2010.1
+ Revision: 500813
- BR docbook-dtd412-xml
- new cvs snapshot (mainly kde4 fixes)
- use make
- diff patch to enable xdg-terminal
- use cvs switch

* Tue Dec 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-16mdv2010.1
+ Revision: 478865
- P2: Silent errors

* Tue Dec 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-15mdv2010.1
+ Revision: 478814
- Add back xdg-utils-1.0.2-email_loop.patch removed by error

* Sun Sep 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-14mdv2010.0
+ Revision: 444793
- Update to xdg-utils trunk ( fix a lot of kde4 issues)

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-13mdv2010.0
+ Revision: 444763
- Add patch7 : Fix kde4 support in xdg-open

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-12mdv2009.1
+ Revision: 351208
- rebuild

* Wed Sep 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-11mdv2009.0
+ Revision: 279353
- typo typo typo ...

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-10mdv2009.0
+ Revision: 278060
- Fix typo in xdg-utils-1.0.2-detect-KDE4.patch

* Sun Aug 31 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-9mdv2009.0
+ Revision: 277921
- Fix sed
- Move sed out of %%post
- Remove broken patch7

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-8mdv2009.0
+ Revision: 277599
- [BUGFIX] harcode path of kmailservice under kde4 if not kde3 one will be used (#41819)
- [BUGFIX] Fix  kfmclient_fix_exit_code under KDE4 (tks to Luc Menut )(Bug #41818)
- Start to support kde4

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2009.0
+ Revision: 226028
- rebuild
- fix description-line-too-long

* Fri Feb 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.2-5mdv2008.1
+ Revision: 161209
- Fix CVE-2008-0386 (Bug #37380)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.2-4mdv2008.1
+ Revision: 102592
- Make MIME type detection under GNOME more robust (upstream #12818)

* Tue Aug 28 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.0.2-3mdv2008.0
+ Revision: 72822
- Enhance error reporting for xdg-email by reporting via zenity/kdialog when possible.
- Fixes FF/xdg-email looping. Closes: #32535

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requries (#32123)

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 44254
- new version
- spec file clean


* Tue Feb 20 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-3mdv2007.0
+ Revision: 123080
-Drop test-suite subpackage, not working correctly
-Patch0: fix xdg-mime default applications (Mdv bug #28711)

* Thu Nov 30 2006 Laurent Montel <lmontel@mandriva.com> 1.0.1-2mdv2007.1
+ Revision: 89361
- Increase release
- Separate test suite file into own package

* Wed Nov 15 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-1mdv2007.1
+ Revision: 84271
- Fix spec
- Use good tarball
- New release 1.0.1
- xdg-utils-1.0-0.rc1.1mdv2007.0
- xdg-utils-1.0-0.beta3.1mdv2007.0
- Remove Patch0: Merged upstream
- Fix patch 0: thanks chty for your tests
- Use right release
- Increase release
- Fix wrong requires (thanks chty)

* Mon Aug 07 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-0.beta1.3mdv2007.0
+ Revision: 53417
- Increase release
- Add Mandriva in the result of the test suite
  before :  distribution: distribution unknown
  now    :  distribution: Mandriva Linux 2007.0
- Package the test-suite too
- Add Requires

* Sun Aug 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-0.beta1.2mdv2007.0
+ Revision: 53194
-1.0 beta2
- Fix description
- Increase release
- import xdg-utils-1.0-0.beta1.0mdv2007.0

