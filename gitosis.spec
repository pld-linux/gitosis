# TODO:
# - should it provide git account, or let admin create it on his own?
#   pros: service working out-of-the-box
#   cons: admin may want to use other name than git
#   Note that it is not a daemon.
# - what to do with all these .conf files?
# - how is it excpected to cooperate with git-daemon?
Summary:	Software for hosting git repositories
Summary(pl.UTF-8):	Narzędzie do hostowania repozytoriów git
Name:		gitosis
Version:	20100816
Release:	0.1
License:	GPL v2
Group:		Development/Tools
# git://eagain.net/gitosis.git
Source0:	http://execve.pl/PLD/%{name}-%{version}.tar.bz2
# Source0-md5:	290a91ce5ff9173810518d5a42a03bcb
URL:		http://eagain.net/gitweb/?p=gitosis.git
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	git-core
Requires:	python-distribute
Requires:	python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software for hosting git repositories.

%description -l pl.UTF-8
Narzędzie do hostowania repozytoriów git.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/gitosis/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst TODO.rst example.conf gitweb.conf lighttpd-gitweb.conf etc-event.d-local-git-daemon
%dir %{py_sitescriptdir}/gitosis
%{py_sitescriptdir}/gitosis/*.py[co]
%{py_sitescriptdir}/gitosis/templates
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/gitosis-*.egg-info
%endif

%attr(755,root,root) %{_bindir}/gitosis-init
%attr(755,root,root) %{_bindir}/gitosis-run-hook
%attr(755,root,root) %{_bindir}/gitosis-serve
