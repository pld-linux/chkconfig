
%bcond_with mr	# Use asteriskes and dashes in all languages
		# for `chkconfig --list` command (aplies more_readable.patch).
		# Note: it makes the program inconsistent with the rest
		# of the world (some people say).

Summary:	Updates and queries runlevel information for system services
Summary(de):	Aktualisiert runlevel-Informationen fЭr Systemdienste und fragt diese ab
Summary(es):	Herramienta para actualizar y listar servicios del sistema, por nivel de ejecuciСn (runlevel)
Summary(fr):	Mises Ю jour et interrogations des services systХmes
Summary(ja):	/etc/rc.d ╓нЁ╛аь╓Р╔А╔С╔ф╔й╔С╔╧╓╧╓К╓©╓А╓н╔╥╔╧╔ф╔Ю╔д║╪╔К
Summary(pl):	NarzЙdzie do aktualizacji i odpytywania o informacje nt serwisСw systemowych
Summary(pt):	Ferramenta para atualizar e listar serviГos do sistema, pelo nМvel de execuГЦo (runlevel)
Summary(ru):	Системная утилита для управления иерархией /etc/rc.d
Summary(tr):	Sistem servis bilgilerini sorgular ve yeniler
Summary(uk):	Системна утил╕та для керування ╕╓рарх╕╓ю /etc/rc.d
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
direkte Bearbeiten der zahlreichen symbolischen VerknЭpfungen in
diesem Verzeichnis abnimmt.

%description -l es
Chkconfig provee una herramienta sencilla en la lМnea de comando para
mantener la jerarquМa de directorios /etc/rc.d, atenuando los
administradores del sistema del manejo directo de numerosos links
simbСlicos.

%description -l fr
chkconfig offre un outil simple en ligne de commande pour maintenir la
hiИrarchie du rИpertoire /etc/rc.d tout en Иvitant aux administrateurs
systХme de manipuler les diffИrents liens symbolique de ce rИpertoire.

%description -l ja
chkconfig
╓о╢Пкэе╙╓й╔╥╔╧╔ф╔Ю╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓г╓╒╓К║ё╓Ё╓Л╓о╔╥╔╧╔ф╔Ю╔╣║╪╔с╔╧╓н
runlevel ╓н╬ПйС╓Р╔╒╔ц╔в╔г║╪╔х╓Д╦║╬з╓╧╓К║ёchkconfig ╓о /etc/rc.d ╓н
б©©Т╓н╔╥╔С╔э╔Й╔ц╔╞╔Й╔С╔╞╓РаЮ╨Н╓╥╓ч╓╧╓н╓г║╒╔╥╔╧╔ф╔Ю╢имЩ╪т╓о╪Йф╟╓г
╔╥╔С╔э╔Й╔ц╔╞╔Й╔С╔╞╓Р╓©╓с╓©╓с╔╗╔г╔ё╔ц╔х╓╥╓й╓╞╓ф╓Б╓Х╓╓║ё

%description -l pl
Pakiet chkconfig udostЙpnia proste narzЙdzia do zarz╠dzania
zawarto╤ci╠ katalogСw w /etc/rc.d .

%description -l pt_BR
Chkconfig provЙ uma ferramenta simples na linha de comando para manter
a hierarquia de diretСrios /etc/rc.d, aliviando os administradores do
sistema da manipulaГЦo direta de numerosos links simbСlicos.

%description -l ru
chkconfig - это простая утилита командной строки, предназначенная для
управления иерархией /etc/rc.d, освобождающая системного
администратора от необходимости вручную создавать/удалять
многочисленные симлинки в этом каталоге.

%description -l tr
SaПladЩПЩ basit bir komut satЩrЩ programЩ yardЩmЩyla, /etc/rc.d
dizinlerinin yapЩsЩyla ilgilenerek sistem yЖneticilerinin bu
dizinlerde bulunan Гok sayЩdaki simgesel baПlantЩyЩ dЭzenleme iЧini
hafifletir.

%description -l uk
chkconfig - це проста утил╕та командного рядка, призначена для
керування ╕╓рарх╕╓ю /etc/rc.d, яка зв╕льня╓ системного адм╕н╕стратора
в╕д необх╕дност╕ вручну створювати/видаляти численн╕ символьн╕
посилання в цьому каталоз╕.

%package -n ntsysv
Summary:	Full-screen interface for configurating runlevel information
Summary(es):	Interface con menЗs para configuraciСn de informaciСn de niveles de ejecuciСn
Summary(ja):	/etc/rc.d Ё╛Ё╛аь╓Р╔А╔С╔ф╔й╔С╔╧╓╧╓К╔╥╔╧╔ф╔Ю╔д║╪╔К
Summary(pl):	PeЁnoekranowy interfejs do wybierania dziaЁaj╠cych usЁug systemowych
Summary(pt):	Interface com menus para configuraГЦo de informaГУes de nМveis de execuГЦo
Summary(ru):	Полноэкранный интерфейс для настройки уровней исполнения
Summary(uk):	Повноекранний ╕нтерфейс для налагодження р╕вн╕в виконання
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n ntsysv
ntsysv provides a full-screen tool for updating the /etc/rc.d
directory hierarchy, which controls the starting and stopping of
system services.

%description -n ntsysv -l es
ntsysv ofrece una herramienta basada en menЗs para actualizar la
jerarquМa de directorios /etc/rc.d, que controla el arranque y el
cierre de servicios del sistema.

%description -n ntsysv -l ja
ntsysv ╓о╔╥╔╧╔ф╔Ю╔╣║╪╔с╔╧╓н runlevel ╓н╬ПйС╓Р╔╒╔ц╔в╔г║╪╔х╓Д╦║╬з╓╧╓К║ё
ntsysv ╓о ╔╥╔╧╔ф╔Ю╢имЩ╪т╓╛д╬юэ/etc/rc.d ╓нб©©Т╓н╔╥╔С╔э╔Й╔ц╔╞╔Й╔С╔╞╓Р
аЮ╨Н╓╧╓К╓Ё╓х╓╚╓И╡РйЭ╓╧╓К║ё

%description -n ntsysv -l pl
ntsysv udostЙpnia peЁnoekranowe narzЙdzie do aktualizowania zawarto╤ci
katalogСw w /etc/rc.d, ktСre kontroluj╠ wЁ╠czanie i wyЁ╠czanie
poszczegСlnych serwisСw systemowych.

%description -n ntsysv -l pt_BR
O ntsysv fornece uma ferramenta baseada em menus para atualizar a
hierarquia de diretСrios /etc/rc.d, que controla a inicializaГЦo e a
terminaГЦo de serviГos do sistema.

%description -n ntsysv -l ru
ntsysv - это полноэкранная утилита для обновления и изменения иерархии
каталогов /etc/rc.d, которые управляют запуском и остановкой системных
сервисов.

%description -n ntsysv -l uk
ntsysv - це повноекранна утил╕та для оновлення та зм╕ни ╕╓рарх╕╖
каталог╕в /etc/rc.d, котр╕ керують запуском та зупинкою системних
серв╕с╕в.

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
