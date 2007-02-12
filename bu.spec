Summary:	bu - Incremental NFS BackUp tool
Summary(pl.UTF-8):	bu - system przyrostowych kopii zapasowych po NFS-ie
Name:		bu
Version:	2.8
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.hightek.org/bu/download/%{name}-%{version}.tar.gz
# Source0-md5:	4f4e81c3a983e93f50c3b9a2991066dc
URL:		http://hightek.org/bu/
# /var/backups cannot be used arbitrary by new applications
BuildRequires:	FHS-fix
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small but very configurable incremental backup tool written
in Unix shell script. It is designed to backup files to other file
systems as opposed to backing up to tape. It is very simple to use,
yet has many features one would expect from a sophisticated backup
tool, such as nice logs, and include and exclude file filters with
wild card capability.

%description -l pl.UTF-8
Jest to małe, ale o dużych możliwościach konfiguracyjnych narzędzie do
kopii zapasowych napisane jako skrypt powłoki. Zostało stworzone do
tworzenia kopii zapasowych plików na inne systemy jak na taśmę. Jest
bardzo proste w użytkowaniu, pomimo iż ma wiele możliwości, których
można oczekiwać po rozbudowanym programie tego typu, takich jak
przyjemne logi, włączanie i wyłączanie plików przy zastosowaniu masek.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_var}/backups/bu

cp bu $RPM_BUILD_ROOT%{_bindir}
cp Include Exclude $RPM_BUILD_ROOT%{_var}/backups/bu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README white_paper
%attr(755,root,root) %{_bindir}/bu
%dir %{_var}/backups
%{_var}/backups/bu
