Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen f�r Systemdienste und fragt diese ab
Summary(fr):	Mises � jour et interrogations des services syst�mes
Summary(pl):	Narz�dzie do aktualizacji i odpytywania o informacje nt serwis�w systemowych
Summary(pt):	Ferramenta para atualizar e listar servi�os do sistema, pelo n�vel de execu��o (runlevel)
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Name:		chkconfig
Version:	1.2.22
Release:	4
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.redhat.com/pub/redhat/code/chkconfig/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-fhs.patch
Patch2:		%{name}-add.patch
Patch3:		%{name}-popt.patch
Patch4:		%{name}-rcdir.patch
Patch5:		%{name}-noxinet.patch
BuildRequires:	slang-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
Prereq:		popt
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chkconfig provides a simple command-line tool for maintaining the
/etc/rc.d directory hierarchy by relieving system administrators of
directly manipulating the numerous symbolic links in that directory.

%description -l de
chkconfig bietet ein einfaches Befehlszeilen-Tool zum Verwalten der
Verzeichnishierarchie /etc/rc.d, indem es dem Systemadministrator das
direkte Bearbeiten der zahlreichen symbolischen Verkn�pfungen in
diesem Verzeichnis abnimmt.

%description -l fr
chkconfig offre un outil simple en ligne de commande pour maintenir la
hi�rarchie du r�pertoire /etc/rc.d tout en �vitant aux administrateurs
syst�me de manipuler les diff�rents liens symbolique de ce r�pertoire.

%description -l pl
Pakiet chkconfig udost�pnia proste narz�dzia do zarz�dzania
zawarto�ci� katalog�w w /etc/rc.d .

%description -l pt_BR
Chkconfig prov� uma ferramenta simples na linha de comando para manter
a hierarquia de diret�rios /etc/rc.d, aliviando os administradores do
sistema da manipula��o direta de numerosos links simb�licos.

%description -l tr
Sa�lad��� basit bir komut sat�r� program� yard�m�yla, /etc/rc.d
dizinlerinin yap�s�yla ilgilenerek sistem y�neticilerinin bu
dizinlerde bulunan �ok say�daki simgesel ba�lant�y� d�zenleme i�ini
hafifletir.

%package -n ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(pl):	Pe�noekranowy interfejs do wybierania dzia�aj�cych us�ug systemowych
Summary(pt):	Interface com menus para configura��o de informa��es de n�veis de execu��o
Group:		Applications/System
Requires:	%{name} = %{version}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d
directory hierarchy, which controls the starting and stopping of
system services.

%description -n ntsysv -l pl
ntsysv udost�pnia pe�noekranowe narz�dzie do aktualizowania zawarto�ci
katalog�w w /etc/rc.d, kt�re kontroluj� startowanie i stopowanie
poszczeg�lnych serwis�w systemowych.

%description -n ntsysv -l pt_BR
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diret�rios /etc/rc.d, que controla a inicializa��o e a
termina��o de servi�os do sistema.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build

%ifarch sparc
LIBMHACK=-lm
%endif

%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBMHACK="$LIBMHACK"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/{init,rc{0,1,2,3,4,5,6}}.d

%{__make} install \
    instroot=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/chkconfig
%{_mandir}/man8/chkconfig.8*

%files -n ntsysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ntsysv
%{_mandir}/man8/ntsysv.8*
