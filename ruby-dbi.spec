%define base_name	dbi
%define name	ruby-%{base_name}
%define version	0.4.3
%define release	3

# Be backportable
%{!?ruby_vendorlibdir:%define ruby_vendorlibdir %ruby_sitelibdir}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A database independent interface for accessing database
Group:		Development/Ruby
License:	BSD-like
URL:		https://ruby-dbi.rubyforge.org/
Source:		http://rubyforge.org/frs/download.php/63601/%{base_name}-%{version}.tar.gz
BuildRequires:	ruby
BuildArch:	    noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Ruby/DBI is a database interface in the spirit of Perl's prolific DBI authored
by Tim Bunce.

%prep
%setup -q -n %{base_name}-%{version}

%build
ruby setup.rb config \
	--bin-dir=%{buildroot}%{_bindir} \
	--rb-dir=%{buildroot}%{ruby_vendorlibdir}
ruby setup.rb setup

%install
rm -rf %{buildroot}
ruby setup.rb install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog examples LICENSE
%_bindir/*
%{ruby_vendorlibdir}/dbi*



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-2mdv2011.0
+ Revision: 614725
- the mass rebuild of 2010.1 packages

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 531332
- new version

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 397043
- new version

* Wed Sep 03 2008 Pascal Terjan <pterjan@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 279352
- Fix backports

* Tue Sep 02 2008 Pascal Terjan <pterjan@mandriva.org> 0.2.0-1mdv2009.0
+ Revision: 279046
- BuildRequires ruby
- import ruby-dbi


* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2009.0
- first mdv release
