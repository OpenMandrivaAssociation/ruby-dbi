%define base_name	dbi
%define name	ruby-%{base_name}
%define version	0.2.0
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A database independent interface for accessing database
Group:		Development/Ruby
License:	BSD-like
URL:		http://ruby-dbi.rubyforge.org/
Source:		http://rubyforge.org/frs/download.php/33959/%{base_name}-%{version}.tar.gz
BuildRequires:	ruby
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Ruby/DBI is a database interface in the spirit of Perl's prolific DBI authored
by Tim Bunce.

%prep
%setup -q -n %{base_name}-%{version}

%build
ruby setup.rb config --with=dbi,dbd_proxy,dbd_sqlite,dbd_mysql,dbd_pg,dbd_sqlite3,dbd_odbc,dbd_ado,dbd_sqlrelay \
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
%ruby_vendorlibdir/DBD
%ruby_vendorlibdir/dbi*

