Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen für Systemdienste und fragt diese ab
Summary(fr):	Mises à jour et interrogations des services systèmes
Summary(pl):	Narzêdzie do aktualizacji i odpytywania o informacje nt serwisów systemowych
Summary(pt_BR):	Ferramenta para atualizar e listar serviços do sistema, pelo nível de execução (runlevel)
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Name:		chkconfig
Version:	1.0.5
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pt_BR):	Utilitários/Sistema
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.redhat.com/pub/redhat/code/chkconfig/%{name}-%{version}.tar.gz
Source1:	chkconfig.pl.po
Patch:		chkconfig-opt.patch
BuildPrereq:	slang-devel
BuildPrereq:	newt-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
chkconfig provides a simple command-line  tool  for  maintaining  the
/etc/rc.d  directory  hierarchy by relieving system administrators of
directly manipulating the  numerous symbolic links in that directory.

%description -l de
chkconfig bietet ein einfaches Befehlszeilen-Tool zum Verwalten der
Verzeichnishierarchie /etc/rc.d, indem es dem Systemadministrator das direkte
Bearbeiten der zahlreichen symbolischen Verknüpfungen in diesem
Verzeichnis abnimmt.

%description -l fr
chkconfig offre un outil simple en ligne de commande pour maintenir la
hiérarchie du répertoire /etc/rc.d tout en évitant aux administrateurs
système de manipuler les différents liens symbolique de ce répertoire.

%description -l pl
Pakiet chkconfig udostêpnia proste narzêdzia do zarz±dzania zawarto¶ci±
katalogów w /etc/rc.d

%description -l pt_BR
Chkconfig provê uma ferramenta simples na linha de comando
para manter a hierarquia de diretórios /etc/rc.d, aliviando os
administradores do sistema da manipulação direta de numerosos
links simbólicos.

%description -l tr
Saðladýðý basit bir komut satýrý programý yardýmýyla, /etc/rc.d dizinlerinin
yapýsýyla ilgilenerek sistem yöneticilerinin bu dizinlerde bulunan çok
sayýdaki simgesel baðlantýyý düzenleme iþini hafifletir.

%package -n ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(pt_BR):	Interface com menus para configuração de informações de níveis de execução
Group:		Utilities/System
Group(pt_BR):	Utilitários/Sistema
Group(pl):	Narzêdzia/System
Requires:	%{name} = %{version}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d directory
hierarchy, which controls the starting and stopping of system services.

%description -l pl -n ntsysv
ntsysv udostêpnia pe³noekranowe narzêdzie do aktualizowania zawarto¶ci
katalogów w /etc/rc.d, które kontroluj± startowanie i stopowanie
poszczególnych serwisów systemowych.

%description -l pt_BR -n ntsysv
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diretórios /etc/rc.d, que controla a inicialização e a
terminação de serviços do sistema.

%prep
%setup -q
%patch -p1

install %{SOURCE1} po/pl.po

%build

%ifarch sparc
LIBMHACK=-lm
%endif

make \
	OPTIMIZE="$RPM_OPT_FLAGS" \
	LIBMHACK="$LIBMHACK"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/{init,rc{0,1,2,3,4,5,6}}.d

make instroot=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/chkconfig

%lang(cs)     /usr/share/locale/cs/LC_MESSAGES/chkconfig.mo
%lang(de)     /usr/share/locale/de/LC_MESSAGES/chkconfig.mo
%lang(en)     /usr/share/locale/en*/LC_MESSAGES/chkconfig.mo
%lang(fr)     /usr/share/locale/fr/LC_MESSAGES/chkconfig.mo
%lang(no)     /usr/share/locale/no/LC_MESSAGES/chkconfig.mo
%lang(pl)     /usr/share/locale/pl/LC_MESSAGES/chkconfig.mo
%lang(pt_BR)  /usr/share/locale/pt_BR/LC_MESSAGES/chkconfig.mo
%lang(ro)     /usr/share/locale/ro/LC_MESSAGES/chkconfig.mo
%lang(sk)     /usr/share/locale/sk/LC_MESSAGES/chkconfig.mo
%lang(sr)     /usr/share/locale/sr/LC_MESSAGES/chkconfig.mo
%lang(tr)     /usr/share/locale/tr/LC_MESSAGES/chkconfig.mo

/usr/man/man8/chkconfig.8*

%dir /etc/rc.d
%dir /etc/rc.d/*

%files -n ntsysv
%defattr(644,root,root,755)
%attr(755,root,root) /usr/sbin/ntsysv
/usr/man/man8/ntsysv.8*

%changelog
* Wed Apr 21 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.0.5-1]
- updated to 1.0.5,
- removed man group from man pages,
- added %defattr description in %files -n ntsysv,
- replacements in %files,
- added gzipping man pages,
- added %dir macros,
- fixed Requires in ntsysv,
- cosmetic changes,
- recompiled on rpm 3.

* Tue Jan 26 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.9.5-3]
- fixed pl translation,
- added "Group(pl)",
- cosmetics changes in %%files.

* Thu Oct 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.5-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %lang macros for files /usr/share/locale/*/LC_MESSAGES/chkconfig.mo
- added pl translation,
- fiew simplification in %files and %install,
- added "Requires: chkconfig = %%{version}" for ntsysv,
- added full %attr description in %files.

* Thu Oct 08 1998 Cristian Gafton <gafton@redhat.com>
- updated czech translation (and use cs instead of cz)

* Tue Sep 22 1998 Arnaldo Carvalho de Melo <acme@conectiva.com.br>
- added pt_BR translations
- added more translatable strings
- support for i18n init.d scripts description

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built against newt 0.30
- split ntsysv into a separate package

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- added numerous translations

* Mon Mar 23 1998 Erik Troan <ewt@redhat.com>
- added i18n support

* Sun Mar 22 1998 Erik Troan <ewt@redhat.com>
- added --back
