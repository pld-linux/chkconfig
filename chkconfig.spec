Summary:	Updates and queries runlevel information for system services
Summary(de.UTF-8):	Aktualisiert runlevel-Informationen für Systemdienste und fragt diese ab
Summary(es.UTF-8):	Herramienta para actualizar y listar servicios del sistema, por nivel de ejecución (runlevel)
Summary(fr.UTF-8):	Mises à jour et interrogations des services systèmes
Summary(ja.UTF-8):	/etc/rc.d の階層をメンテナンスするためのシステムツール
Summary(pl.UTF-8):	Narzędzie do aktualizacji i odpytywania o informacje nt serwisów systemowych
Summary(pt.UTF-8):	Ferramenta para atualizar e listar serviços do sistema, pelo nível de execução (runlevel)
Summary(ru.UTF-8):	Системная утилита для управления иерархией /etc/rc.d
Summary(tr.UTF-8):	Sistem servis bilgilerini sorgular ve yeniler
Summary(uk.UTF-8):	Системна утиліта для керування ієрархією /etc/rc.d
Name:		chkconfig
Version:	1.32
Release:	1
Epoch:		2
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/fedora-sysv/chkconfig/releases
Source0:	https://github.com/fedora-sysv/chkconfig/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	19f00c055c7af343fcf18a03088f5533
Patch0:		%{name}-add.patch
Patch1:		%{name}-noxinet.patch
Patch2:		%{name}-rc.d.patch
Patch3:		%{name}-optflags.patch
Patch4:		%{name}-pl.patch
Patch5:		%{name}-split-usr.patch
URL:		https://github.com/fedora-sysv/chkconfig
BuildRequires:	gettext-tools
BuildRequires:	libselinux-devel
BuildRequires:	newt-devel
BuildRequires:	popt-devel
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chkconfig provides a simple command-line tool for maintaining the
/etc/rc.d directory hierarchy by relieving system administrators of
directly manipulating the numerous symbolic links in that directory.

%description -l de.UTF-8
chkconfig bietet ein einfaches Befehlszeilen-Tool zum Verwalten der
Verzeichnishierarchie /etc/rc.d, indem es dem Systemadministrator das
direkte Bearbeiten der zahlreichen symbolischen Verknüpfungen in
diesem Verzeichnis abnimmt.

%description -l es.UTF-8
Chkconfig provee una herramienta sencilla en la línea de comando para
mantener la jerarquía de directorios /etc/rc.d, atenuando los
administradores del sistema del manejo directo de numerosos links
simbólicos.

%description -l fr.UTF-8
chkconfig offre un outil simple en ligne de commande pour maintenir la
hiérarchie du répertoire /etc/rc.d tout en évitant aux administrateurs
système de manipuler les différents liens symbolique de ce répertoire.

%description -l ja.UTF-8
chkconfig
は基本的なシステムユーティリティである。これはシステムサービスの
runlevel の情報をアップデートや検証する。chkconfig は /etc/rc.d の
多数のシンボリックリンクを操作しますので、システム管理者は手動で
シンボリックリンクをたびたびエディットしなくてもよい。

%description -l pl.UTF-8
Pakiet chkconfig udostępnia proste narzędzia do zarządzania
zawartością katalogów w /etc/rc.d .

%description -l pt_BR.UTF-8
Chkconfig provê uma ferramenta simples na linha de comando para manter
a hierarquia de diretórios /etc/rc.d, aliviando os administradores do
sistema da manipulação direta de numerosos links simbólicos.

%description -l ru.UTF-8
chkconfig - это простая утилита командной строки, предназначенная для
управления иерархией /etc/rc.d, освобождающая системного
администратора от необходимости вручную создавать/удалять
многочисленные симлинки в этом каталоге.

%description -l tr.UTF-8
Sağladığı basit bir komut satırı programı yardımıyla, /etc/rc.d
dizinlerinin yapısıyla ilgilenerek sistem yöneticilerinin bu
dizinlerde bulunan çok sayıdaki simgesel bağlantıyı düzenleme işini
hafifletir.

%description -l uk.UTF-8
chkconfig - це проста утиліта командного рядка, призначена для
керування ієрархією /etc/rc.d, яка звільняє системного адміністратора
від необхідності вручну створювати/видаляти численні символьні
посилання в цьому каталозі.

%package -n ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(es.UTF-8):	Interface con menús para configuración de información de niveles de ejecución
Summary(ja.UTF-8):	/etc/rc.d 階階層をメンテナンスするシステムツール
Summary(pl.UTF-8):	Pełnoekranowy interfejs do wybierania działających usług systemowych
Summary(pt.UTF-8):	Interface com menus para configuração de informações de níveis de execução
Summary(ru.UTF-8):	Полноэкранный интерфейс для настройки уровней исполнения
Summary(uk.UTF-8):	Повноекранний інтерфейс для налагодження рівнів виконання
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d
directory hierarchy, which controls the starting and stopping of
system services.

%description -n ntsysv -l es.UTF-8
ntsysv ofrece una herramienta basada en menús para actualizar la
jerarquía de directorios /etc/rc.d, que controla el arranque y el
cierre de servicios del sistema.

%description -n ntsysv -l ja.UTF-8
ntsysv はシステムサービスの runlevel の情報をアップデートや検証する。
ntsysv は システム管理者が直接/etc/rc.d の多数のシンボリックリンクを
操作することから解放する。

%description -n ntsysv -l pl.UTF-8
ntsysv udostępnia pełnoekranowe narzędzie do aktualizowania zawartości
katalogów w /etc/rc.d, które kontrolują włączanie i wyłączanie
poszczególnych serwisów systemowych.

%description -n ntsysv -l pt_BR.UTF-8
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diretórios /etc/rc.d, que controla a inicialização e a
terminação de serviços do sistema.

%description -n ntsysv -l ru.UTF-8
ntsysv - это полноэкранная утилита для обновления и изменения иерархии
каталогов /etc/rc.d, которые управляют запуском и остановкой системных
сервисов.

%description -n ntsysv -l uk.UTF-8
ntsysv - це повноекранна утиліта для оновлення та зміни ієрархії
каталогів /etc/rc.d, котрі керують запуском та зупинкою системних
сервісів.

%package -n alternatives
Summary:	Maintain symbolic links determining default commands
Summary(pl.UTF-8):	Utrzymywanie dowiązań symbolicznych określających domyślne polecenia
Group:		Applications/System

%description -n alternatives
alternatives creates, removes, maintains and displays information
about the symbolic links comprising the alternatives system. The
alternatives system is a reimplementation of the Debian alternatives
system. It was rewritten primarily to remove the dependence on Perl;
it is intended to be a drop in replacement for Debian's
update-alternatives script.

%description -n alternatives -l pl.UTF-8
alternatives tworzy, usuwa, utrzymuje i wyświetla informacje o
dowiązaniach symbolicznych obejmujących system alternatyw. System
alternatyw to reimplementacja systemu alternatyw ("alternatives") z
Debiana. Została napisana głównie w celu usunięcia zależności od
Perla; ma być zamiennikiem skryptu update-alternatives z Debiana.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcppflags} %{rpmcflags}" \
	OPTLDFLAGS="%{rpmldflags}" \
	SYSTEMDUTILDIR=/lib/systemd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/{init,rc{0,1,2,3,4,5,6}}.d,env.d},/sbin,/var/lib/alternatives}

%{__make} install \
	BINDIR=/sbin \
	MANDIR=%{_mandir} \
	SYSTEMDUTILDIR=/lib/systemd \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bal

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/chkconfig
%attr(755,root,root) /lib/systemd/systemd-sysv-install
%{_mandir}/man8/chkconfig.8*

%files -n ntsysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ntsysv
%{_mandir}/man8/ntsysv.8*

%files -n alternatives
%defattr(644,root,root,755)
%dir %{_sysconfdir}/alternatives
%attr(755,root,root) %{_sbindir}/alternatives
%attr(755,root,root) %{_sbindir}/update-alternatives
%dir /var/lib/alternatives
%{_mandir}/man8/alternatives.8*
%{_mandir}/man8/update-alternatives.8*
