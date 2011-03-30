Summary:	Save Subversion commits to CVS repository
Name:		svn2cvs
Version:	0.1
Release:	0.1
License:	GPL
Group:		Development/Version Control
Source0:	%{name}.tbz2
# Source0-md5:	960f25ea89eb88fbbda7e404a6d0b1ae
URL:		http://svn2cvs.tigris.org/
BuildRequires:	perl-tools-pod
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This script will allows you to commit changes made to Subversion
repository to (read-only) CVS repository manually or from Subversion's
post-commit hook.

%prep
%setup -qn %{name}

%build
pod2man src/svn2cvs.pl > svn2cvs.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p src/svn2cvs.pl $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p svn2cvs.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/svn2cvs.1*
