%define base_name	dbi
%define name	ruby-%{base_name}
%define version	0.4.3
%define release	%mkrel 1

# Be backportable
%{!?ruby_vendorlibdir:%define ruby_vendorlibdir %ruby_sitelibdir}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A database independent interface for accessing database
Group:		Development/Ruby
License:	BSD-like
URL:		http://ruby-dbi.rubyforge.org/
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

