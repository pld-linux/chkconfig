Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen für Systemdienste und fragt diese ab
Summary(fr):	Mises à jour et interrogations des services systèmes
Summary(pl):	Narzêdzie do aktualizacji i odpytywania o informacje nt serwisów systemowych
Summary(pt_BR):	Ferramenta para atualizar e listar serviços do sistema, pelo nível de execução (runlevel)
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Name:		chkconfig
Version:	1.0.6
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pt_BR):	Utilitários/Sistema
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.redhat.com/pub/redhat/code/chkconfig/%{name}-%{version}.tar.gz
Source1:	chkconfig.pl.po
Patch0:		chkconfig-opt.patch
Patch1:		chkconfig-fhs.patch
Patch2:		chkconfig-pld.patch
BuildRequires:	slang-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
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

%package -n	ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(pt_BR):	Interface com menus para configuração de informações de \
Summary(pt_BR):	níveis de execução
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
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

install %{SOURCE1} po/pl.po

%build

%ifarch sparc
LIBMHACK=-lm
%endif

make 	OPTIMIZE="$RPM_OPT_FLAGS" \
	LIBMHACK="$LIBMHACK"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/{init,rc{0,1,2,3,4,5,6}}.d

make install \
    instroot=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/chkconfig

%{_mandir}/man8/chkconfig.8*

%dir /etc/rc.d
%dir /etc/rc.d/*

%files -n ntsysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ntsysv

%{_mandir}/man8/ntsysv.8*
