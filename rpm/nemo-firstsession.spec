Name:		nemo-firstsession
Version:	0.1
Release:	1
Summary:	Initial session setup for user

Group:		Base
License:	GPLv2
URL:		https://github.com/nemomobile/nemo-firstsession
Source0:	%{name}-%{version}.tar.bz2
Requires:	oneshot
Requires:	xdg-user-dirs
BuildRequires:	oneshot
BuildArch:	noarch

%{_oneshot_requires_post}

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}/%{_oneshotdir}
install -m 755 oneshot.d/* %{buildroot}/%{_oneshotdir}

%post
if [ "$1" -eq 1 ]; then
    %{_bindir}/add-oneshot --user 00-initial-user-setup
fi

%files
%defattr(-,root,root,-)
%{_oneshotdir}/*
