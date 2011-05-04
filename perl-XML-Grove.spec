%define upstream_name	 XML-Grove
%define upstream_version 0.46alpha

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Provides the information set of parsed XML/HTML/SGML trees
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The XML::Grove Perl module provides simple access to the information
set of parsed XML, HTML, or SGML instances using a tree of Perl
hashes.  This package also includes several extensions to XML::Grove
that provide the following:

   - returning element contents as a string
   - returning element contents as XML, HTML, or Canonical XML
   - processing entire groves using the visitor pattern
   - processing entire groves using PerlSAX
   - running a filter over all nodes in the grove
   - substituting values into an XML template grove
   - indexing a grove by ID or other attributes
   - accessing elements and objects via URL-like paths
   - create grove objects using an easy shorthand

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/XML/*
