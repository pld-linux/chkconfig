
%bcond_with mr	# Use asteriskes and dashes in all languages
		# for `chkconfig --list` command (aplies more_readable.patch).
		# Note: it makes the program inconsistent with the rest
		# of the world (some people say).

Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen f�r Systemdienste und fragt diese ab
Summary(es):	Herramienta para actualizar y listar servicios del sistema, por nivel de ejecuci�n (runlevel)
Summary(fr):	Mises � jour et interrogations des services syst�mes
Summary(ja):	/etc/rc.d �γ��ؤ���ƥʥ󥹤��뤿��Υ����ƥ�ġ���
Summary(pl):	Narz�dzie do aktualizacji i odpytywania o informacje nt serwis�w systemowych
Summary(pt):	Ferramenta para atualizar e listar servi�os do sistema, pelo n�vel de execu��o (runlevel)
Summary(ru):	��������� ������� ��� ���������� ��������� /etc/rc.d
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Summary(uk):	�������� ���̦�� ��� ��������� �����Ȧ�� /etc/rc.d
Name:		chkconfig
Version:	1.2.24h
Release:	10%{?with_mr:+mr}
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.buttsoft.com/~thumper/downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5: 032eae68329d07d0844775486ac74668
Patch0:		%{name}-add.patch
Patch1:		%{name}-noxinet.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-ponames.patch
Patch4:		%{name}-link.patch
Patch5:		%{name}-more_readable.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
BuildRequires:	slang-devel
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

%description -l es
Chkconfig provee una herramienta sencilla en la l�nea de comando para
mantener la jerarqu�a de directorios /etc/rc.d, atenuando los
administradores del sistema del manejo directo de numerosos links
simb�licos.

%description -l fr
chkconfig offre un outil simple en ligne de commande pour maintenir la
hi�rarchie du r�pertoire /etc/rc.d tout en �vitant aux administrateurs
syst�me de manipuler les diff�rents liens symbolique de ce r�pertoire.

%description -l ja
chkconfig
�ϴ���Ū�ʥ����ƥ�桼�ƥ���ƥ��Ǥ��롣����ϥ����ƥॵ���ӥ���
runlevel �ξ���򥢥åץǡ��Ȥ両�ڤ��롣chkconfig �� /etc/rc.d ��
¿���Υ���ܥ�å���󥯤����ޤ��Τǡ������ƥ�����Ԥϼ�ư��
����ܥ�å���󥯤򤿤Ӥ��ӥ��ǥ��åȤ��ʤ��Ƥ�褤��

%description -l pl
Pakiet chkconfig udost�pnia proste narz�dzia do zarz�dzania
zawarto�ci� katalog�w w /etc/rc.d .

%description -l pt_BR
Chkconfig prov� uma ferramenta simples na linha de comando para manter
a hierarquia de diret�rios /etc/rc.d, aliviando os administradores do
sistema da manipula��o direta de numerosos links simb�licos.

%description -l ru
chkconfig - ��� ������� ������� ��������� ������, ��������������� ���
���������� ��������� /etc/rc.d, ������������� ����������
�������������� �� ������������� ������� ���������/�������
�������������� �������� � ���� ��������.

%description -l tr
Sa�lad��� basit bir komut sat�r� program� yard�m�yla, /etc/rc.d
dizinlerinin yap�s�yla ilgilenerek sistem y�neticilerinin bu
dizinlerde bulunan �ok say�daki simgesel ba�lant�y� d�zenleme i�ini
hafifletir.

%description -l uk
chkconfig - �� ������ ���̦�� ���������� �����, ���������� ���
��������� �����Ȧ�� /etc/rc.d, ��� �צ���Ѥ ���������� ��ͦΦ��������
צ� ����Ȧ����Ԧ ������ ����������/�������� ������Φ �������Φ
��������� � ����� ������ڦ.

%package -n ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(es):	Interface con men�s para configuraci�n de informaci�n de niveles de ejecuci�n
Summary(ja):	/etc/rc.d �����ؤ���ƥʥ󥹤��륷���ƥ�ġ���
Summary(pl):	Pe�noekranowy interfejs do wybierania dzia�aj�cych us�ug systemowych
Summary(pt):	Interface com menus para configura��o de informa��es de n�veis de execu��o
Summary(ru):	������������� ��������� ��� ��������� ������� ����������
Summary(uk):	������������� ��������� ��� ������������ Ҧ�Φ� ���������
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d
directory hierarchy, which controls the starting and stopping of
system services.

%description -n ntsysv -l es
ntsysv ofrece una herramienta basada en men�s para actualizar la
jerarqu�a de directorios /etc/rc.d, que controla el arranque y el
cierre de servicios del sistema.

%description -n ntsysv -l ja
ntsysv �ϥ����ƥॵ���ӥ��� runlevel �ξ���򥢥åץǡ��Ȥ両�ڤ��롣
ntsysv �� �����ƥ�����Ԥ�ľ��/etc/rc.d ��¿���Υ���ܥ�å���󥯤�
���뤳�Ȥ���������롣

%description -n ntsysv -l pl
ntsysv udost�pnia pe�noekranowe narz�dzie do aktualizowania zawarto�ci
katalog�w w /etc/rc.d, kt�re kontroluj� w��czanie i wy��czanie
poszczeg�lnych serwis�w systemowych.

%description -n ntsysv -l pt_BR
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diret�rios /etc/rc.d, que controla a inicializa��o e a
termina��o de servi�os do sistema.

%description -n ntsysv -l ru
ntsysv - ��� ������������� ������� ��� ���������� � ��������� ��������
��������� /etc/rc.d, ������� ��������� �������� � ���������� ���������
��������.

%description -n ntsysv -l uk
ntsysv - �� ������������ ���̦�� ��� ��������� �� �ͦ�� �����Ȧ�
������Ǧ� /etc/rc.d, ���Ҧ ������� �������� �� �������� ���������
���צӦ�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{?with_mr:%patch5 -p1}

mv -f po/{eu_ES,eu}.po
mv -f po/{no,nb}.po
mv -f po/{sr,sr@Latn}.po
mv -f po/{zh,zh_TW}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-max-level=6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/{init,rc{0,1,2,3,4,5,6}}.d,/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sbindir}/chkconfig $RPM_BUILD_ROOT/sbin

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
