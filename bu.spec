Summary:	bu - Incremental NFS BackUp tool
Name:		bu
Version:	2.8
Release:	1
License:	BSD
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.advancedresearch.org/bu/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is a small but very configurable incremental backup tool
written in Unix shell script.  It is designed to backup files
to other file systems as opposed to backing up to tape. It is 
very simple  to  use, yet  has many features one would expect
from  a  sophisticated backup tool, such  as  nice  logs, and
include and exclude file filters with wild card capability.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_var}/backups/bu


cp bu $RPM_BUILD_ROOT%{_bindir}
cp Include Exclude $RPM_BUILD_ROOT%{_var}/backups/bu

gzip -9nf Changelog README white_paper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/bu
%{_var}/backups/bu/*
