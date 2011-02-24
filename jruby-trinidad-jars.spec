# Generated from trinidad_jars-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(jruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(jruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname trinidad_jars
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Tomcat's jars packed for Trinidad
Name: jruby-trinidad-jars
Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/calavera/trinidad
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: jruby 
BuildRequires: jruby 
BuildArch: noarch
Provides: jruby-trinidad-jars = %{version}

%description
Bundled version of Tomcat packed for Trinidad


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
jgem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Feb 24 2011 Sergio Rubio <rubiojr@frameos.org> - 1.0.0-1
- upstream update

* Fri Oct 15 2010 Sergio Rubio <rubiojr@frameos.org> - 0.3.2-1
- Initial package
