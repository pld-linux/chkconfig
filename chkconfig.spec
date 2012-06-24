Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen f�r Systemdienste und fragt diese ab
Summary(fr):	Mises � jour et interrogations des services syst�mes
Summary(pl):	Narz�dzie do aktualizacji i odpytywania o informacje nt serwis�w systemowych
Summary(pt_BR):	Ferramenta para atualizar e listar servi�os do sistema, pelo n�vel de execu��o (runlevel)
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Name:		chkconfig
Version:	1.0.6
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pt_BR):	Utilit�rios/Sistema
Group(pl):	Narz�dzia/System
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
Bearbeiten der zahlreichen symbolischen Verkn�pfungen in diesem
Verzeichnis abnimmt.

%description -l fr
chkconfig offre un outil simple en ligne de commande pour maintenir la
hi�rarchie du r�pertoire /etc/rc.d tout en �vitant aux administrateurs
syst�me de manipuler les diff�rents liens symbolique de ce r�pertoire.

%description -l pl
Pakiet chkconfig udost�pnia proste narz�dzia do zarz�dzania zawarto�ci�
katalog�w w /etc/rc.d

%description -l pt_BR
Chkconfig prov� uma ferramenta simples na linha de comando
para manter a hierarquia de diret�rios /etc/rc.d, aliviando os
administradores do sistema da manipula��o direta de numerosos
links simb�licos.

%description -l tr
Sa�lad��� basit bir komut sat�r� program� yard�m�yla, /etc/rc.d dizinlerinin
yap�s�yla ilgilenerek sistem y�neticilerinin bu dizinlerde bulunan �ok
say�daki simgesel ba�lant�y� d�zenleme i�ini hafifletir.

%package -n	ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(pt_BR):	Interface com menus para configura��o de informa��es de \
Summary(pt_BR):	n�veis de execu��o
Group:		Utilities/System
Group(pt_BR):	Utilit�rios/Sistema
Group(pl):	Narz�dzia/System
Requires:	%{name} = %{version}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d directory
hierarchy, which controls the starting and stopping of system services.

%description -l pl -n ntsysv
ntsysv udost�pnia pe�noekranowe narz�dzie do aktualizowania zawarto�ci
katalog�w w /etc/rc.d, kt�re kontroluj� startowanie i stopowanie
poszczeg�lnych serwis�w systemowych.

%description -l pt_BR -n ntsysv
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diret�rios /etc/rc.d, que controla a inicializa��o e a
termina��o de servi�os do sistema.

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
