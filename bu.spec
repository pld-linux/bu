Summary:	bu - Incremental NFS BackUp tool
Summary(pl):	bu - System backup'u inkrementalnego po NFS'ie
Name:		bu
Version:	2.8
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.hightek.org/bu/download/%{name}-%{version}.tar.gz
URL:		http://hightek.org/bu/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small but very configurable incremental backup tool written
in Unix shell script. It is designed to backup files to other file
systems as opposed to backing up to tape. It is very simple to use,
yet has many features one would expect from a sophisticated backup
tool, such as nice logs, and include and exclude file filters with
wild card capability.

%description -l pl
Jest to ma³e, ale o du¿ych mo¿liwo¶ciach konfiguracyjnych narzêdzie do
backup'u napisane jako skrypt shell'owy. Zosta³o stworzone do backup'u
plików na inne sytemy jak na ta¶mê. Jest bardzo proste w u¿ytkowaniu,
pomimo i¿ ma wiele mo¿liwo¶ci, których mo¿na oczekiwaæ po rozbudowanym
programie tego typu, takich jak przyjemne logi, includowanie i
excludowanie plików przy zastosowaniu masek.

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
%{_var}/backups/bu
